def ordena_coluna(matriz, col):
    for i in range(1,len(matriz)):
        j = i
        while j > 0 and matriz[j-1][col] > matriz[j][col]:
            aux = matriz[j]
            matriz[j] = matriz[j-1]
            matriz[j-1] = aux
            j = j-1
    return matriz


col = 0
matriz = [[5, 4, 3], [6, 7, 8], [1, 2, 0]]
print(ordena_coluna(matriz, col))

    
    
