from dash import Dash, dcc, html, Input, Output
from plotly import figure_factory as ff, express as px, graph_objs as go
import pandas as pd
import time


def get_page():
    page = html.Div(children=[
        # Cabeçalho da página
        html.Header(id='header', children=[
            html.H1(children='Relatório de Falhas do Sistema'),
            html.Div(children='Aplicação para demonstração de mudança de estado de acordo com hora.'),
        ]),

        # Seção de exposição de gráficos
        html.Section(id='charts', children=[
            dcc.Graph(id='timeline_graph', figure=timeline_graph()),
            dcc.Graph(id='gantt_graph', figure=gantt_graph()),
        ])
    ])

    return page


def timeline_graph():
    """# Link da Documentação da função"""
    # https://plotly.com/python-api-reference/generated/plotly.express.timeline.html#plotly.express.timeline

    df = [
        dict(Etapa="Asp", Start='2017-01-05', Finish='2017-03-05', Status='Ativo', User='Ope x', Lenght='0000-02-00'),
        dict(Etapa="Asp", Start='2017-03-05', Finish='2017-04-05', Status='Inativo', User='Ope x', Lenght='0000-01-00'),
        dict(Etapa="Asp", Start='2017-04-05', Finish='2017-09-05', Status='Ativo', User='Ope z', Lenght='0000-05-00'),
        dict(Etapa="Asp", Start='2017-09-05', Finish='2017-10-05', Status='Falha', User='Ope x', Lenght='0000-01-00'),
        dict(Etapa="Asp", Start='2017-10-05', Finish='2017-11-05', Status='Inativo', User='Ope y', Lenght='0000-01-00'),
        dict(Etapa="Asp", Start='2017-11-05', Finish='2018-01-05', Status='Falha', User='Ope z', Lenght='0000-02-00'),
        dict(Etapa="Asp", Start='2018-01-05', Finish='2018-06-05', Status='Ativo', User='Ope z', Lenght='0000-05-00'),
        dict(Etapa="Asp", Start='2018-06-05', Finish='2018-09-05', Status='Falha', User='Ope y', Lenght='0000-03-00'),
        dict(Etapa="Asp", Start='2018-09-05', Finish='2018-11-05', Status='Ativo', User='Ope z', Lenght='0000-02-00'),
    ]

    # df['Duração'] = df['Finish'] - df['Start']

    colors = {  # Atribuição de Cores para cada estado
        'Inativo': 'gray',
        'Ativo': 'darkgreen',
        'Falha': 'red',
    }

    pattern = {
        'Inativo': '-',
        'Ativo': 'V',
        'Falha': 'F',
    }

    template = [
        'ggplot2', 'seaborn', 'simple_white', 'plotly', 'plotly_white',
        'plotly_dark', 'presentation', 'xgridoff', 'ygridoff', 'gridon'
    ]

    fig = px.timeline(
        # Parâmetros de Dados
        data_frame=df,                      # DataBase
        x_start='Start',                    # Coluna de dados para início de uma marca
        x_end='Finish',                     # Coluna de dados para final de uma marca
        y='Etapa',                          # Atribui eixo y, agrupada marcas de mesmo parâmetro
        color='Status',                     # Atribui cor a cada marca
        pattern_shape=None,                 # Atribui padrões de desenhos em cada marca
        # SubGráficos
        facet_row=None,                     # Constrói subgráficos de acordo com uma categoria organizados na horizontal
        facet_col=None,                     # Constrói subgráficos de acordo com uma categoria organizados na vertical
        facet_col_wrap=0,                   # Agrupa os subgráficos entre o limite de espaço definido
        facet_row_spacing=None,             # Espaço horizontal entre os subgráficos (0.0 - 1.0)
        facet_col_spacing=None,             # Espaço vertical entre os subgráficos (0.0 - 1.0)
        # Configurações de Legenda
        hover_name='Status',                # Mostrar nomes do parâmetro ao passar o mouse sobre uma marca
        hover_data=None,                    # Mostrar algum dado extra ao passar o mouse sobre uma marca
        custom_data=None,                   # Dados extra de utilização dos widgets ou callbacks
        text='Lenght',                      # Texto que aparece como label (rótulo) de cada marca
        category_orders=None,               # Forçar alguma ordenação dos dados
        labels=None,                        # Definir legendas de Eixos
        # Animação
        animation_frame=None,               # Animação para demonstrar decorrer do gráfico
        animation_group=None,               # Define gropos na animação, agrupa dados de mesmo parâmetro
        # Estilo
        color_discrete_sequence=None,       # Redefine as cores default de masrcas de acordo com os Status
        color_discrete_map=colors,          # Redefine as cores de marcas específicas de acordo com os Status
        pattern_shape_sequence=None,        # Redefine o padrão de desenho default de masrcas de acordo com os Status
        pattern_shape_map=None,             # Redefine o padrão de desenho de marcas específicas de acordo com os Status
        color_continuous_scale=None,        # Define escala de acordo com cores quando há dados numéricos
        range_color=None,                   # Redefine escala de cores quando há dados numéricos
        color_continuous_midpoint=None,     # Define a metade da escala de cores quando há dados numéricos
        opacity=None,                       # Opacidade do gráfico
        # Tamanhos e Escala
        range_x=None,                       # Reescreve auto-escalonamento do eixo x
        range_y=None,                       # Reescreve auto-escalonamento do eixo y
        title=None,                         # Título do gráfico
        template=template[5],               # Define um template para o gráfico
        width=None,                         # Largura do gráfico
        height=None,                        # Altura do gráfico
    )

    return fig


