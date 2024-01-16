import streamlit as st
import pandas as pd
import plotly.express as px

# Load datasets

batsmans = pd.read_csv('Datasets/batting_summary.csv')
bowlers = pd.read_csv('Datasets/bowling_summary.csv')
player = pd.read_csv('Datasets/world_cup_players_info.csv')
matches = pd.read_csv('Datasets/match_schedule_results.csv')

# Function to display batting analysis
def batting_analysis():
    st.header("Batting Dataset Analysis")

    st.subheader("Showing first five rows")
    st.write(batsmans.head())

    st.subheader("Showing last five rows")
    st.write(batsmans.tail())

    st.subheader("Shape of the dataset")
    st.write(batsmans.shape)

    st.subheader("Total information about the dataset")
    st.write(batsmans.info())

    st.subheader("Checking any null values")
    st.write(batsmans.isnull().sum())

    st.subheader("Checking any duplicated values")
    st.write(batsmans.duplicated().sum())

    st.subheader("Extra statistical measures")
    st.write(batsmans.describe())

    st.header("Visualizations")

    st.subheader("a) Most runs")
    most_run = batsmans.groupby('Batsman_Name')['Runs'].sum().sort_values(ascending=False).reset_index().head(10)
    fig = px.bar(most_run, x='Batsman_Name', y='Runs', title='Most Runs', labels={'Runs': 'Total Runs', 'Batsman_Name': 'Batsman_Name'}, color='Runs', color_continuous_scale='magma')
    st.plotly_chart(fig)

    st.subheader("b) Most 4s")
    four = batsmans.groupby('Batsman_Name')['4s'].sum().sort_values(ascending=False).reset_index().head(10)
    fig = px.line(four, x='Batsman_Name', y='4s', title='Most Fours', labels={'Batsman_Name': 'Batsman_Name', 'Fours': '4s'}, line_shape="linear", markers=True, color='4s')
    st.plotly_chart(fig)

    st.subheader("c) Most 6s")
    sixes = batsmans.groupby('Batsman_Name')['6s'].sum().sort_values(ascending=False).reset_index().head(10)
    fig = px.pie(sixes, names='Batsman_Name', values='6s', title='Most Sixes', labels={'Batsman_Name': 'Batsman_Name', 'Sixes': '6s'}, color='Batsman_Name', color_discrete_sequence=px.colors.sequential.Viridis)
    st.plotly_chart(fig)

# Function to display bowling analysis
def bowling_analysis():
    st.header("Bowling Dataset Analysis")

    st.subheader("Showing first five rows")
    st.write(bowlers.head())

    st.subheader("Showing last five rows")
    st.write(bowlers.tail())

    st.subheader("Shape of the dataset")
    st.write(bowlers.shape)

    st.subheader("Total information about the dataset")
    st.write(bowlers.info())

    st.subheader("Checking any null values")
    st.write(bowlers.isnull().sum())

    st.subheader("Checking any duplicated values")
    st.write(bowlers.duplicated().sum())

    st.subheader("Extra statistical measures")
    st.write(bowlers.describe())

    st.header("Visualizations")

    st.subheader("a) Most wickets")
    wickets = bowlers.groupby('Bowler_Name')['Wickets'].sum().sort_values(ascending=False).reset_index().head(10)
    fig = px.bar(wickets, x='Bowler_Name', y='Wickets', title='Most Wickets', labels={'Bowler_Name': 'Bowler_Name', 'Wickets': 'Wickets'}, color='Wickets', color_continuous_scale='balance')
    st.plotly_chart(fig)

    st.subheader("b) Most Maidens")
    maidens = bowlers.groupby('Bowler_Name')['Maidens'].sum().sort_values(ascending=False).reset_index().head(10)
    fig = px.line(maidens, x='Bowler_Name', y='Maidens', title='Most Maidens', labels={'Bowler_Name': 'Bowler_Name', 'Maidens': 'Maidens'}, line_shape="linear", markers=True, color='Maidens')
    st.plotly_chart(fig)

    st.subheader("c) Total Run conceded")
    runs_bowl = bowlers.groupby('Bowler_Name')['Runs'].sum().sort_values(ascending=False).reset_index().head(10)
    fig = px.pie(runs_bowl, names='Bowler_Name', values='Runs', title='Total Runs Conceded', labels={'Bowler_Name': 'Bowler_Name', 'Runs': 'Runs'}, color='Bowler_Name', color_discrete_sequence=px.colors.sequential.Sunsetdark)
    st.plotly_chart(fig)

