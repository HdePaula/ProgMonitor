# pip install dash

# Possiveis consultas
# https://www.youtube.com/watch?v=fKgPXUUsg1M
import main

from dash import Dash
from dash_html_components import Div, H1, H3, P
from dash_core_components import Graph

app = Dash('ProgMonitor') #esta puxando a estilizacao do arquivo .css dentro da pasta "assets"

app.layout = Div(
    children=[
        H1('ProgMonitor'),
        H3('CPU'),
        P(main.getCpuName()),
        H3('RAM'),
        Graph(
            config={'displayModeBar': False}, #tira o menu padrao do grafico
            figure={
                'data': [
                    {
                        'values': [main.getRamUsed(), main.getRamFree()],
                        'labels': ['RAM em uso', 'RAM livre'],
                        'type': 'pie'
                    },
                ],
                'layout': {
                    'title': 'Uso de RAM'
                },
            }
        ),
        H3('GPU'),
        P(main.getGpuName()),
        Graph(
            config={'displayModeBar': False},
            figure={
                'data': [
                    {'y': [main.getGpuTemp()]},
                ],
                'layout': {
                    'title': 'Tamperatura GPU'
                },
            }
        )
    ]
)

app.run_server(debug=True)