

num = int(input("Digite um numero: "))
cont = 0
cont = cont + 1
for cont in range(20):
    if num % 2 == 0:
        print(num * cont)
    else:
        print("Esse numero não é par")

    