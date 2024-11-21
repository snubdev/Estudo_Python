import csv

data = ["021", "Tablet Pro", "Eletrônicos", "499.99", "20"]

with open('dados.csv', mode='a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(data)