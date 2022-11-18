import pandas as pd
import plotly_express as px
import numpy as np
import matplotlib.pyplot as plt
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

# import tool for lambda func (used on line 44)
import functools as ft

athlete_events = pd.read_csv("../Projekt-Databehandling/Data/athlete_events.csv")
noc_regions = pd.read_csv("../Projekt-Databehandling/Data/noc_regions.csv")

def medal_distribution_per_sport(sport, df):

    ski_jumping = df[(df["Sport"] == sport)]

    bronze_ski_jumping = ski_jumping[(ski_jumping["Medal"] == "Bronze")]
    silver_ski_jumping = ski_jumping[(ski_jumping["Medal"] == "Silver")]
    gold_ski_jumping = ski_jumping[(ski_jumping["Medal"] == "Gold")]

    bronze_ski_jumping = (
        bronze_ski_jumping.groupby(["Team"])["Medal"]
        .count()
        .reset_index(name="Bronze") # new name for medal column
        .sort_values(["Bronze"], ascending=False)
    )

    silver_ski_jumping = (
        silver_ski_jumping.groupby(["Team"])["Medal"]
        .count()
        .reset_index(name="Silver") # new name for medal column
        .sort_values(["Silver"], ascending=False)
    )

    gold_ski_jumping = (
        gold_ski_jumping.groupby(["Team"])["Medal"]
        .count()
        .reset_index(name="Gold") # new name for medal column
        .sort_values(["Gold"], ascending=False)
    )

    medal_total = [bronze_ski_jumping, silver_ski_jumping, gold_ski_jumping]
    # Added a lambda function in order to merge 3 dataframes with only needed columns
    df_final = ft.reduce(lambda left, right: pd.merge(left, right), medal_total)
    # Creates a sum column with total medal sum, only for sorting purpose
    df_final['Sum'] = df_final.sum(axis=1)
    # sort by 'sum' column - highest to lowest
    df_final.sort_values(by='Sum', ascending=False, inplace=True)

    labels_skiing = {
        "value": "Medals won",
        "variable": "Medals",
        "x": "Teams",
    }

    sublabels_skiing = {
        "wide_variable_0": "Bronze",
        "wide_variable_1": "Silver",
        "wide_variable_2": "Gold",
    }

    fig = px.bar(
        x=df_final["Team"],
        y=[df_final["Bronze"],df_final["Silver"], df_final["Gold"]],
        barmode="group",  # groups the bars next to eachother instead of stacking on eachother
        labels=labels_skiing,
        title=f'Top Countries With Most Medals won in {sport}',
    )
    newnames = sublabels_skiing
    # To be able to change the sub titles for 'Antal doser' without changing the data source,
    # you can switch the legendgroups name with a dict and map it onto existing subtitle names.
    # I had to do this since I couldn't change it through 'labels=' like the other titles
    # source: https://stackoverflow.com/questions/64371174/plotly-how-to-change-variable-label-names-for-the-legend-in-a-plotly-express-li
    fig.for_each_trace(lambda t: t.update(name=newnames[t.name]))

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
    # fig.update_xaxes(tickangle=40)
    return fig


#---------------------------------------------------------------------------------------------------------------------------------------------

def amount_of_athlets(sport, df):
    df_sport = df[(df['Sport'] == sport)]

    tmp = df_sport.groupby(['Year', 'City'])['Season'].value_counts()
    df_sport = pd.DataFrame(data={'Athlets': tmp.values}, index=tmp.index).reset_index()

    fig = px.scatter(df_sport,
            x='Year',
            y='Athlets',
            size='Year',
            title='Amount of athlets for '+sport+' Each Olympics',
            
    )

    return fig
