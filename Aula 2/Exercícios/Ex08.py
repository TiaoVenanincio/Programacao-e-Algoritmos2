def verifica(lista_1, lista_2):
    for i in range(len(lista_1)):
        passou = False
        for j in range(len(lista_2)):
            if lista_1[i] == lista_2[j]:
                passou = True
                break
        if passou == False:
            return 0
        
    return 1


lista_1 = [2, 6, 4, 8, 10, 3]
lista_2 = [10, 3, 2, 4, 6, 8]
estado = verifica(lista_1, lista_2)
if estado == 1:
    print("Possui")
else:
    print("Nao possui")