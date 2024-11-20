import json

def open_json(payload):
    with open(payload) as f:
        data = json.load(f)
    return data

def save_json(file_name, data):
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f'{file_name} salvo com sucesso')

def main():
    file_path_1 = 'loja_1.json'
    file_path_2 = 'loja_2.json'

    data_file_1 = open_json(file_path_1)
    data_file_2 = open_json(file_path_2)

    data = (data_file_1, data_file_2)
    print(data)

    file_name = 'new_payload.json'
    save_json(file_name, data)

if __name__ == '__main__':
    main()