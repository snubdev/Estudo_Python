import csv
import pandas as pd


produtos_eletronicos = [
    {"id": 1,"nome": "Smartphone","categoria": "Eletrônicos","preco": 1999.90,"quantidade": 30},
    {"id": 2,"nome": "Televisão 4K","categoria": "Eletrônicos","preco": 2999.90,"quantidade": 15},
    {"id": 3,"nome": "Notebook","categoria": "Eletrônicos","preco": 4999.90,"quantidade": 20},
    {"id": 4,"nome": "Fone de Ouvido Bluetooth","categoria": "Eletrônicos","preco": 299.90,"quantidade": 50},
    {"id": 5,"nome": "Câmera Digital","categoria": "Eletrônicos","preco": 1599.90,"quantidade": 10},
    {"id": 6,"nome": "Tablet","categoria": "Eletrônicos","preco": 999.90,"quantidade": 25},
    {"id": 7,"nome": "Console de Videogame","categoria": "Eletrônicos","preco": 2499.90,"quantidade": 18},
    {"id": 8,"nome": "Impressora","categoria": "Eletrônicos","preco": 499.90,"quantidade": 12},
    {"id": 9,"nome": "Smartwatch","categoria": "Eletrônicos","preco": 799.90,"quantidade": 20},
    {"id": 10,"nome": "Caixa de Som Bluetooth","categoria": "Eletrônicos","preco": 349.90,"quantidade": 40}
]

file_name = 'dados.csv'

with open(file_name, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=produtos_eletronicos[0].keys())

    writer.writeheader()
    writer.writerows(produtos_eletronicos)

print('Arquivo criado com sucesso')

