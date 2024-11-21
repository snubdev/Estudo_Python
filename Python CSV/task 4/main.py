import csv

file = 'dados.csv'

with open(file, mode='r', newline='') as f:
    reader_csv = csv.reader(f)
    line = list(reader_csv)

line_csv = 21
column_csv = 4
new_value = '10'

line[line_csv][column_csv] = new_value

with open(file, mode='w', newline='') as f:
    writer_csv = csv.writer(f)
    writer_csv.writerows(line)