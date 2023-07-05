class Televisao:
    def __init__(self, ligada, canal):
        self.ligada = ligada
        self.canal = canal

    def imprime_ligada(self):
        print(self.ligada)

    def imprime_canal(self):
        print(self.canal)

    def ligar(self):
        self.ligada = True

    def desligar(self):
        self.ligada = False

    def muda_canal_para_baixo(self):
        if self.canal != 1:
            self.canal -= 1
        else:
            self.canal = 49

    def muda_canal_para_cima(self):
        if self.canal != 49:
            self.canal += 1
        else:
            self.canal = 1

tv = Televisao(True, 2)
tv.muda_canal_para_baixo()
tv.muda_canal_para_baixo()
tv.imprime_canal()

tv2 = Televisao(True, 48)
tv2.muda_canal_para_cima()
tv2.muda_canal_para_cima()
tv2.imprime_canal()