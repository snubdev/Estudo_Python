import json

def load_json(file_path):
    with open(file_path) as f:
        data = json.load(f)

    print(data)
    return data

def search_json(data, search_key):
    result = []

    def search_recursive(d, key):
        if isinstance(d, dict):
            for k, v in d.items():
                if k == key:
                    result.append(v)
                if isinstance(v, (dict, list)):
                    search_recursive(v, key)
        elif isinstance(d, list):
            for item in d:
                if isinstance(item, (dict, list)):
                    search_recursive(item, key)

    search_recursive(data, search_key)
    return result

def main():
    file_path = 'payload.json'
    data = load_json(file_path)

    if data is None:
        return 'Payload Vazio'

    search_key = 'industry'

    result = search_json(data, search_key)

    print(f"Valores encontrados para a chave '{search_key}':")

    for r in result:
        print(r)

if __name__ == '__main__':
    main()
