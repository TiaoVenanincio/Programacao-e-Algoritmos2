#insertion sort

def ordena(lista):
    #percorre a partir do segundo elemento
    for i in range(1, len(lista)):
        j = i

        while j > 0 and lista[j-1] > lista[j]:
        #Desloca os itens da esqueda para direta e, no espaço que sobra na direita(j),
        #insere o menor número
            aux = lista[j]
            lista[j] = lista[j-1]
            lista[j-1] = aux
            j = j - 1
    return lista



lista = [5, 4, 3, 2, 1, 6, 7, 0]
lista = ordena(lista)
print(lista)