def gantt_graph():
    """# Link da Documentação da função"""
    # https://plotly.com/python/gantt/

    cores = {       # Atribuição de Cores para cada estado
        'Inativo': '#70798C',  # State gray
        'Ativo': '#85CB33',  # Yellow green
        'Falha': '#8D0C0C',  # Dark red
    }

    df = [
        dict(Task="Aspersão", Start='2017-01-05', Finish='2017-03-05', Resource='Ativo'),
        dict(Task="Aspersão", Start='2017-03-05', Finish='2017-04-05', Resource='Inativo'),
        dict(Task="Aspersão", Start='2017-04-05', Finish='2017-09-05', Resource='Ativo'),
        dict(Task="Aspersão", Start='2017-09-05', Finish='2017-10-05', Resource='Falha'),
        dict(Task="Aspersão", Start='2017-10-05', Finish='2017-11-05', Resource='Inativo'),
        dict(Task="Aspersão", Start='2017-11-05', Finish='2018-01-05', Resource='Falha'),
        dict(Task="Aspersão", Start='2018-01-05', Finish='2018-06-05', Resource='Ativo'),
        dict(Task="Aspersão", Start='2018-06-05', Finish='2018-09-05', Resource='Falha'),
        dict(Task="Aspersão", Start='2018-09-05', Finish='2018-11-05', Resource='Ativo'),
    ]

    fig = ff.create_gantt(
        df,
        colors=cores,                   # Atribui cor a cada um dos estados
        index_col='Resource',           # Define o estado de cada coluna
        show_colorbar=True,             # Mostrar legenda de cores
        reverse_colors=False,           # Inverter sequência de cores (listas)
        title='Relatório de Falhas',    # Título do gráfico
        bar_width=0.5,                  # Tamanho das barras
        showgrid_x=False,               # Mostrar linhas do eixo x
        showgrid_y=False,               # Mostrar linhas do eixo y
        height=300,                     # Altura do gráfico
        width=800,                      # Largura do gráfico
        tasks=None,                     # ?
        task_names=None,                # ?
        data=None,                      # ?
        group_tasks=True,               # Agrupar linhas de mesma fonte
        show_hover_fill=True,           # Habilita caixa de texto sobre o mouse
    )

    return fig



