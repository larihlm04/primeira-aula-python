lista = [
    {"nome": "Ana"},
    {"nome": "Carlos"},
    {"nome": "Julia"}
    
]

for pessoa in lista:
    print(pessoa["nome"])


def buscar_nome(lista,nome):
    for pessoa in lista:
        if pessoa["nome"] == nome:
            return pessoa
    return None

resultado = buscar_nome(lista,"Carlos")
print(f"Busca:", resultado)

def remover_nome(lista,nome):
    for pessoa in lista:
        if pessoa["nome"] == nome:
            lista.remove(pessoa)
            return True
    return False

removido = remover_nome(lista,"Julia")
print(f"Removido:",removido)