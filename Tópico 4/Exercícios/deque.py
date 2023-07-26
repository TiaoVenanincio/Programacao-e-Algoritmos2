class Deque:
    def __init__(self):
        self.items = []

    def estaVazia(self):
        return self.items == []
    
    def addAtras(self, item):
        self.items.insert(0, item)

    def addFrente(self, item):
        self.items.append(0, item)

    def removeFrente(self):
        return self.items.pop()
    
    def removeAtras(self):
        return self.items.pop(0)

    def tamanho(self):
        return len(self.items)