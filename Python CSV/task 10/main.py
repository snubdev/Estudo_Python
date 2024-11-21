import csv

file_name = 'dados.csv'

data = []

with open(file_name, mode='r', encoding='utf-8') as file:
    writer = csv.DictReader(file)

    for l in writer:
        data.append(l)

print(data)