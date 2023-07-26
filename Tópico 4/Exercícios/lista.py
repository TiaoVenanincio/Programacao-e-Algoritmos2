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

    def size(self):
        atual = self.head
        count = 0
        while atual is not None:
            count += 1
            atual = atual.next
        return count
    
    def append(self, valor):
        novo = Node(valor)
        novo.next = None
        if self.isEmpty()==True:
            self.head = novo
        else:
            atual = self.head
            while atual.next is not None:
                atual = atual.next
            atual.next = novo

    def pop(self):
        if self.isEmpty()==True:
            print("Não foi possivel remover o item. A lista está vazia")
            return None
        else:
            atual = self.head
            anterior = None
            while atual.next is not None:
                anterior = atual
                atual = atual.next

            if anterior is None:
                self.head = None
            else:
                anterior.next = None
            return atual.data
                