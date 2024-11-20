import json

produto = {"nome": "Camiseta", "preco": 29.99, "quantidade_em_estoque": 100}

def main():
    new_json = json.dumps(produto)
    print(new_json)

if __name__ == '__main__':
    main()
