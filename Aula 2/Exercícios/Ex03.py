def modifica(lista):
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            lista.append(lista[i])
            lista[i] *= 3
 



lista = [1, 2, 3, 4, 5]
modifica(lista)
print(lista)