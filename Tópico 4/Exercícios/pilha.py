class Pilha:
    def __init__(self):
        self.items = []

    def estaVazia(self):
        return len(self.items)
    
    def adiciona(self, item):
        self.items.append(item)

    def remove(self):
        return self.items.pop()
    
    def topo(self):
        return self.items[len(self.items)-1]
    
    def tamanho(self):
        return len(self.items)
    
s = Pilha()

print(s.estaVazia())
s.adiciona(4)
s.adiciona('casa')
print(s.topo())
s.adiciona(True)
print(s.tamanho())
print(s.estaVazia())
s.adiciona(8.4)
print(s.remove())
print(s.remove())
print(s.tamanho())