class Fila:
    def __init__(self):
        self.items = []

    def estaVazia(self):
        return self.items == []
    
    def enfileira(self, item):
        self.items.insert(0, item)

    def desenfileira(self):
        return self.items.pop()
    
    def tamanho(self):
        return len(self.items)
    
#Exercicio batata quente:
def batata_quente(nomes, k):
    fila = Fila()
    for nome in nomes:
        fila.enfileira(nome)

    while fila.tamanho() > 1:
        for i in range(k):
            fila.enfileira(fila.desenfileira())
        fila.desenfileira()

    return fila.desenfileira()

nomes = ["Tião", "Lavínia", "Yago", "Ricardo", "Marcia", "Julia"]
nome_final = batata_quente(nomes, 3)
print(nome_final)