def acesso(usuario,admin,ativo,permissao,erro):
    if (usuario and ativo):
        return permissao
    elif (not ativo) and usuario:
        return erro
    elif (admin and ativo):
        return permissao
    elif (not ativo) and admin:
        return erro

usuario = False
admin = True
ativo = False
permissao = True
erro = False


decisao = acesso(usuario,admin,ativo,permissao,erro)
print(decisao)