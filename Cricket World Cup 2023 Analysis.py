#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sn

import plotly.express as px


# In[3]:


batsmans=pd.read_csv('batting_summary.csv')
bowlers=pd.read_csv('bowling_summary.csv')
players=pd.read_csv('world_cup_players_info.csv')
matches=pd.read_csv('match_schedule_results.csv')


# # 1. Batting dataset Analysis

# **Showing first five rows**

# In[4]:


batsmans.head()


# **Shwoing last five rows**

# In[5]:


batsmans.tail()


# **Shape of the dataset**

# In[6]:


batsmans.shape


# **Total information about the dataset**

# In[7]:


batsmans.info()


# **Checking any null values**

# In[8]:


batsmans.isnull().sum()


# **Checking any duplicated values**

# In[9]:


batsmans.duplicated().sum()


# **Extra statistical measures**

# In[10]:


batsmans.describe()


# ## Visualizations

# ### a) Most runs

# In[11]:


most_run=batsmans.groupby('Batsman_Name')['Runs'].sum().sort_values(ascending=False).reset_index().head(10)

most_run


# In[12]:


fig=px.bar(most_run,x='Batsman_Name', y='Runs', title='Most Runs',
           
labels={'Runs':'Total Runs', 'Batsman_Name':'Batsman_Name'}, color='Runs',color_continuous_scale='magma')

fig.update_layout(xaxis_title='Batsman Name', yaxis_title='Most Runs',height=600, width=800)
fig.update_layout(template='ggplot2')

fig.show()


# ### b) Most 4s

# In[13]:


four=batsmans.groupby('Batsman_Name')['4s'].sum().sort_values(ascending=False).reset_index().head(10)

four


# In[14]:


fig=px.line(four,x='Batsman_Name',y='4s',title='Most Fours',
          labels={'Batsman_Name': 'Batsman_Name','Fours':'4s'},
           line_shape="linear",
            markers=True,
            color='4s'
          )
fig.update_layout(xaxis_title='Batsman Names', yaxis_title='Fours')
fig.update_layout(template='ggplot2')
fig.update_traces(marker=dict(size=12))

fig.show()


# ### c) Most 6s

# In[15]:


sixes=batsmans.groupby('Batsman_Name')['6s'].sum().sort_values(ascending=False).reset_index().head(10)

sixes


# In[74]:


fig=px.pie(sixes,names='Batsman_Name',values='6s',title='Most Sixes',
          labels={'Batsman_Name': 'Batsman_Name','Sixes':'6s'},
           color='Batsman_Name', color_discrete_sequence=px.colors.sequential.Viridis
          )
fig.update_layout(height=600, width=800)
fig.update_layout(template='ggplot2')
fig.show()


# -----------------------------------------------------------------------------------------------------------

# # 2. Bowling dataset Analysis

# **Showing the first five rows**

# In[17]:


bowlers.head()


# **Showing last five rows**

# In[18]:


bowlers.tail()


# **Showing the shape of the datashape**

# In[19]:


bowlers.shape


# **Showing total information**

# In[20]:


bowlers.info()


# **Checking null values**

# In[21]:


bowlers.isnull().sum()


# **Checking duplicates**

# In[22]:


bowlers.duplicated().sum()


# **Showing extra statistical measures**

# In[23]:


bowlers.describe()


# ## Visualizations

# ### a) Most wickets

# In[24]:


wickets=bowlers.groupby('Bowler_Name')['Wickets'].sum().sort_values(ascending=False).reset_index().head(10)

wickets


# In[83]:


fig=px.bar(wickets, x='Bowler_Name',y='Wickets',title='Most Wickets',
           labels={'Bowler_Name':'Bowler_Name', 'Wickets':'Wickets'},
           color='Wickets', color_continuous_scale='balance'
          )
fig.update_layout(xaxis_title='Bowler Names', yaxis_title='Wickets', height=600, width=800)

fig.update_layout(template='ggplot2')

fig.show()


# ### b) Most Maidens

# In[26]:


maidens=bowlers.groupby('Bowler_Name')['Maidens'].sum().sort_values(ascending=False).reset_index().head(10)

maidens


# In[27]:


fig=px.line(maidens, x='Bowler_Name',y='Maidens',title='Most Maidens',
           labels={'Bowler_Name':'Bowler_Name', 'maidens':'Maidens'},
           line_shape="linear",
            markers=True,
            color='Maidens'
          )

fig.update_layout(xaxis_title='Bowler Names', yaxis_title='Maidens')
fig.update_traces(marker=dict(size=12))
fig.update_layout(template='ggplot2')

fig.show()


# ### c) Total Run conceded

# In[28]:


runs_bowl=bowlers.groupby('Bowler_Name')['Runs'].sum().sort_values(ascending=False).reset_index().head(10)

runs_bowl


# In[85]:


