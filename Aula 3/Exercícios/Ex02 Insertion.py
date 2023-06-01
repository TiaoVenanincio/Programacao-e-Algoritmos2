#insertion sort
lista = [5, 4, 3, 2, 1, 6, 7, 0]

#percorre a partir do segundo elemento
for i in range(1, len(lista)):
    j = i

    while j > 0 and lista[j-1] > lista[j]:
        aux = lista[j]
        lista[j] = lista[j-1]
        lista[j-1] = aux
        j = j - 1


print(lista)
