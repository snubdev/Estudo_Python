import json

def load_json(file_path):
    with open(file_path) as f:
        data = json.load(f)

    print(data)
    return data


def main():
    file_path = 'payload.json'
    data = load_json(file_path)
    print(type(data))

if __name__ == '__main__':
    main()