# Function to display player analysis
def player_analysis():
    st.header("Players Dataset Analysis")

    st.subheader("Show the first five rows")
    st.write(player.head())

    st.subheader("The last five rows")
    st.write(player.tail())

    st.subheader("Dataset shape")
    st.write(player.shape)

    st.subheader("Total information")
    st.write(player.info())

    st.subheader("Checking any null values")
    st.write(player.isnull().sum())

    st.subheader("Checking duplicates")
    st.write(player.duplicated().sum())

    st.header("Visualizations")

    st.subheader("a) How many players from a single team")
    country_players = pd.DataFrame(player['team_name'].value_counts().reset_index())
    fig=px.line(country_players, x='team_name',y='count',title='Total Players from each contry',
           labels={'team_name':'team_name', 'count':'count'},
            line_shape="linear",
            markers=True, color='team_name'
        
          )
    fig.update_layout(xaxis_title='Team Names', yaxis_title='Number of Players')
    fig.update_traces(marker=dict(size=12))
    fig.update_layout(template='ggplot2')
    st.plotly_chart(fig)

    st.subheader("b) Batting Style numbers")
    players = player[player['battingStyle'] != 'Right-hand bat']
    batting_style = pd.DataFrame(players['battingStyle'].value_counts().reset_index())
    fig=px.bar(batting_style, x='battingStyle',y='count',title='Batting Styles ',
           labels={'battingStyle':'battingStyle', 'count':'count'},
           color='count'
          )
    fig.update_layout(xaxis_title='Batsman', yaxis_title='Number of Players')
    fig.update_layout(template='ggplot2')
    st.plotly_chart(fig)

    st.subheader("c) Bowling Style numbers")
    bowling_style = pd.DataFrame(player['bowlingStyle'].value_counts().reset_index())
    fig = px.bar(bowling_style, x='bowlingStyle', y='count', title='All Bowling Styles',
             labels={'bowlingStyle': 'Bowling Style', 'count': 'Count'},
             color='count', color_continuous_scale='magma', template='ggplot2'
            )

    fig.update_layout(xaxis_title='Bowling Styles', yaxis_title='Number of Players', height=600, width=800)
    fig.update_layout(template='ggplot2')
    st.plotly_chart(fig)

    st.subheader("d) Total Playing Roles")
    playing_Role = pd.DataFrame(players['playingRole'].value_counts().reset_index())
    players = player[player['playingRole'] != ' ']
    playing_Role = pd.DataFrame(players['playingRole'].value_counts().reset_index())
    fig = px.pie(playing_Role, names='playingRole', values='count', title='All Playing Styles',
             labels={'bowlingStyle': 'playingRole', 'count': 'Count'},
             color='count'
            )

    fig.update_layout(height=600, width=800)
    fig.update_layout(template='ggplot2')
    st.plotly_chart(fig)

# Function to display match schedule results analysis
def match_schedule_results_analysis():
    st.header("Match Schedule Results Dataset Analysis")

    st.subheader("To show the first five rows of the dataset")
    st.write(matches.head())

    st.subheader("last five rows")
    st.write(matches.tail())

    st.subheader("To check the shape of the dataset")
    st.write(matches.shape)

    st.subheader("Total information")
    st.write(matches.info())

    st.subheader("To check null values")
    st.write(matches.isnull().sum())

    st.subheader("To check duplicates")
    st.write(matches.duplicated().sum())

    st.header("Visualizations")

    st.subheader("a) Total number of winning Teams")
    total_winning_teams = pd.DataFrame(matches['Winner'].value_counts().reset_index())
    fig = px.pie(total_winning_teams, names='Winner', values='count', title='Total number of Match winners',
             labels={'Winner': 'Winner', 'count': 'Count'},
             color='Winner'
            )

    fig.update_layout( height=600, width=800)
    fig.update_layout(template='ggplot2')
    st.plotly_chart(fig)

    st.subheader("b) Total match Venues")
    total_venue = pd.DataFrame(matches['Venue'].value_counts().reset_index())
    fig = px.bar(total_venue, x='Venue', y='count', title='Number of Match venues',
             labels={'Venue': 'Venue', 'count': 'Count'},
             color='count', color_continuous_scale='bluered', template='seaborn'
            )

    fig.update_layout(xaxis_title='Venues', yaxis_title='Total matches', height=600, width=800)
    fig.update_layout(template='ggplot2')
    st.plotly_chart(fig)

# Main Streamlit App
st.title("Cricket World Cup 2023 Analysis 🏏🏆")

selected_analysis = st.sidebar.selectbox("Select Analysis", ["Batting", "Bowling", "Players", "Match Schedule Results"])

if selected_analysis == "Batting":
    batting_analysis()
elif selected_analysis == "Bowling":
    bowling_analysis()
elif selected_analysis == "Players":
    player_analysis()
elif selected_analysis == "Match Schedule Results":
    match_schedule_results_analysis()