fig=px.pie(runs_bowl, names='Bowler_Name',values='Runs',title='Total Runs Conceded',
           labels={'Bowler_Name':'Bowler_Name', 'runs':'Runs'},
           color='Bowler_Name',color_discrete_sequence=px.colors.sequential.Sunsetdark
          )
fig.update_layout(height=600, width=800)
fig.update_layout(template='ggplot2')

fig.show()


# ----------------------------------------------------------------------------------------------------

# # 3. Players dataset Analysis

# **Show the first five rows**

# In[30]:


players.head()


# **the last five rows**

# In[31]:


players.tail()


# **Dataset shape**

# In[32]:


players.shape


# **total information**

# In[33]:


players.info()


# **Checking any null values**

# In[34]:


players.isnull().sum()


# **Checking duplicates**

# In[35]:


players.duplicated().sum()


# ## Visualizations

# ### a) How many players from a single team

# In[41]:


country_players=pd.DataFrame(players['team_name'].value_counts().reset_index())

country_players


# In[42]:


fig=px.line(country_players, x='index',y='team_name',title='Total Players from each contry',
           labels={'team_name':'index', 'count':'team_name'},
            line_shape="linear",
            markers=True, color='index'
        
          )
fig.update_layout(xaxis_title='Team Names', yaxis_title='Number of Players')
fig.update_traces(marker=dict(size=12))
fig.update_layout(template='ggplot2')

fig.show()


# ### b) Batting Style numbers

# In[43]:


# Assuming 'battingStyle' is the column name and 'Right-hand bat' is the value to be removed
players = players[players['battingStyle'] != 'Right-hand bat']


# In[44]:


batting_style=pd.DataFrame(players['battingStyle'].value_counts().reset_index())
batting_style


# In[47]:


fig=px.bar(batting_style, x='index',y='battingStyle',title='Batting Styles ',
           labels={'battingStyle':'index', 'count':'battingStyle'},
           color='battingStyle'
          )
fig.update_layout(xaxis_title='Batsman', yaxis_title='Number of Players')
fig.update_layout(template='ggplot2')

fig.show()


# ### c) Bowling Style numbers

# In[48]:


bowling_style=pd.DataFrame(players['bowlingStyle'].value_counts().reset_index())
bowling_style


# In[53]:


fig = px.bar(bowling_style, x='index', y='bowlingStyle', title='All Bowling Styles',
             labels={'bowlingStyle': 'index', 'count': 'bowlingStyle'},
             color='bowlingStyle', color_continuous_scale='Viridis', template='ggplot2'
            )

fig.update_layout(xaxis_title='Bowling Styles', yaxis_title='Number of Players', height=600, width=900)
fig.update_layout(template='ggplot2')

fig.show()


# ### d) Total Playing Roles

# In[54]:


playing_Role=pd.DataFrame(players['playingRole'].value_counts().reset_index())
playing_Role


# In[55]:


# To remove the blank row
players = players[players['playingRole'] != ' ']


# In[56]:


playing_Role=pd.DataFrame(players['playingRole'].value_counts().reset_index())
playing_Role


# In[92]:


fig = px.pie(playing_Role, names='index', values='playingRole', title='All Playing Styles',
             labels={'bowlingStyle': 'index', 'count': 'playingRole'},
             color='playingRole',color_discrete_sequence=px.colors.sequential.Inferno  
            )

fig.update_layout(template='ggplot2')

fig.show()


# ---------------------------------------------------------------------------------------------------

# # 4. Match Schedule Results dataset analysis

# **To show the first five rows of the dataset**

# In[59]:


matches.head()


# **last five rows**

# In[60]:


matches.tail()


# **To check the shape of the dataset**

# In[61]:


matches.shape


# **Total information**

# In[62]:


matches.info()


# **To check null values**

# In[63]:


matches.isnull().sum()


# **To check duplicates**

# In[65]:


matches.duplicated().sum()


# ## Visualizations

# ### a) Total number of winning Teams

# In[66]:


total_winning_teams=pd.DataFrame(matches['Winner'].value_counts().reset_index())

total_winning_teams


# In[68]:


fig = px.pie(total_winning_teams, names='index', values='Winner', title='Total number of Match winners',
             labels={'Winner': 'index', 'count': 'Winner'},
             color='index'
            )

fig.update_layout( height=600, width=800)
fig.update_layout(template='ggplot2')

fig.show()


# ### b) Total match Venues

# In[93]:


total_venue=pd.DataFrame(matches['Venue'].value_counts().reset_index())

total_venue


# In[102]:


fig = px.bar(total_venue, x='index', y='Venue', title='Number of Match venues',
             labels={'Venue': 'index', 'count': 'index'},
             color='Venue', color_continuous_scale='greens'
            )

fig.update_layout(xaxis_title='Venues', yaxis_title='Total matches', height=600, width=800)
fig.update_layout(template='ggplot2')

fig.show()


# -----------------------------------------------------------------------------------------------------

# In[ ]:




