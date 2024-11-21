import pandas as pd

df = pd.read_csv('dados.csv')

df_sorted = df.sort_values(by='Categoria')

print(df_sorted)

df_sorted.to_csv('new_dados_ordenados.csv', index=False)
