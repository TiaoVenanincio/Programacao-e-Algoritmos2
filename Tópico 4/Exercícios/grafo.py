class No:
    def __init__(self, indice, vizinhos=None, atributos=None):
        self.indice = indice

        if vizinhos is None:
            self.dici_vizinhos = {}
        else:
            self.dici_vizinhos = vizinhos

        if atributos is None:
            self.dici_atributos = {}
        else:
            self.dici_atributos = atributos

    def adiciona_vizinho(self, indice_viz, peso=1):
        self.dici_vizinhos[indice_viz] = peso

    def indices_vizinhos(self):
        return list(self.dici_vizinhos.keys())
    
    def retorna_peso(self, indice_viz):
        if indice_viz in self.dici_vizinhos:
            return self.dici_vizinhos[indice_viz]
        else:
            print("No {} e {} nao sao vizinhos".format(self.indice, indice_viz))
            

class Grafo:
    def __init__(self):
        self.dici_nos = {}

    def adiciona_no(self, indice_no, vizinhos=None, atributos=None):
        no = No(indice_no, vizinhos, atributos)
        self.dici_nos[indice_no] = no

    def retorna_no(self, indice_no):
        return self.dici_nos[indice_no]
    
    def nos_grafo(self):
        return list(self.dici_nos.keys())
    
    def adiciona_aresta(self, indice_v1, indice_v2, peso=1):
        if indice_v1 not in self.dici_nos:
            self.adiciona_no(indice_v1)
        if indice_v2 not in self.dici_nos:
            self.adiciona_no(indice_v2)

        self.dici_nos[indice_v1].adiciona_vizinho(indice_v2, peso)
        self.dici_nos[indice_v2].adiciona_vizinho(indice_v1, peso)

    def estao_conectados(self, indice_no1, indice_no2):
        if indice_no1 not in self.dici_nos:
            print('No {} não consta no grafo'.format(indice_no1))
            return None
        if indice_no2 not in self.dici_nos:
            print('No {} não consta no grafo'.format(indice_no2))
            return None
        if indice_no2 in self.dici_nos[indice_no1].indices_vizinhos():
            return True
        else:
            return False
        
    def retorna_peso(self, indice_no1, indice_no2):
        if indice_no1 not in self.dici_nos:
            print('No {} não consta no grafo'.format(indice_no1))
            return None
        if indice_no2 not in self.dici_nos:
            print('No {} não consta no grafo'.format(indice_no2))
            return None
        if indice_no2 not in self.dici_nos[indice_no1].indices_vizinhos():
            print("No {} e {} não são vizinhos".format(indice_no1, indice_no2))
        else:
            return self.dici_nos[indice_no1].retorna_peso(indice_no2)
        
    def adiciona_arestas(self, lista_arestas, pesos):
        indice_aresta = 0
        for aresta in lista_arestas:
            indice_v1 = aresta[0]
            indice_v2 = aresta[1]
            self.adiciona_aresta(indice_v1, indice_v2, pesos[indice_aresta])
            indice_aresta += 1

    def imprime_arestas(self):
        for ind_no in self.nos_grafo():
            no = self.retorna_no(ind_no)
            for ind_viz in no.indices_vizinhos():
                peso = no.retorna_peso(ind_viz)
                if no.indice<ind_viz:
                    print("{}, {}, {}".format(no.indice, ind_viz, peso))

#exemplo de uso da classe:
g = Grafo()
for i in range(6):
    g.adiciona_no(i)

g.adiciona_aresta(0,1,5)
g.adiciona_aresta(0,5,2)
g.adiciona_aresta(1,2,4)
g.adiciona_aresta(2,3)
g.adiciona_aresta(3,4,7)
g.adiciona_aresta(3,5,3)
g.adiciona_aresta(4,0)
g.adiciona_aresta(5,4,8)
g.adiciona_aresta(5,2,1)

g.imprime_arestas()

g2 = Grafo()
arestas = [[0,1], [0,3], [2,1], [3,4], [4,5]]
pesos = [4, 7, 2, 5, 3]
g2.adiciona_arestas(arestas, pesos)
print()
g2.imprime_arestas
print(g2.estao_conectados(0,3))
print(g2.retorna_peso(0,4))