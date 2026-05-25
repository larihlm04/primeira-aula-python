salario = float(input("digite o salario: "))
aumento = float(input("digite a porcentagem do aumento: "))

novo_salario = salario * (1 + aumento/100)

print(f"Salario antigo:{salario},Aumento:{aumento},Novo salario:{novo_salario}")