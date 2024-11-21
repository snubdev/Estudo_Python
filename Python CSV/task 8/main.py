import pandas as pd

df = pd.read_csv('dados.csv')

media = df['Preço'].mean()

print(f'O valor da Média da coluna é {media}')
