import pandas as pd
import plotly_express as px

athlete_events = pd.read_csv("../Projekt-Databehandling/Data/athlete_events.csv")

#---------------------------------------------------------------------------------------------------------------------------------------------
# From uppgift 0, made into a treemap and we can change which medal we want to plot
def treemap_most_x_medals_won(medal, df):
  gold_athlete = df[(df['Medal'] == medal)].dropna()
  #gold_athlete = gold_athlete[['Team', 'Medal']].sort_values(by=['Team'])
  gold_athlete = gold_athlete.groupby(['Team'])['Medal'].count().reset_index(
    name='Count').sort_values(['Count'], ascending=False)

  fig = px.treemap(gold_athlete.head(30), path=['Team'], values='Count',
                    color='Count', hover_data=['Team'], title=f'Top 30 Countries With Most {medal} Medals Won')
  return fig

#---------------------------------------------------------------------------------------------------------------------------------------------
# same as sports_medal function, but its a piechart and we can change the country with dropdown menus or click-menus
def sports_medals_sweden_piechart(country, df):
    # get all swe data from dataframe
    df_data_sweden = df.loc[df["Team"] == country]

    # sort out team sports
    df_data_sweden = df_data_sweden.groupby(["Games", "Event", "Medal", "Team", "Year"]).sum(numeric_only= False).reset_index()

    # groupby sport and count medals 
    df_sport_medal = df_data_sweden[["Sport", "Medal"]].groupby("Sport").count().reset_index().sort_values(by= "Medal", ascending= False).head(10)

    fig = px.pie(df_sport_medal.head(20), values='Medal', names='Sport', title=f'Olympic Sports With Most Amount of Medals Won For {country}')
    return fig