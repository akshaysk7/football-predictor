import pandas as pd
s = pd.Series([3, 3, 0, 3, 1, 3, 3, 3])
print(s)
rawform=s.rolling(5).sum()
print(rawform)
print(rawform.shift(1))