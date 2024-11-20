import json

def load_json(file_path):
    with open(file_path) as f:
        data = json.load(f)

    print(data)
    return data

def get_all_keys(data, parent_key=''):
    keys = []

    for key, value in data.items():
        full_key = f'{parent_key}.{key}' if parent_key else key
        keys.append(full_key)

        if isinstance(value, dict):
            keys.extend(get_all_keys(value, full_key))
        elif isinstance(value, list):
            for i, item in enumerate(value):
                keys.extend(get_all_keys(item, f'{full_key}[{i}]'))

    return keys

def main():
    file_path = 'payload.json'
    data = load_json(file_path)

    if data is None:
        return 'Payload Vazio'

    keys = get_all_keys(data)

    for key in keys:
        print(key)

if __name__ == '__main__':
    main()