import pandas as pd 
df=pd.read_csv("E0.csv")
arsenal=df[(df['HomeTeam']=='Arsenal') | (df['AwayTeam']=='Arsenal')]
print(arsenal.shape)
home_view = df.copy()
home_view['team'] = df['HomeTeam']
home_view['opponent'] = df['AwayTeam']
home_view['venue'] = 'Home'
print(home_view[['team', 'opponent', 'venue', 'HomeTeam', 'AwayTeam']].head())
away_view = df.copy()
away_view['team'] = df['AwayTeam']
away_view['opponent'] = df['HomeTeam']
away_view['venue'] = 'away'
print(away_view[['team', 'opponent', 'venue', 'AwayTeam', 'HomeTeam']].head())
team_matches=pd.concat([home_view,away_view],ignore_index=True)
print(team_matches.shape)