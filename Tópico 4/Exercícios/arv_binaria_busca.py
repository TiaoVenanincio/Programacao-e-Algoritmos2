class No:
    def __init__(self, chave, valor, esquerdo=None, direito=None, pai=None):
        self.chave = chave
        self.valor = valor 
        self.esquerdo = esquerdo
        self.direito = direito
        self.pai = pai

class ArvoreBinaraiBusca:
    def __init__(self):
        self.raiz = None

    def insere(self, chave, valor):
        if self.raiz is not None:
            self._insere(chave, valor, self.raiz)
        else:
            self.raiz = No(chave, valor)

    def _insere(self, chave, valor, no_corrente):
        if chave < no_corrente.chave:
            if no_corrente.esquerdo is not None:
                self._insere(chave, valor, no_corrente.esquerdo)
            else:
                no_corrente.esquerdo = No(chave, valor, pai=no_corrente)
        else:
            if no_corrente.direito is not None:
                self._insere(chave, valor, no_corrente.direito)
            else:
                no_corrente.direito = No(chave, valor, pai=no_corrente)