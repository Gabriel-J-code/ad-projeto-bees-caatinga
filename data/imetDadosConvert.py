import pandas as pd
import os

def processar_arquivos_climaticos(pasta_origem, arquivo_saida):
    todos_os_dados = []

    # Lista todos os arquivos na pasta
    arquivos = [f for f in os.listdir(pasta_origem) if f.endswith('.csv')]
    
    if not arquivos:
        print("Nenhum arquivo CSV encontrado na pasta especificada.")
        return

    for arquivo in arquivos:
        caminho_completo = os.path.join(pasta_origem, arquivo)
        print(f"Processando: {arquivo}...")
        
        # 1. Extrair Metadados do cabeçalho (as primeiras 9 linhas)
        metadados = {}
        with open(caminho_completo, 'r', encoding='latin-1') as f:
            for _ in range(9):
                linha = f.readline().strip()
                if ':' in linha:
                    chave, valor = linha.split(':', 1)
                    metadados[chave.strip()] = valor.strip()
        
        # 2. Ler os dados climáticos
        # skiprows=10 pula o cabeçalho de metadados e a linha em branco
        try:
            df = pd.read_csv(caminho_completo, sep=';', skiprows=10, encoding='latin-1', decimal='.')
            
            # Remover colunas fantasmas (comuns em CSVs que terminam com ;)
            df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
            
            # 3. Injetar os metadados em novas colunas para cada linha
            for chave, valor in metadados.items():
                df[chave] = valor
            
            # Converter a coluna de data para o formato datetime do Pandas
            if 'Data Medicao' in df.columns:
                df['Data Medicao'] = pd.to_datetime(df['Data Medicao'], errors='coerce')

            todos_os_dados.append(df)
            
        except Exception as e:
            print(f"Erro ao processar {arquivo}: {e}")

    # 4. Consolidar e Salvar
    if todos_os_dados:
        df_final = pd.concat(todos_os_dados, ignore_index=True)
        
        # Substitui a string 'null' por um valor vazio real (NaN)
        df_final = df_final.replace('null', pd.NA)
        
        # Salva o arquivo final
        df_final.to_csv(arquivo_saida, index=False, sep=';', encoding='utf-8-sig')
        print(f"\nSucesso! Arquivo consolidado salvo como: {arquivo_saida}")
        print(f"Total de linhas processadas: {len(df_final)}")
    else:
        print("Nenhum dado foi processado.")

# --- CONFIGURAÇÃO ---
# Coloque o caminho da pasta onde estão seus arquivos originais
caminho_da_minha_pasta = 'data\dados imet mensais' 
nome_do_resultado = 'dados_climaticos_unificados.csv'

# Criar a pasta se não existir (apenas para teste)
if not os.path.exists(caminho_da_minha_pasta):
    os.makedirs(caminho_da_minha_pasta)
    print(f"Coloque seus arquivos CSV na pasta: {caminho_da_minha_pasta}")
else:
    processar_arquivos_climaticos(caminho_da_minha_pasta, nome_do_resultado)