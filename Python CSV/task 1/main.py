import csv

with open('dados.csv', mode='r', newline='', encoding='utf-8') as f:
    data = csv.reader(f)

    for r in data:
        print(r)



