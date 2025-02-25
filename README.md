# Teste para Processo seletivo - Bioinformática GoGenetic
Candidato: Cleber Furtado Aksenen

## Overview
O projeto visa processar, visualizar e interpretar os resultados de microbiomas de amostras de microbioma intestinal.
Origem: Uma tabela (tabela.tsv), convertido de um formato BIOM.

## Requisitos
Para a execução do projeto, será necessário:
- Python versão 3

As seguintes bibliotecas:
- pandas
- numpy
- matplotlib
- seaborn
- plotly
- scipy
- scikit-learn

Para a instalação das bibliotecas de forma automática, execute:
```
pip install -r requirements.txt
```

## Processo
A tabela com os dados está disponível em:

```
./dados/
└── tabela.tsv
```

Todos os códigos desenvolvidos foram devidamente documentados no arquivo "main.ipynb" e separados em:
- Carregamento dos dados
- Cálculo da Abundância Relativa dos gêneros por amostra
- Elaboração de visualizações gráficas
- Criação de um relatório automatizado

## Resultados
Todos os resultados se encontram disponíveis em:

```
resultados/
├── genero_abundancia_relativa.tsv   # Tabela com a abundância relativa de cada gênero
├── grafico_barras_empilhadas.html   # Gráfico de barras empilhadas da distribuição dos gêneros
├── heatmap.html                     # Mapa de calor para visualização dos dados
├── sankey.html                       # Diagrama de Sankey para análise de fluxo de abundância
├── relatorio.html                    # Relatório automatizado consolidando os resultados
└── Resultados_e_Discussao.docx       # Documento com a análise e discussão dos resultados
```
