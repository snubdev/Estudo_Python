import csv

file = 'dados.csv'

value = 'Tablet'

with open(file, mode='r', newline='') as f:
    reader_csv = csv.reader(f)
    for line in reader_csv:
        for c in line:
            if value in c:
                print(line)