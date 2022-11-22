import pandas as pd
import plotly_express as px
import numpy as np
import matplotlib.pyplot as plt
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
# import tool for lambda func (used on line 44)
import functools as ft

athlete_events = pd.read_csv("../Projekt-Databehandling/Data/athlete_events.csv")
noc_regions = pd.read_csv("../Projekt-Databehandling/Data/noc_regions.csv")

#-------------------------------------------------------------------------------------------------------------------------------------

def medal_distribution_per_sport(sport, df):
    # find all columns with x sport
    sports_olympics = df[(df["Sport"] == sport)]

    # creates 3 dataframes with all medal-types
    bronze_medal = sports_olympics[(sports_olympics["Medal"] == "Bronze")]
    silver_medal = sports_olympics[(sports_olympics["Medal"] == "Silver")]
    gold_medal = sports_olympics[(sports_olympics["Medal"] == "Gold")]

    # count the amount of each medal types for each dataframe
    bronze_medal = (
        bronze_medal.groupby(["Team"])["Medal"]
        .count()
        .reset_index(name="Bronze")
        .sort_values(["Bronze"], ascending=False)
    )

    silver_medal = (
        silver_medal.groupby(["Team"])["Medal"]
        .count()
        .reset_index(name="Silver")
        .sort_values(["Silver"], ascending=False)
    )

    gold_medal = (
        gold_medal.groupby(["Team"])["Medal"]
        .count()
        .reset_index(name="Gold")
        .sort_values(["Gold"], ascending=False)
    )

    medal_total = [gold_medal, silver_medal ,bronze_medal]
    # Added a lambda function in order to merge 3 dataframes with only needed columns
    # Source for lambda function: https://stackoverflow.com/questions/23668427/pandas-three-way-joining-multiple-dataframes-on-columns
    df_final = ft.reduce(lambda left, right: pd.merge(left, right), medal_total)
    # Creates a sum column with total medal sum, only for sorting purposes
    df_final['Sum'] = df_final.sum(axis=1)
    # sort by 'sum' column - highest to lowest
    df_final.sort_values(by='Sum', ascending=False, inplace=True)
    df_final = df_final.head(10)
    labels = {
        "value": "Medals won",
        "variable": "Medals",
        "x": "Teams",
    }

    sublabels = {
        "wide_variable_0": "Gold",
        "wide_variable_1": "Silver",
        "wide_variable_2": "Bronze",
    }

    fig = px.bar(
        x=df_final["Team"],
        y=[df_final["Gold"], df_final["Silver"], df_final["Bronze"]],
        barmode="group",  # groups the bars next to eachother instead of stacking on eachother
        labels=labels,
        title=f'Top Countries With Most Medals Won in {sport}',
        color_discrete_sequence=['#FFD700', '#8C8C8C', '#BF834E'] # gold, silver & bronze
    )
    newnames = sublabels
    # Re-used a bit of code from my Labb 1, the original source is below.
    # source: https://stackoverflow.com/questions/64371174/plotly-how-to-change-variable-label-names-for-the-legend-in-a-plotly-express-li
    fig.for_each_trace(lambda t: t.update(name=newnames[t.name]))

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )

    return fig

#--------------------------------------------------------------------------------------------------------------------------------------------

def most_medals_per_country_sports(sport, df):
    # pick out every row that has snowboarding in it
    medals_olympics = df[(df["Sport"] == sport)]

    # counts number of medals for each country in total, then is sorted in descending order
    medals_olympics = (
        medals_olympics.groupby(["Team"])["Medal"]
        .count()
        .reset_index(name="Count") # new name for medal column
        .sort_values(["Count"], ascending=False)
    )

    fig = px.bar(
        medals_olympics.head(10),
        x='Team',
        y='Count',
        title=f'Amount of Medals Per Country for {sport}'
        
    )

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
    )

    fig.update_traces(marker_color="#185ADB")

    return fig


#---------------------------------------------------------------------------------------------------------------------------------------------

def amount_of_athlets(sport, df):
    df_sport = df[(df['Sport'] == sport)]

    # To plot the amount of athletes i used this source:
    # https://www.kaggle.com/code/gpreda/plotly-tutorial-120-years-of-olympic-games/notebook
    # I cannot explictly remember what part of the page this bit of code came from, however I was inspired by one of the examples
    tmp = df_sport.groupby(['Year', 'City'])['Season'].value_counts()
    df_sport = pd.DataFrame(data={'Athlets': tmp.values}, index=tmp.index).reset_index()

    fig = px.scatter(df_sport,
            x='Year',
            y='Athlets',
            size='Year',
            title=f'Amount of Athlets for {sport} Each Olympics',
            
    )

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
    )

    fig.update_traces(marker_color="#185ADB")

    return fig
    
