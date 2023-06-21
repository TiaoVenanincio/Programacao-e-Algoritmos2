class Dados:
    def __init__(self, valores):
        self.valores = valores

    def calc_media(self):
        soma = 0
        for num in self.valores:
            soma += num
        return soma / len(self.valores)
    
    def calc_maximo(self):
        maior = self.valores[0]
        for i in range(1, len(self.valores)+1):
            if i > maior:
                maior = i
        return maior
    
    def get_valores(self):
        return self.valores

    def info_dados(self):
        print("A média é %.3f e o valor máximo é %d" %(self.calc_media(), self.calc_maximo()))

lista = Dados([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

lista.info_dados()