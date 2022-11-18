import dash
import os
from dash.dependencies import Output, Input
import plotly_express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dash import html, dcc
from uppgift_2_grafer import most_medals_per_country_sports, amount_of_athlets
from uppgift_1_grafer import *
from hash_data import Hash_DataFrame as hd


athlete_events = pd.read_csv("../Projekt-Databehandling/Data/athlete_events.csv")
athlete_events = hd.hash_Columns(athlete_events, ["Name"])
sport_dict = {'Ski Jumping': 'Ski Jumping', 'Snowboarding': 'Snowboarding', 'Football': 'Football', 'Bobsleigh': 'Bobsleigh'}
game_dict = {"0" : 'Summer & Winter', "1" : 'Summer', "2" : 'Winter'}

# Creates the Dash app
app = dash.Dash(__name__)

# variable names:
dropdown_options_medals_athlets = [{'label': name, 'value': sport} for sport, name in sport_dict.items()]
dropdown_options_sweden_medals = [{'label': name, 'value': season} for season, name in game_dict.items()]
sub_options_dropdown = [{'label': option, 'value': option} for option in ('Medals Won', 'Amount of Athlets')]

# Set up the app layout
app.layout = html.Main([
    #--------------FIRST GRAPH(S)----------------------------------
    html.H1('Data & Graphs for Olympics'),
    html.P('Choose a Sport'),
    dcc.Dropdown(id= 'sportpicker-dropdown',
    options= dropdown_options_medals_athlets,
    value='Snowboarding'
    ),
    dcc.RadioItems(id = 'sub-options-dropdown', options= sub_options_dropdown, value= 'Medals Won'), # open-high-low-close(options)
    dcc.Graph(id = 'athlete-medal-graph'), # first graph
    #-------------SECOND GRAPH(S)----------------------------------
    html.H1('How Many Medals Sweden Has Won In The Olympics'),
    html.P('Choose a Season'),
    dcc.Dropdown(id = 'game-picker',
    options=game_dict,
    value='1'
    ),
    dcc.Graph(id = 'sweden-medal-graph') # second graph

    ]
)

# To control our element that we've created
@app.callback(
    Output('athlete-medal-graph', 'figure'),
    Input('sportpicker-dropdown', 'value'),
    Input('sub-options-dropdown', 'value'),
)

def update_first_graph(sport, graph):
    # if-statements for sub-options-
    if graph == 'Amount of Athlets':
        return amount_of_athlets(sport, athlete_events)

    elif graph == 'Medals Won':
        return most_medals_per_country_sports(sport, athlete_events)

# Controlling elements for second graph
@app.callback(
    Output('sweden-medal-graph', 'figure'),
    Input('game-picker', 'value')
)

def update_second_graph(season):
    return total_medels_os(season)

if __name__ == '__main__':
    app.run_server(debug = True)


