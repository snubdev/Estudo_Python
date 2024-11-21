import pandas as pd

df = pd.read_csv('dados.csv')

df['Status'] = ''

df.to_csv('dados.csv', index=False)