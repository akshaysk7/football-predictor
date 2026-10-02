import pandas as pd 
df=pd.read_csv("E0.csv")
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')
df = df.sort_values('Date', ignore_index=True)
home_view = df.copy()
home_view['team'] = df['HomeTeam']
home_view['opponent'] = df['AwayTeam']
home_view['venue'] = 'Home'
print(home_view[['team', 'opponent', 'venue', 'HomeTeam', 'AwayTeam']].head())
away_view = df.copy()
away_view['team'] = df['AwayTeam']
away_view['opponent'] = df['HomeTeam']
away_view['venue'] = 'Away'
print(away_view[['team', 'opponent', 'venue', 'AwayTeam', 'HomeTeam']].head())
team_matches=pd.concat([home_view,away_view],ignore_index=True)
print(team_matches.shape)
team_matches.groupby('team')  
def points(venue,FTR):
    if venue=='Home'and FTR=='H':
        return(3)
    elif venue=='Away'and FTR=='A':
        return(3)
    elif FTR=='D':
        return(1)
    else:
        return(0)
print(points('Home', 'H'))   # expect 3
print(points('Away', 'A'))   # expect 3
print(points('Away', 'H'))   # expect 0
print(points('Home', 'D'))   # expect 1
team_matches['points']= team_matches.apply(lambda row: points(row['venue'],row['FTR']), axis=1)
f= lambda row: row['team']+ ' vs ' + row['opponent']
print(f(team_matches.iloc[388])) 
print(team_matches['points'].value_counts())
