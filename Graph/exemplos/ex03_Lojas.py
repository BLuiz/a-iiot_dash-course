from dash import Dash, Input, Output, html, dcc
import plotly.express as px
import pandas as pd

'# Um dashboard em python normalmente é separado em layout, que são os elementos do site como os gráficos'
'# E também há os callbacks, que são os elementos do site que manipulam o site e os gráficos, como os botões '

# Inicializando o App (Tornar disnível para exibição no navegador com o Flask)
app = Dash(__name__)

# Dados de um arquivo
df = pd.read_excel('Vendas.xlsx')
fig = px.bar(df, x="Produto", y="Valor Final", color="ID Loja", barmode="group")

opcoes = list(df['ID Loja'].unique())
opcoes.append('Todas as Lojas')


app.layout = html.Div(children=[
    html.H1(children='Faturamento de Lojas'),

    html.H3(children='Gráfico qualitativo de todos os Produtos separados por Loja'),

    html.Div(children='''
        Obs: Esse gráfico mostra a quantidade de produtos vendidos, não o faturamento.
    '''),

    # Div de id='texto' com objetivo de receber um valor dos callbacks
    html.Div(id="texto"),

    dcc.Dropdown(opcoes, value='Todas as Lojas', id='lista_lojas', clearable=False),

    dcc.Graph(
        id='graph_qtd_vendas',
        figure=fig
    )
])


# Função chamada para manipulação do site, contém o Decorator(@) e a definição da função
# Decorators também servem para direcionar o usuário à uma página especifica
# O valor captado no parametro value do Input de 'lista_lojas' ocasiona a mudança em um id correspondente a 'texto'
# @app.route('/homepage')
@app.callback(
    Output('graph_qtd_vendas', 'figure'),
    Input('lista_lojas', 'value')
)
def update_output(value):
    if value == 'Todas as Lojas':
        fig = px.bar(df, x="Produto", y="Valor Final", color="ID Loja", barmode="group")
    else:
        tabela_loja = df.loc[df['ID Loja']==value, :]
        fig = px.bar(tabela_loja, x="Produto", y="Valor Final", color="ID Loja", barmode="group")
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
