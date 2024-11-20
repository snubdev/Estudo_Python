import json

def load_json(file_path):
    with open((file_path)) as f:
        data = json.load(f)

    print(data)
    return data

def save_json(file_name, data):
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f'{file_name} salvo com sucesso')

def main():
    file_path = 'payload.json'
    data = load_json(file_path)

    # Adiciona Chave e Valor no JSON
    data["loja"]["email"] = 'lojaexemplo@email.com'

    data["loja"]["produtos"].append({
        "nome": "Produto 3",
        "preco": 19.99,
        "quantidade_em_estoque": 100
    })

    file_name = 'new_payload.json'
    save_json(file_name, data)

if __name__ == '__main__':
    main()
