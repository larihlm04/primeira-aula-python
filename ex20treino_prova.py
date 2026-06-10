ano = int(input("Digite um ano: "))
if (ano % 100 == 0) and (ano % 400 == 0):
    print("Esse ano é bissexto")
else:
    print("Esse ano não é bissexto")