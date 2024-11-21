import pandas as pd

df = pd.read_csv('../task 10/dados.csv')

contegem = df['Quantidade'].value_counts()[10]

print(contegem)