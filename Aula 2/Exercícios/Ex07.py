def soma(lista):
    soma_atual = 0
    nova_lista = []
    for i in range(len(lista)):
        soma_atual += lista [i]
        nova_lista.append(soma_atual)
    return nova_lista


lista = [5, 2, 4, 1, 3, 2, 4]
nova_lista = soma(lista)
print(nova_lista)