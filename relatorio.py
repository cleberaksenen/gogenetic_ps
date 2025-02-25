import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Carregar os dados
df = pd.read_csv("tabela.tsv", sep="\t", skiprows=1)
df["Genero"] = df["taxonomy"].str.extract(r"g__(\w+)")

genero_abundancia = df.groupby("Genero")[["16S-Amostra1", "16S-Amostra2"]].sum()
genero_abundancia_relativa = (genero_abundancia.div(genero_abundancia.sum()) * 100).round(2)
genero_abundancia_relativa.columns = ["Amostra 1 (%)", "Amostra 2 (%)"]
genero_abundancia_relativa = genero_abundancia_relativa.reset_index()

# Criar gráfico interativo com Plotly
amostras = ["Amostra 01", "Amostra 02"]
cores = px.colors.qualitative.Plotly
trace_list = []
for i, genero in enumerate(genero_abundancia_relativa["Genero"].unique()):
    valores = genero_abundancia_relativa.loc[
        genero_abundancia_relativa["Genero"] == genero, ["Amostra 1 (%)", "Amostra 2 (%)"]
    ].values.flatten()
    
    trace = go.Bar(
        x=amostras,
        y=valores,
        name=genero,
        hovertemplate='<b>%{x}</b><br>Gênero: ' + genero + '<br>Abundância Relativa: %{y:.2f}%',
        marker=dict(color=cores[i % len(cores)], line=dict(color="black", width=0.7)),
    )
    trace_list.append(trace)

layout = go.Layout(
    title=dict(
        text="Distribuição dos Gêneros nas Amostras",
        x=0.5,
        font=dict(size=16, family="Arial, sans-serif", color="black")
    ),
    xaxis=dict(
        title="Amostras",
        tickfont=dict(size=14),
        showline=True,
        linecolor="black"
    ),
    yaxis=dict(
        title="Abundância Relativa (%)",
        tickfont=dict(size=14),
        showgrid=True,
        gridcolor="lightgrey",
        zeroline=True,
        zerolinecolor="black"
    ),
    barmode="stack",
    legend=dict(
        title="Gêneros",
        x=1.02,
        y=1,
        font=dict(size=12)
    ),
    plot_bgcolor="white",
    margin=dict(t=60, r=50, b=60, l=70),
)

fig = go.Figure(data=trace_list, layout=layout)

# Gerar tabela em HTML formatada
tabela_html = genero_abundancia_relativa.to_html(index=False, classes='table table-striped table-responsive text-center', border=0)

# Criar relatório em HTML
html_content = f'''
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Relatório de Abundância Relativa</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.0/css/bootstrap.min.css">
    <style>
        .container {{
            max-width: 800px;
            margin: auto;
        }}
        table {{
            width: 100%;
            text-align: center;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1 class="text-center mt-4">Relatório de Abundância Relativa</h1>
        <hr>
        <h2 class="text-center">Tabela de Abundância Relativa</h2>
        {tabela_html}
        <hr>
        <h2 class="text-center">Gráfico de Distribuição</h2>
        <div id="grafico"></div>
    </div>
    <script>
        var grafico = {fig.to_json()};
        Plotly.newPlot('grafico', grafico.data, grafico.layout);
    </script>
</body>
</html>
'''

# Salvar o relatório como um arquivo HTML
report_path = "relatorio_interativo.html"
with open(report_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Relatório salvo como {report_path}")