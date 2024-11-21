import pandas as pd

def group_csv(file_1, file_2, name_column):
    df1 = pd.read_csv(file_1)
    df2 = pd.read_csv(file_2)

    if name_column not in df1.columns or name_column not in df2.columns:
        print(f"A coluna '{name_column}' não foi encontrada em um dos arquivos.")
        return None

    df_combind = pd.concat([df1, df2])

    print(df_combind)

    df_combind.to_csv('produtos.csv', index=False)

    return 'Agrupamento concluido'

file_1 = 'dados.csv'
file_2 = 'new_dados.csv'
name_column = 'Categoria'

result = group_csv(file_1, file_2, name_column)

