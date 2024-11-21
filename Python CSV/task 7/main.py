import pandas as pd

df1 = pd.read_csv('dados.csv')
df2 = pd.read_csv('new_dados.csv')

df_combind = pd.concat([df1, df2])

print(df_combind)

df_combind.to_csv('produtos.csv', index=False)
