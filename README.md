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

./dados/
└── tabela.tsv

Todos os códigos desenvolvidos foram devidamente documentados no arquivo "main.ipynb" e separados em:
- Carregamento dos dados
- Cálculo da Abundância Relativa dos gêneros por amostra
- Elaboração de visualizações gráficas
- Criação de um relatório automatizado

## Resultados
Todos os resultados se encontram disponíveis em:

./resultados/
└── genero_abundancia_relativa.tsv (tabela com a abundância relativa de cada gênero)
└── grafico_barras_empilhadas.html (gráfico de barras empilhadas da distribuição dos gêneros nas duas amostras)
└── heatmap.html (outra sugestão de gráfico)
└── sankey.html (outra sugestão de gráfico)
└── relatorio.html (relatório automatizado com os resultados)
└── Resultados e discussão.docx (resultados e discussão)

