def adicionar_voluntario(lista,nome,idade):
    novo = {
        "id": len(lista) + 1,
        "nome": nome,
        "idade": idade
    }

    lista.append(novo)

def listar_voluntarios(lista):
    for voluntario in lista:
        print(voluntario["nome"])

def buscar(lista,id):
    for voluntario in lista:
        if voluntario["id"] == id:
            print(voluntario["nome"])
            return
    print("Não encontrado")

def remover(lista,id):
    for voluntario in lista:
        if voluntario["id"] == id:
            lista.remove(voluntario)
            print("Removido")
            return
    print("Não encontrado")


# ---------------- USO ----------------

voluntarios = []

adicionar_voluntario(voluntarios, "Ana", 20)
adicionar_voluntario(voluntarios, "Carlos", 25)

listar_voluntarios(voluntarios)

buscar(voluntarios, 1)

remover(voluntarios, 1)

listar_voluntarios(voluntarios)
