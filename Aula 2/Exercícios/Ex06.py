def mostra_colunas(matriz):
    lista_1, lista_2 = [], []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j == 0:
                lista_1.append(matriz[i][j])
            else:
                lista_2.append(matriz[i][j])
    return lista_1, lista_2


matriz = [[1, 2],[3, 4], [5, 6]]
lista_1, lista_2 = [], []
lista_1, lista_2 = mostra_colunas(matriz)
print(lista_1, lista_2)

