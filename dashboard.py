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

        #DADOS CPU
        Div(
            children=[
                H3('CPU'),
                P(main.getCpuName()),
                P(main.getCpuFreq()),
                P(main.getCpuCount()),
                Graph(
                    config={'displayModeBar': False}, #tira o menu padrao do grafico
                    figure={
                        'data': [
                            {
                                'values': [main.getCpuUsedPercent(), (100 - main.getCpuUsedPercent())],
                                'labels': ['CPU em uso', 'CPU'],
                                'type': 'pie'
                            },
                        ],
                        'layout': {
                            'title': 'Uso de CPU'
                        },
                    }
                ),
            ]
        ),

        #DADOS RAM
        Div(
            children=[
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
            ]
        ),
        
        #DADOS GPU
        Div(
            children=[
                H3('GPU'),
                P(main.getGpuName()),

                Graph(
                    config={'displayModeBar': False}, #tira o menu padrao do grafico
                    figure={
                        'data': [
                            {
                                'values': [main.getGpuUsedPercent(), (100.0 - float(main.getGpuUsedPercent()))],
                                'labels': ['GPU em uso', 'GPU livre'],
                                'type': 'pie'
                            },
                        ],
                            'layout': {
                            'title': 'Uso da GPU'
                        },
                    }
                ),

                #GPU MEMORIA
                Graph(
                    config={'displayModeBar': False}, #tira o menu padrao do grafico
                    figure={
                        'data': [
                            {
                                'values': [main.getGpuMemoryUsed(), (float(main.getGpuMemoryTotal()) - float(main.getGpuMemoryUsed()))],
                                'labels': ['Memoria GPU em uso', 'Memoria GPU livre'],
                                'type': 'pie'
                            },
                        ],
                            'layout': {
                            'title': 'Uso de Memoria GPU'
                        },
                    }
                ),

                #GPU TEMPERATURA
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
                ),
            ]
        )
    ]
)

app.run_server(debug=True)