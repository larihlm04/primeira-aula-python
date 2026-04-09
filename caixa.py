tabela = {"Alface": 5.00,
    "Tomate": 8.30,
    "Limão": 4.45,
    "Banana": 5.67 }
    
produto = input("Qual produto você quer adicionar: ").lower()
qntd = int(input("Quanto você quer adicionar: "))
if produto == "Alface":
    preco = tabela.get ("Alface") * qntd
elif produto == "Limão":
    preco = tabela.get ("Limão") * qntd
elif produto == "Tomate":
    preco = tabela.get ("Tomate") * qntd
elif produto == "Banana":
    preco = tabela.get ("Banana") * qntd
print(preco)