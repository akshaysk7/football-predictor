import pandas as pd 
df=pd.read_csv("E0.csv")
print(df['Date'].dtype)
df['Date'] = pd.to_datetime(df['Date'],format='%d/%m/%Y')
print(df['Date'].dtype)
df=df.sort_values('Date',ignore_index=True)


