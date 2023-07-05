#Organizando uma matriz com base em uma coluna, neste caso a coluna idade
def ordena_coluna(matriz, col):
    for i in range(1,len(matriz)):
        j = i
        while j > 0 and matriz[j-1][col] > matriz[j][col]:
            aux = matriz[j]
            matriz[j] = matriz[j-1]
            matriz[j-1] = aux
            j = j-1
    return matriz

#Matriz["Nome", idade]
matriz = [["Tiao", 21], ["Yago", 20], ["Fernanda", 18]]
matriz = ordena_coluna(matriz, 1)
print(matriz)