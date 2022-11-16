import pandas as pd
import plotly_express as px
import numpy as np
import matplotlib.pyplot as plt
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

athlete_events = pd.read_csv("../Projekt-Databehandling/Data/athlete_events.csv")
noc_regions = pd.read_csv("../Projekt-Databehandling/Data/noc_regions.csv")

ski_jumping = athlete_events[(athlete_events["Sport"] == "Ski Jumping")]

skiing_olympics = (
    ski_jumping.groupby(["Team"])["Medal"]
    .count()
    .reset_index(name="Count") # new name for medal column
    .sort_values(["Count"], ascending=False)
)

skiing_olympics.head(3)

top_countries_medals = ski_jumping[(ski_jumping["Team"] == "Austria") | (ski_jumping["Team"] == "Norway") | (ski_jumping["Team"] == "Finland")]

bronze_ski_jumping = top_countries_medals[(top_countries_medals["Medal"] == "Bronze")]
silver_ski_jumping = top_countries_medals[(top_countries_medals["Medal"] == "Silver")]
gold_ski_jumping = top_countries_medals[(top_countries_medals["Medal"] == "Gold")]

medals_per_country = ski_jumping.groupby("Team")["Medal"].value_counts(dropna=True)
bronze_ski_jumping = bronze_ski_jumping.groupby("Team")["Medal"].value_counts(
    dropna=False
)
silver_ski_jumping = silver_ski_jumping.groupby("Team")["Medal"].value_counts(
    dropna=False
)
gold_ski_jumping = gold_ski_jumping.groupby("Team")["Medal"].value_counts(dropna=False)


def plotly_bar_plot_with_labels_sublabels(
    x, y, title, labels, sublabels,
):

    fig = px.bar(
        x=x,
        y=y,
        barmode="group",  # groups the bars next to eachother instead of stacking on eachother
        labels=labels,
        title=title,
    )
    newnames = sublabels
    # To be able to change the sub titles for 'Antal doser' without changing the data source,
    # you can switch the legendgroups name with a dict and map it onto existing subtitle names.
    # I had to do this since I couldn't change it through 'labels=' like the other titles
    # source: https://stackoverflow.com/questions/64371174/plotly-how-to-change-variable-label-names-for-the-legend-in-a-plotly-express-li
    fig.for_each_trace(lambda t: t.update(name=newnames[t.name]))

    fig.show()


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

plotly_bar_plot_with_labels_sublabels(
    top_countries_medals.Team.unique(),
    [bronze_ski_jumping, silver_ski_jumping, gold_ski_jumping],
    'Top 3 Countries With Most Medals won in Ski Jumping',
    labels_skiing,
    sublabels_skiing

)


# pick out every row that has snowboarding in it
snowboarding_olympics = athlete_events[(athlete_events["Sport"] == "Snowboarding")]


# counts number of medals for each country in total, then is sorted in descending order
snowboarding_olympics = (
    snowboarding_olympics.groupby(["Team"])["Medal"]
    .count()
    .reset_index(name="Count") # new name for medal column
    .sort_values(["Count"], ascending=False)
)

fig = px.bar(
    snowboarding_olympics.head(10),
    x='Team',
    y='Count',
    title='Antal Medaljer'
    
)
fig.update_xaxes(tickangle=40)
fig.show()

football_df = athlete_events[(athlete_events['Sport'] == "Football")]

tmp = football_df.groupby(['Year', 'City'])['Season'].value_counts()
football_df = pd.DataFrame(data={'Athlets': tmp.values}, index=tmp.index).reset_index()

fig = px.scatter(football_df,
        x='Year',
        y='Athlets',
        title='Amount of Football Players For Each Olympics',
        
)

fig.show()