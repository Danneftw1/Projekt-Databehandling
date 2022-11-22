import pandas as pd
import plotly_express as px
from hash_data import Hash_DataFrame as hd

# file path
file_path = "Data/athlete_events.csv"

# load the data as a dataFrame
df_data = pd.read_csv(file_path)

# encrypt the athletes names. TODO check why error message is not working.
df_data = hd.hash_Columns(df_data, ["Name"])

#---------------------------------------------------------------------------------------------------------------------------------------------

def sport_medals():

    # de sporter landet fått flest medaljer i

    # get all swe data from dataframe
    df_data_sweden = df_data.loc[df_data["Team"] == "Sweden"]

    # sort out team sports
    temp = (
        df_data_sweden.groupby(["Games", "Event", "Medal", "Team", "Year"])
        .sum(numeric_only=False)
        .reset_index()
    )

    # groupby sport and count medals
    df_sport_medal = (
        temp[["Sport", "Medal"]]
        .groupby("Sport")
        .count()
        .reset_index()
        .sort_values(by="Medal", ascending=False)
        .head(10)
    )

    # NOTE i lag sport är det en medalj per lag medlem.
    fig = px.bar(df_sport_medal, x="Sport", y="Medal")

    fig.update_traces(marker_color="#185ADB")

    return fig

#---------------------------------------------------------------------------------------------------------------------------------------------

def total_medels_os(value): 
    # antal medaljer per OS

    # get all swe data from dataframe
    df_data_sweden = df_data.loc[df_data["Team"] == "Sweden"]

    # Create a new dataframe with year and medals
    df_os_medals = df_data_sweden.groupby("Year")["Medal"].count().reset_index()

    # rename Medal to toalal medals
    df_os_medals.rename(columns={"Medal": "total Medals"}, inplace=True)

    # seasons and column names
    seasons = ["Summer", "Winter"]
    column_names = ["Summer medals", "Winter medals"]

    # counts medals for winter and summer os and add them to new columns "Summer medals" and "Winter medals"
    for i, season in enumerate(seasons):

        df_temp = (
            df_data_sweden[["Year", "Medal"]]
            .loc[df_data_sweden["Season"] == season]
            .groupby("Year")
            .count()
            .reset_index()
        )
        df_temp.rename(columns={"Medal": column_names[i]}, inplace=True)
        df_os_medals = pd.merge(df_os_medals, df_temp, how="left", on="Year")

    # Titels and column names
    titels = [
        "Total Number of Medals Per OS",
        "Total Number of Medals Per Summer OS",
        "Total Number of Medals Per Winter OS",
    ]
    columns = [["Summer medals", "Winter medals"], "Summer medals", "Winter medals"]

    fig = px.bar(
        df_os_medals,
        x="Year",
        y=columns[int(value)],
        barmode="group",
        title=titels[int(value)],
        color_discrete_sequence=['#FFC947', '#185ADB']
    )

    fig.update_layout(
        yaxis_title="number of medals",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
    )

    return fig

#---------------------------------------------------------------------------------------------------------------------------------------------

def age_distribution():

    # histogram över åldrar
    # gets swedish participants
    df_swedish_participants = df_data.loc[df_data["Team"] == "Sweden"]

    # group the data where name is the same and creates a new dataframe with age and name.
    df_age = (
        df_swedish_participants[["Age", "Name"]]
        .groupby(["Name", "Age"])
        .count()
        .reset_index()
    )

    # Plots the histogram
    fig = px.histogram(df_age, x="Age", title="OS Age Distribution in Swedish Athlets")
    fig.update_layout(
        yaxis_title="Number",
        margin=dict(t=30, b=0, l=0, r=0),
        title_x=0.5,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(
            size=10,
        ),
    )

    fig.update_traces(marker_color="#185ADB")

    return fig

#---------------------------------------------------------------------------------------------------------------------------------------------

def sex_distribution():

    # Kön fördelning i os för sverige

    # gets swedish participants
    df_swedish_participants = df_data.loc[df_data["Team"] == "Sweden"]

    # group by sex and name
    df_swe_sex = df_swedish_participants.groupby(["Sex", "Name"]).count().reset_index()

    # group by sex.
    df_swe_sex = df_swe_sex.groupby("Sex")["Sex"].count()

    # Plots graph
    fig = px.pie(
        df_swe_sex,
        names=df_swe_sex.index,
        values="Sex",
        title="Total Gender Distribution in Swedish Athlets",
        color=df_swe_sex.index,
        color_discrete_map={
            "M": "#185ADB",
            "F": "#FFC947",
        },
    )
    fig.update_layout(
        margin=dict(t=30, b=0, l=0, r=0),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        title_x=0.5,
        font=dict(
            size=10,
        ),
        legend=dict(orientation="h"),
    )

    return fig
