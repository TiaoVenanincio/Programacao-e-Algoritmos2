#Se o numero for par, adiciona-o ao fim da lista
#e, na posicao atual do numero par, multiplica-o por 3 e substitui.

def modifica(lista):
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            lista.append(lista[i])
            lista[i] *= 3
 



lista = [1, 2, 3, 4, 5]
modifica(lista)
print(lista)