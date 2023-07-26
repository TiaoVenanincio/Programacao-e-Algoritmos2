class Node:
    def __init__(self, valor):
        self.data = valor
        self.next = None

class Lista:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None
    
    def prepend(self, valor):
        novo = Node(valor)
        novo.next = self.head
        self.head = novo

    def print(self):
        atual = self.head
        while atual != None:
            print(atual.data)
            atual = atual.next