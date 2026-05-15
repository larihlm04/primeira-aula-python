lista = [
    {"nome": "Ana"},
    {"nome": "Carlos"},
    {"nome": "Julia"}
    
]

print(f"O primeiro nome é:", (lista[0]["nome"]))

def adicionar_nome(lista,nome):
    novo = {"nome": nome}

    lista.append(novo)

def remover(lista,nome):
    for pessoa in lista:
        if pessoa["nome"] == nome:
            lista.remove(pessoa) 
            print("Removido") 
            return 
    print("Não encontrado")

def lista_nomes(lista):
    for pessoa in lista:
        print(pessoa["nome"])
        return

lista_nomes(lista)

adicionar_nome(lista,"Maria")

remover(lista,"Carlos")
