#Representacao em lista de adjacêcnia
grafo = [[1, 2],
         [0, 2, 3, 4],
         [0, 1, 4],
         [1],
         [1, 2]]

#Remocao da aresta entre os nós 1 e 0
grafo[0].remove(1)
grafo[1].remove(0)
print(grafo)

#adicao de uma aresta entre os nós 3 e 4:
grafo[3].append(4)
grafo[4].append(3)
print(grafo)

#adicao de um novo nó:
grafo.append([])