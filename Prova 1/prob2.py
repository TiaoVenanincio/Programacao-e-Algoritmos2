def busca_rg(dados, numero, indice_inicial, indice_final):
    if indice_final >= indice_inicial:
        meio = int((indice_inicial+indice_final)/2)
        
        if dados[meio][0] == numero:
            print("%s" % dados[meio][1])
    
        elif dados[meio][0] > numero:
            return busca_rg(dados,numero, indice_inicial, meio-1)
        
        else:
            return busca_rg(dados, numero, meio+1, indice_final)
    else:
        print("RG não encontrado")