class Vetor:
    def __init__(self, vetor):
        self.vetor = vetor

    def inverte(self):
        for i in range(len(self.vetor)):
            self.vetor[i] = -self.vetor[i]

    def soma(self, v2):
        novo_vetor = []
        for i in range(len(self.vetor)):
            novo_vetor.append(self.vetor[i] + v2.vetor[i])
        return novo_vetor
    
v1 = Vetor([4, 2, 6, 1])
v1.inverte()
print(v1.vetor)

v2 = Vetor([1, 3, 2, 2])
v3 = v1.soma(v2)
print(v3)