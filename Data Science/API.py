import pandas as pd
import matplotlib.pyplot as plt

"""
API stands for Application Program Interfaces
API's allow for two pieces of software to communicate. THe Pandas library is a good example of
an API. We use it to process data when we create a dataframe OBJECT. The input is the dictionary.

REST API's are a type of API that allow one to communicate through the internet.
Representational State Transfer API's  

REST API's send request via HTTP (Hyper Text Transfer Protocol) message, which contains a JSON
file
"""
# Pandas as an API

def one_dict(list_dict): # To be used later
    keys = list_dict[0].keys()
    out_dict = {key:[] for key in keys}
    for dict_ in list_dict:
        for key, value in dict_.items():
            out_dict[key].append(value)
    return out_dict

dict_ = {'a':[11,21,31],'b':[12,22,32],'c':[13,23,33]}

df = pd.DataFrame(dict_)
print(type(df),'\n')
"""
When calling methods through the dataframe object (In this case it is called 'df'), the API 
performs certain actions and returns the requested data.

EXample:
df.head() will return the first five rows of the data frame
df.mean() telles the API to calculate the mean and return the value 
"""

from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder 


nba_teams = teams.get_teams() # This will return a list of dictionaries. One dictonary per team.

print(nba_teams[0:3],'\n')

dict_nba = one_dict(nba_teams) # Combine the list of dictionaries into one dictionary
df_teams = pd.DataFrame(dict_nba)

df_warriors = df_teams[df_teams['nickname']=="Warriors"]
print(df_warriors,'\n')

id_warriors = df_warriors[['id']].values[0][0] 

game_finder = leaguegamefinder.LeagueGameFinder(team_id_nullable=id_warriors)
game_finder.get_json() # We cam use this to return the JSON file created by the gamefinder object

games = game_finder.get_data_frames()[0] # This will return a data frame containing infromation about all the games involving the Golden State Warriors

home = games[games['MATCHUP']=='GSW vs. TOR'] # The 'vs.' indicates it was a home game
away = games[games['MATCHUP']=='GSW @ TOR'] # The '@' indicates it was an away game

fig, ax = plt.subplots()

away.plot(x='GAME_DATE',y='PLUS_MINUS', ax=ax)
home.plot(x='GAME_DATE',y='PLUS_MINUS', ax=ax)
ax.legend(["away", "home"])
ax.invert_xaxis()
print(plt.show())
