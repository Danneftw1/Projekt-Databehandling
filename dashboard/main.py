import dash
import os
from dash.dependencies import Output, Input
import plotly_express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dash import html, dcc
from uppgift_2_grafer import most_medals_per_country_sports, amount_of_athlets

athlete_events = pd.read_csv("../Projekt-Databehandling/Data/athlete_events.csv")
sport_dict = {'Ski Jumping': 'Ski Jumping', 'Snowboarding': 'Snowboarding', 'Football': 'Football', 'Bobsleigh': 'Bobsleigh'}

# Creates the Dash app
app = dash.Dash(__name__)

# variable names:
dropdown_options = [{'label': name, 'value': sport} for sport, name in sport_dict.items()]
ohlc_options = [{'label': option, 'value': option} for option in ('Medals Won', 'Amount of Athlets')]

# Set up the app layout
app.layout = html.Main([
    html.H1('Data & Graphs for Olympics'),
    html.P('Choose a Sport'),
    dcc.Dropdown(id= 'sportpicker-dropdown',
    options= dropdown_options
    ),
    dcc.RadioItems(id = 'ohlc-radio', options= ohlc_options, value= 'Medals Won'), # open-high-low-close(options)
    dcc.Graph(id = 'athlete-graph'),
    ]
)

# To control our element that we've created
@app.callback(
    Output('athlete-graph', 'figure'),
    Input('sportpicker-dropdown', 'value'),
    Output('athlete-graph', 'figure'),
    input('ohlc-radio', 'value')
)

def update_graph(sport):
    df_sport = athlete_events[(athlete_events['Sport'] == sport)]

    tmp = df_sport.groupby(['Year', 'City'])['Season'].value_counts()
    df_sport = pd.DataFrame(data={'Athlets': tmp.values}, index=tmp.index).reset_index()

    fig = px.scatter(df_sport,
            x='Year',
            y='Athlets',
            size='Year',
            title=f'Amount of athlets for {sport} Each Olympics')

    return fig

if __name__ == '__main__':
    app.run_server(debug = True)



