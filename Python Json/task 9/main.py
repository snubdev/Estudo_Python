import json

produtos = [
    {"nome": "Camiseta", "preco": 29.99, "estoque": 50},
    {"nome": "Calça", "preco": 59.99, "estoque": 30},
    {"nome": "Tênis", "preco": 99.99, "estoque": 20},
    {"nome": "Meias", "preco": 9.99, "estoque": 100},
    {"nome": "Óculos de Sol", "preco": 79.99, "estoque": 15}
]

def create_json(data, file_name):
    data_sorted = sorted(data, key=lambda x: x['preco'])

    # Convetendo para o JSON e Salvado no arquivo
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(data_sorted, f, ensure_ascii=False, indent=2)

    return 'JSON criado com sucesso'

def main():
    file_name = 'payload.json'
    result = create_json(produtos, file_name)
    print(result)

if __name__ == '__main__':
    main()

