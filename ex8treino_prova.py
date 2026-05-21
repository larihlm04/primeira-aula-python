#validação usuario e senha
usuario_certo = "larihlm04"
senha_certa = 123

usuario = input("Digite o usuario: ")
senha = int(input("Digite a senha: "))
while usuario != usuario_certo:
    print("Tente novamente")
    usuario = input("Digite o usuario: ")
while senha != senha_certa:
    print("Tente novamente")
    senha = int(input("Digite o usuario: "))
if usuario == usuario_certo:
    print("Bem-vindo")
elif senha == senha_certa:
    print("Bem-vindo")
