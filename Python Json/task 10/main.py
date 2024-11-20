import json
import csv

def load_json(file_path):
    with open(file_path) as f:
        data = json.load(f)

    print(data)
    return data

def create_csv(data, file_name):
    with open(file_name, 'w', newline='', encoding='utf-8') as csv_f:
        writer_csv = csv.writer(csv_f)

        writer_csv.writerow(data['produtos'][0].keys())

        for i in data['produtos']:
            writer_csv.writerow(i.values())

    return f'JSON convertido para CSV com sucesso. Arquivo salvo como {file_name}'

def main():
    file_path = 'payload.json'
    data = load_json(file_path)

    result = create_csv(data, 'produtos.csv')

    print(result)


# Execução do script
if __name__ == '__main__':
    main()

