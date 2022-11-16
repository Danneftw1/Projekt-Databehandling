import dash
import os
from dash.dependencies import Output, Input
import plotly_express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dash import html, dcc

athlete_events = pd.read_csv("../Projekt-Databehandling/Data/athlete_events.csv")
sport_dict = {'SJ': 'Ski Jumping', 'SB': 'Snowboard', 'FB': 'Football'}

# Creates the Dash app
app = dash.Dash(__name__)

# variable names:
dropdown_options = [{'label': name, 'value': sport} for sport, name in sport_dict.items()]
ohlc_options = [{'label': option, 'value': option} for option in ('Medals Won', 'Medal Distribution', 'Amount of Athlets')]

# Set up the app layout
app.layout = html.Main([
    html.H1('Data & Graphs for Olympics'),
    html.P('Choose a Sport'),
    dcc.Dropdown(id= 'sportpicker-dropdown',
    options= dropdown_options
    ),
    dcc.RadioItems(id = 'ohlc-radio', options= ohlc_options, value= 'Medals Won'), # open-high-low-close(options)
    dcc.Graph(id = 'snowboard-graph'),
    dcc.Graph(id = 'football-graph'),
    dcc.Graph(id = 'ski-jumping-graph')
    ]
)

# To control our element that we've created
@app.callback(
    Output('snowboard-graph', 'figure'),
    Input('sportpicker-dropdown', 'value'),
    input('ohlc-radio', 'value'),
)

def update_graph(sport, )

if __name__ == '__main__':
    app.run_server(debug = True)



