from dash import Dash
from sites.pagina import get_page
'''from plotly import figure_factory as ff, express as px, graph_objs as go
import pandas as pd
import time'''

app = Dash(__name__)

app.layout = get_page()

# Executando o servidor
if __name__ == '__main__':
    app.run_server(debug=True)

