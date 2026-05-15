def f(salario:float,cargo:str):
    if cargo == "junior":
        return salario * 1.05
    elif cargo == "pleno":
        return salario * 1.10
    elif cargo == "senior":
        return salario * 1.15

resultado = f(1.500,"pleno")
print(f"O salário é de:",resultado)

