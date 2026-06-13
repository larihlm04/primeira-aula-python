produtos = [
    { "nome": "Alface","preco": 5.00,
    "nome":"Tomate", "preco": 8.30,
    "nome": "Limão", "preco": 4.45,
    "nome": "Banana", "preco": 5.67 
    }
]

for produto in produtos:
    if produto["preco"] >= 5.5:
        print(f"O produto é:", produto["nome"])


