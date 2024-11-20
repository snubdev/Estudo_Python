import csv
import json

def open_csv(file_path):
    with open(file_path, 'r', newline='', encoding='utf-8') as csv_f:
        reader = csv.DictReader(csv_f)

    print(reader)
    return reader

def create_json(reader, file_name):
    data = []

    for i in reader:
        data.append(i)

    products = {
        'produtos': data
    }

    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(products, f, indent=4, ensure_ascii=False)

    return f'CSV convertido para JSON com sucesso. Arquivo salvo como {file_name}'

def main():
    file_path = 'produtos.csv'
    reader = open_csv(file_path)

    file_name = 'payload.json'
    result = create_json(reader, file_name)

    print(result)

if __name__ == '__main__':
    main()

