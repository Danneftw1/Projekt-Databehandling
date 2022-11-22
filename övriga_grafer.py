import pandas as pd
import plotly_express as px

athlete_events = pd.read_csv("../Projekt-Databehandling/Data/athlete_events.csv")

# ---------------------------------------------------------------------------------------------------------------------------------------------
# From uppgift 0, made into a treemap and we can change which medal we want to plot
def treemap_most_x_medals_won(medal, df):
    athlete_medals = (
        df.groupby(["Games", "Event", "Medal", "Team"])
        .sum(numeric_only=False)
        .reset_index()
    )
    # sorts the gold medals
    gold_medals = athlete_medals[["Team", "Medal"]].loc[
        athlete_medals["Medal"] == medal
    ]
    gold_medals = (
        gold_medals.groupby("Team")
        .count()
        .sort_values("Medal", ascending=False)
        .reset_index()
    )
    fig = px.treemap(
        gold_medals.head(30),
        path=["Team"],
        values="Medal",
        color="Medal",
        hover_data=["Team"],
        title=f"Top 30 Countries With Most {medal} Medals Won",
    )
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )

    return fig


# ---------------------------------------------------------------------------------------------------------------------------------------------
# same as sports_medal function, but its a piechart and we can change the country with dropdown menus or click-menus
def sports_medals_sweden_piechart(country, df):
    # get all swe data from dataframe
    df_data_sweden = df.loc[df["Team"] == country]

    # sort out team sports
    df_data_sweden = (
        df_data_sweden.groupby(["Games", "Event", "Medal", "Team", "Year"])
        .sum(numeric_only=False)
        .reset_index()
    )

    # groupby sport and count medals
    df_sport_medal = (
        df_data_sweden[["Sport", "Medal"]]
        .groupby("Sport")
        .count()
        .reset_index()
        .sort_values(by="Medal", ascending=False)
        .head(10)
    )

    fig = px.pie(
        df_sport_medal,
        values="Medal",
        names="Sport",
        title=f"Sports With Most Amount of Medals For {country}",
        color_discrete_sequence=['#185ADB', '#0B2761', '#195BE0', '#1A60ED', '#1651C7', '#FFC947', '#614C1B', '#E0B03F', '#EDBA42', '#C79C38']
    )
    fig.update_layout(
        margin=dict(t=30, b=0, l=0, r=0),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        title_x=0.5,
        font=dict(
            size=9,
        ),
        legend=dict(orientation="h"),
    )
    return fig
