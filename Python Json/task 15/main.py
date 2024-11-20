import json

def load_json(file_path):
    with open(file_path) as f:
        data = json.load(f)

    print(data)
    return data

def extract_values(data, key):
    values = []

    def search(obj):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k == key:
                    values.append(v)
                elif isinstance(v, (dict, list)):
                    search(v)
        elif isinstance(obj, list):
            for item in obj:
                if isinstance(item, (dict, list)):
                    search(item)

    search(data)
    return values

def main():
    file_path = 'payload.json'
    data = load_json(file_path)

    if data is None:
        return 'Payload Vazio'

    search_key = 'contact'

    result = extract_values(data, search_key)

    for r in result:
        print(r)

if __name__ == '__main__':
    main()

