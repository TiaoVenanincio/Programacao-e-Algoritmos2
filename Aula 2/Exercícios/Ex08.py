#Verifica se as duas listas possuem os mesmos números, independente da ordem

def verifica(lista_1, lista_2):
    for i in range(len(lista_1)):
        passou = False  #reinicia a variavel
        for j in range(len(lista_2)):
            if lista_1[i] == lista_2[j]:
                passou = True #confirma que o numero atual está na outra lista
                break  #evita que verifique além do necessário
        if passou == False: #caso nao tenha encontrado o mesmo numero na outra lista
            return 0 #encerra a execuçao
        
    return 1


lista_1 = [2, 6, 4, 8, 10, 3]
lista_2 = [10, 3, 2, 4, 6, 8]
estado = verifica(lista_1, lista_2)
if estado == 1:
    print("Possui os mesmos numeros")
else:
    print("Nao possui os mesmos numeros")


lista_3 = [2, 6, 4, 8, 10, 100]
lista_4 = [10, 3, 2, 4, 6, 8]
estado = verifica(lista_3, lista_4)
if estado == 1:
    print("Possui os mesmos numeros")
else:
    print("Nao possui os mesmos numeros")