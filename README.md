[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/62cuUVGE)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=20196675&assignment_repo_type=AssignmentRepo)
# Projeto da disciplina de análise de dados
 
- Membros da equipe: Gabriel de Jesus
- Objetivo do projeto: Analisar os fatores que afetam a produção e o faturamento anual de mel no Brasil

## Questões iniciais a serem respondidas
1. ### Como o valor do mel variou com o passar dos anos?
2. ### Quais regiões, estados e municípios são mais produtivos e/ou mais lucrativos? São as mesmas?

## Fontes de dados:
### Principais:
* [IPEADATA](http://www.ipeadata.gov.br/): 'Produção - mel de abelha' e 'Produção - mel de abelha - quantidade': possuem, respectivamente, dados sobre o valor arrecadado pela venda de mel, e a  quantidade produzida no brasil doas anos 1974 a 2024, organizados por níveis geográficos (pais, estados, municípios, áreas comparáveis, regiões metropolitanas etc). É preciso considerar que os valores de venda do mel estão deflacionados para o ano de 2010 e na casa dos mil, para esse porjeto os valores foram reajustados para valores deflacionados para o ano de 2024, e ajustados para a casa dos reais.
* [DADOS HISTÓRICOS ANUAIS do Instituo Nacional de Metereóloga](https://portal.inmet.gov.br/dadoshistoricos): contem dados do clima do pais em diferentes municípios e regiões do pais do anos de 2000 a 2025 (limitado ao dia de 31/07 durante a produção destes trabalho)
* Bioma de cada localidade [IBGE define bioma predominante em cada município brasileiro para fins estatísticos](https://agenciadenoticias.ibge.gov.br/agencia-noticias/2012-agencia-de-noticias/noticias/40519-ibge-define-bioma-predominante-em-cada-municipio-brasileiro-para-fins-estatisticos)   
* IPEADATA: Índice nacional de preços ao consumidor amplo (IPCA) geral: índice (dez. 1993 = 100), usado para um comparação justa do valor do mel com o passar dos anos. Os indices usados foram recalculados tendo 2024 como base usando recursos disponíveis no site da IPEADATA.

### Potenciais:   
* GBIF - presença das especieis nativas em cada região
* Desmatamento e Queimadas
* [Censo Agropecuário Tabela 6935](https://sidra.ibge.gov.br/tabela/6935): Número de estabelecimentos agropecuários com apicultura e Venda de produtos, Total de caixas de abelha e Quantidade de mel e cera de abelha, geleia real, própolis e pólen vendidos, por tipologia, condição do produtor em relação às terras, grupos de atividade econômica e grupos de área total (Vide Notas)

