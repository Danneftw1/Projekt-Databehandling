import dash
import os
from dash.dependencies import Output, Input
import plotly_express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dash import html, dcc
from uppgift_2_grafer import *
from uppgift_1_grafer import *
from hash_data import Hash_DataFrame as hd
from layout import Layout
from övriga_grafer import *


athlete_events = pd.read_csv("../Projekt-Databehandling/Data/athlete_events.csv")
athlete_events = hd.hash_Columns(athlete_events, ["Name"])

# dropdown menu name variables:
sport_dict = {
    "Biathlon": "Biathlon",
    "Snowboarding": "Snowboarding",
    "Alpine Skiing": "Alpine Skiing",
    "Freestyle Skiing": "Freestyle Skiing",
    "Boxing": "Boxing",
    "Weightlifting": "Weightlifting",
}
game_dict = {"0": "Summer & Winter", "1": "Summer", "2": "Winter"}

treemap_medal_dict = {
    "Gold": "Gold",
    "Silver": "Silver",
    "Bronze": "Bronze"
}

# variable names:
dropdown_options_medals_athlets = [
    {"label": name, "value": sport} for sport, name in sport_dict.items()
]
dropdown_options_sweden_medals = [
    {"label": name, "value": season} for season, name in game_dict.items()
]
sub_options_dropdown = [
    {"label": option, "value": option}
    for option in ("Medals Won", "Amount of Athlets", "Medal Distribution")
]

sub_options_treemap = [
    {"label": option, "value": option}
    for option in ("Gold", "Silver", "Bronze")
]

# Creates the Dash app
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.LUMEN],
    meta_tags=[dict(name="viewport", content="width=device-width, initial-scale=1.0")],
)

app.layout = Layout(dropdown_options_medals_athlets, dropdown_options_sweden_medals, sub_options_dropdown, game_dict, treemap_medal_dict).layout()

# Set up the app layout
# app.layout = html.Main([
#     #--------------FIRST GRAPH(S)----------------------------------
#     html.H1('Data & Graphs for Olympics'),
#     html.P('Choose a Sport'),
#     dcc.Dropdown(id= 'sportpicker-dropdown',
#     options= dropdown_options_medals_athlets,
#     value='Snowboarding'
#     ),
#     dcc.RadioItems(id = 'sub-options-dropdown', options= sub_options_dropdown, value= 'Medals Won'), # open-high-low-close(options)
#     dcc.Graph(id = 'athlete-medal-graph'), # first graph
#     #-------------SECOND GRAPH(S)----------------------------------
#     html.H1('How Many Medals Sweden Has Won In The Olympics'),
#     html.P('Choose a Season'),
#     dcc.Dropdown(id = 'game-picker',
#     options=game_dict,
#     value='1'
#     ),
#     dcc.Graph(id = 'sweden-medal-graph') # second graph

#     ]
# )

# To control our element that we've created
@app.callback(
    Output("athlete-medal-graph", "figure"),
    Input("sportpicker-dropdown", "value"),
    Input("sub-options-dropdown", "value"),
)

# all graphs are functions from other .py-files that are just imported into main.py
# makes main.py much easier to read code-wise
def update_first_graph(sport, graph):
    # if-statements for sub-options-dropdown
    if graph == "Amount of Athlets":
        return amount_of_athlets(sport, athlete_events)

    elif graph == "Medals Won":
        return most_medals_per_country_sports(sport, athlete_events)

    elif graph == "Medal Distribution":
        return medal_distribution_per_sport(sport, athlete_events)


# Controlling elements for second graph
@app.callback(
    Output("sweden-medal-graph", "figure"),
    Input("game-picker", "value") 
)

def update_second_graph(season):
    return total_medels_os(season)

@app.callback(
    Output("treemap_graph", "figure"),
    Input("treemap_buttons", "value")
)

def update_treemap_graph(medal):
    if medal == "Gold":
        return treemap_most_x_medals_won(medal, athlete_events)
    
    elif medal == "Silver":
        return treemap_most_x_medals_won(medal, athlete_events)
    
    elif medal == "Bronze":
        return treemap_most_x_medals_won(medal, athlete_events)

if __name__ == '__main__':
    app.run_server(debug = False)



