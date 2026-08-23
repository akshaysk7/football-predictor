import pandas as pd 
df=pd.read_csv("E0.csv")
print(df.head())
print(df['MaxCAHA'].mean())
print(df.shape)
print(df.columns.tolist())
print(df[['B365H', 'B365D', 'B365A']].head())