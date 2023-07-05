#Verifica se há um numero repetido na lista

def verifica_repetido(lista):
    iguais = False
    i = 1
    for numero in lista:
        for posicao in range(i, len(lista)):
            if numero == lista[posicao]:
                iguais = True
        i += 1
    print(iguais)

lista1 = [1, 2, 3, 3, 4]
lista2 = [1, 2, 3, 4, 5]
lista3 = [1, 1, 2, 3, 4]
lista4 = [5, 4, 3, 2, 1]
verifica_repetido(lista1)
verifica_repetido(lista2)
verifica_repetido(lista3)
verifica_repetido(lista4)