import csv

file = 'dados.csv'
new_file = 'new_dados.csv'

line_remove = 21

with open(file, 'r') as infile, open(new_file, 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    for i, row in enumerate(reader):
        if i != line_remove:
            writer.writerow(row)