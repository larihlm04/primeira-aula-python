num = int(input("Digite um numero: "))
cont = 0
qntd = 0
for cont in range(50):
    if num % 2 == 0:
        num = num + 2
        print(num)
    elif num % 2 != 0:
        num = num + 2
        print(num)
    