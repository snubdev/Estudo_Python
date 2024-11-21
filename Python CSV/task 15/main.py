import pandas as pd

df = pd.read_csv('dados.csv')

df = df.drop(columns=['Status'])

df.to_csv('dados.csv', index=False)