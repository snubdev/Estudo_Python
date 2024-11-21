import pandas as pd
import numpy as np

def split_csv(file_csv, num_division):
    df = pd.read_csv(file_csv)

    parts = np.array_split(df, num_division)

    for i, p in enumerate(parts):
        name_file = f'dados_{i}.csv'
        p.to_csv(name_file, index=False)
        print(f'Arquivo {name_file} criado com sucesso')

file_csv = 'dados.csv'
num_division = 2

split_csv(file_csv, num_division)

