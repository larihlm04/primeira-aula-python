tabela = {"Alface": 5.00,
    "Tomate": 8.30,
    "Limão": 4.45,
    "Banana": 5.67}
total = 0
while True:    
    produto = input("Qual produto você quer adicionar: ").captalize()
    qntd = int(input("Quanto você quer adicionar: "))
    subtotal = tabela.get(produto) * qntd
    total += subtotal 
    sair = input("Gostaria de finalizar: ")
    if sair == "sim":
        print(f"O valor total é R${total:.2f}")
        break
    else:
        continue