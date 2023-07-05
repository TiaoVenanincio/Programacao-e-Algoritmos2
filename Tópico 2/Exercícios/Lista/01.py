# Faça um programa que leia n nomes inserindo-os em uma lista de forma ordenada
#utilizando a ideia do algoritmo da inserção. No final, o programa deve mostrar todos os nomes
#ordenados alfabeticamente.

nomes = ['Sebastiao','Yago','Maria','Ana','Valter']

indice_minimo =  nomes[0][0]
for i in range(1,len(nomes)):
    while i > 0 and nomes[i-1][0] > nomes[i][0]:
    #Desloca os itens da esqueda para direta e, no espaço que sobra na direita(j),
    #insere o menor número
        aux = nomes[i]
        nomes[i] = nomes[i-1]
        nomes[i-1] = aux
        i = i - 1

print(nomes)


