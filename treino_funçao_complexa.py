lista = [
    {"id": 1,"nome": "Ana"},
    {"id": 2,"nome": "Carlos"},
    {"id": 3,"nome": "Julia"}
    
]

def adicionar_nome(lista,nome):
    novo =  {
     "id": len(lista) + 1,
     "nome": nome
    }

    lista.append(novo)
    return novo

resultado = adicionar_nome(lista,"Maria")
print(f"Pessoa adicionada:",resultado)

def buscar_por_id(lista,id):
    for pessoa in lista:
        if pessoa["id"] == id:
            return pessoa
    return None

resultado = buscar_por_id(lista,1)
print(f"Nome buscado:",resultado)


def atualizar_nome(lista,id,novo):
    for pessoa in lista:
        if pessoa["id"] == id:
            pessoa["nome"] = novo
            return novo
    return False

resultado = atualizar_nome(lista,1,"Larissa")
print(f"Nome atualizado:",resultado)