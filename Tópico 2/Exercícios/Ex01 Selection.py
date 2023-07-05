#selection sort
def ordena(lista):
    indice_minimo = 0
    for i in range(len(lista)-1):
        #atualiza o indicide minimo
        indice_minimo = i
        for j in range(i+1, len(lista)):
            #encontra a posicao do minimo na lista nao ordenada
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j

        #troca o menor elemento com o primeiro nao ordenado
        aux = lista[i]
        lista[i] = lista[indice_minimo]
        lista[indice_minimo] = aux

    return lista


lista = [5, 2, 3, 1, 4]
lista = ordena(lista)
print(lista)