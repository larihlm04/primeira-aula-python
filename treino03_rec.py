cont = 0
acumulador = 0
for cont in range(5):
    n = int(input("Digite um número: "))
    if n % 2 == 0:
        acumulador = acumulador + n
print(acumulador)
    