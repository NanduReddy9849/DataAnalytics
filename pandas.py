
import pandas as pd

s=pd.Series([10,20,30,40],index=['a','b','c','d'])
print(s)


# DataFrame

data={
      'Name':['Nandu','Mahesh','Charan'],
      'Age':[21,23,22],
      'city':['Tadipatri','Sajjaldinne','Koduru']
      }
df=pd.DataFrame(data)
print(df)

# Key operations

print(df.head())
print(df.tail(2))
print(df.info())
print(df.describe())
print(df.columns)
print(df.shape)

# Selection and filtering

print(df['Age'])
print(df[['Name','city']])
print(df[df['Age']>21])
print(df.iloc[1])
print(df.loc[1])
