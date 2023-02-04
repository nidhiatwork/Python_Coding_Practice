import pandas as pd
from datetime import timedelta

df = pd.read_excel("Data.xlsx")
df['Column1'] = pd.to_datetime(df['Column1'])
df['Column2'] = pd.to_datetime(df['Column2'])
df['Column3'] = abs(df["Column1"]-df["Column2"])
lambda_func = lambda x: x.seconds
df['Column4'] = df['Column3'].apply(lambda_func)
res = lambda x: 'Error' if x >=3600 else 'OK'
df['result'] = df['Column4'].apply(res)
print(df)
