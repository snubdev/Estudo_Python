import json

def load_json(file_path):
    with open(file_path) as f:
        data = json.load(f)

    print(data)
    return data

def main():
    file_path = 'payload.json'
    data = load_json(file_path)

    print(f'Nome Empresa: {data["empresa"]["nome"]}')

    for i, department in enumerate(data['empresa']['departamentos']):
        if i == 0:
            for f in department['funcionarios']:
                print(f'Cargo {f["cargo"]}')

if __name__ == '__main__':
    main()
