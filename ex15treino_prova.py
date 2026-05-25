salario = float(input("digite o salario: "))
cargo = input("digite o cargo: ")
filhos = input("tem filhos sim ou nao:")

if cargo == "junior":
    novo_salario = salario * 1.10
elif cargo == "pleno":
    novo_salario = salario * 1.20
elif cargo == "senior":
    novo_salario = salario * 1.30
elif filhos == "sim".lower:
    novo_salario = salario + 500 
else:
    print("Cargo não identificado")

print(f"Meu salário é:{salario},Meu cargo é:{cargo},Meu novo salário é:{novo_salario}")