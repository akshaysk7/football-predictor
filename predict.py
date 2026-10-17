import pandas as pd 
df=pd.read_csv("E0.csv")
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')
df = df.sort_values('Date', ignore_index=True)
df['match_id']=df.index
home_view = df.copy()
home_view['team'] = df['HomeTeam']
home_view['opponent'] = df['AwayTeam']
home_view['venue'] = 'Home'
#print(home_view[['team', 'opponent', 'venue', 'HomeTeam', 'AwayTeam']].head())
away_view = df.copy()
away_view['team'] = df['AwayTeam']
away_view['opponent'] = df['HomeTeam']
away_view['venue'] = 'Away'
#print(away_view[['team', 'opponent', 'venue', 'AwayTeam', 'HomeTeam']].head())
team_matches=pd.concat([home_view,away_view],ignore_index=True)
#print(team_matches.shape)
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
#print(points('Home', 'H'))   # expect 3
#print(points('Away', 'A'))   # expect 3
#print(points('Away', 'H'))   # expect 0
#print(points('Home', 'D'))   # expect 1
team_matches['points']= team_matches.apply(lambda row: points(row['venue'],row['FTR']), axis=1)
#print(team_matches['points'].value_counts())
team_matches=team_matches.sort_values('Date',ignore_index=True)
team_matches['form5']=team_matches.groupby('team')['points'].transform(lambda s: s.rolling(5).sum().shift(1))
print(team_matches.groupby('team').get_group('Arsenal')[['Date','opponent','venue','points','form5']].head(8))
print(team_matches['form5'].isna().sum())
print(team_matches[team_matches['match_id'] == 58][['match_id', 'Date', 'team', 'opponent', 'venue', 'form5']])
home_form=team_matches[team_matches['venue']=='Home'][['match_id','form5']].rename(columns={'form5':'home_form5'})
print(home_form.head())
away_form=team_matches[team_matches['venue']=='Away'][['match_id','form5']].rename(columns={'form5':'away_form5'})
print(away_form.head())
print(home_form[home_form['match_id']==58])
matches=df.merge(home_form, on='match_id').merge(away_form, on='match_id')
print(matches[matches['match_id'] == 58][['HomeTeam', 'AwayTeam', 'home_form5', 'away_form5', 'FTR']])

