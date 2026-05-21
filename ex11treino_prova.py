numero_1 = int(input("Digite um numero: "))
numero_2 = int(input("Digite um numero: "))
menus = input("Digite um menu: ")

while menus != "sair".lower:
    menu_1 = numero_1 + numero_2
    menu_2 = numero_1 - numero_2
    menu_3 = numero_1 * numero_2
    menu_4 = numero_1 / numero_2

    if menus == "menu_1":
        print(menu_1)
    elif menus == "menu_2":
        print(menu_2)
    elif menus == "menu_3":
        print(menu_3)
    elif menus == "menu_4":
        print(menu_4)

    break