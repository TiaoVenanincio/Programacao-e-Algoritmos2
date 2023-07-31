class No:
    def __init__(self, valor, esquerdo=None, direito=None):
        self.valor = valor
        self.esquerdo = esquerdo
        self.direito = direito

class ArvoreBinaria:
    def __init__(self, valor):
        self.raiz = No(valor)

    def insere_a_esquerda(self, no_arvore, valor):
        novo_no = No(valor)
        if no_arvore.esquerdo == None:
            no_arvore.esquerdo = novo_no
        else:
            novo_no.esquerdo = no_arvore.esquerdo
            no_arvore.esquerdo = novo_no

    def insere_a_direita(self, no_arvore, valor):
        novo_no = No(valor)
        if no_arvore.direito == None:
            no_arvore.direito = novo_no
        else:
            novo_no.direito = no_arvore.direito
            no_arvore.direito = novo_no

    def filho_esquerdo(self, no_arvore):
        return no_arvore.esquerdo
    
    def filho_direito(self, no_arvore):
        return no_arvore.direito