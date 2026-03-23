# Análise da Produtividade Apícola Brasileira (2000-2024)

**Autor:** Gabriel de Jesus Franca dos Santos  
**Orientador:** Prof. Dr. Marcus Williams Aquino de Carvalho  
**Instituição:** Universidade Federal da Paraíba (UFPB) – Campus IV (CCAE)  
**Curso:** Bacharelado em Sistemas de Informação

---

## 🐝 Sobre o Projeto
Este repositório contém o código-fonte, o tratamento de dados e as visualizações geradas para o meu **Trabalho de Conclusão de Curso (TCC)**. O objetivo principal é analisar a evolução da produção e do faturamento do mel no Brasil através de uma perspectiva de Ciência de Dados, cruzando fatores econômicos e geográficos.

## 🚀 Diferenciais Técnicos
* **Deflacionamento Monetário:** Uso do IPCA para atualização de valores históricos para a base de 2024, permitindo uma análise real do faturamento.
* **Análise por Biomas:** Cruzamento de dados de mais de 5.500 municípios com a malha de biomas do IBGE (2024).
* **Análise Temporal:** Estudo de 24 anos de série histórica (2000-2024), identificando impactos de eventos climáticos como *El Niño* e secas severas.

## 🛠️ Tecnologias e Ferramentas
* **Linguagem:** Python 3.x
* **Bibliotecas:** `pandas` (manipulação de dados), `matplotlib` e `seaborn` (visualização).
* **Ambiente:** Jupyter Notebook.
* **Dados:** IPEADATA e IBGE.

## 📖 Fontes de Dados
* **[IPEADATA](http://www.ipeadata.gov.br/)**: Dados de produção física, faturamento e índices de inflação (IPCA).
* **[IBGE](https://agenciadenoticias.ibge.gov.br/agencia-noticias/2012-agencia-de-noticias/noticias/40519-ibge-define-bioma-predominante-em-cada-municipio-brasileiro-para-fins-estatisticos)**: Definição de bioma predominante por município para fins estatísticos (2024).
* **[INMET](https://portal.inmet.gov.br/)**: Consulta de eventos climáticos históricos para correlação com as quedas de produtividade.

## 🔮 Roadmap de Evolução (Trabalhos Futuros)
Este projeto é a base para uma análise ainda mais profunda que incluirá:
- [ ] Integração com dados brutos de precipitação e temperatura do INMET.
- [ ] Correlação com índices de queimadas e desmatamento.
- [ ] Mapeamento da distribuição de espécies de abelhas nativas por região.

---
*Este trabalho foi desenvolvido originalmente como parte da disciplina de Análise de Dados e evoluiu para o Trabalho de Conclusão de Curso.*