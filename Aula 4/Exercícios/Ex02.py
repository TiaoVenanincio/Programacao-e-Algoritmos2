class Estoque:
    def __init__(self):
        #dic = {produto, [valor, quantidade]}
        self.produtos = {"Arroz": [10.00, 5], "Banana":[15.00, 8]}

    def adiciona_produto(self, produto, valor):
        info = [valor, 0]
        self.produtos[produto] = info

    def atualiza_produto(self, produto, info):
        self.produtos[produto] = info

    def adiciona_itens(self, produto, quantidade):
        if produto in self.produtos:
            nova_quantidade = self.produtos[produto][1] + quantidade
            valor = self.produtos[produto][0]
            #Edita a quantidade mas mantem o valor
            self.atualiza_produto(produto, [valor, nova_quantidade])
        else:
            print("Produto não encontrado!\n")
    
    def remove_itens(self, produto, quantidade):
        if produto in self.produtos and self.produtos[produto][1] >= quantidade:
            nova_quantidade = self.produtos[produto][1] - quantidade
            valor = self.produtos[produto][0]
            #Edita a quantidade mas mantem o valor
            self.atualiza_produto(produto, [valor, nova_quantidade])
        else:
            print("Produto não encontrado ou estoque insuficiente!\n")

    def atualiza_preco(self, produto, novo_valor):
        if produto in self.produtos:
            quantidade = self.produtos[produto][1]
            #Edita o valor mas mantem a quantidade
            self.atualiza_produto(produto, [novo_valor, quantidade])
        else:
            print("Produto não encontrado!\n")

    def info_produto(self, produto):
        return self.produtos[produto]
    
    def imprime_estoque(self):
        for key in self.produtos.keys():
            produto = key
            valor = est.info_produto(key)[0]
            qtd = est.info_produto(key)[1]
            print("Produto: {:<10s} | Valor: {:.2f} | Qtd: {:d}".format(produto, valor, qtd))
        print("--------------------------------------------")


est = Estoque()

est.imprime_estoque()
print("Add melancia")
est.adiciona_produto("Melancia", 25.00)
est.imprime_estoque()
print("Add 2 bananas")
est.adiciona_itens("Banana", 2)
est.imprime_estoque()
print("Removendo 4 bananas")
est.remove_itens("Banana", 4)
est.imprime_estoque()
print("Atualizando preco arroz")
est.atualiza_preco("Arroz", 30.00)
est.imprime_estoque()

#Testando entradas que resultam erros
est.atualiza_preco("Ferro", 10.00)
est.remove_itens("Banana", 300)
est.adiciona_itens("Bola", 500)
est.imprime_estoque()
