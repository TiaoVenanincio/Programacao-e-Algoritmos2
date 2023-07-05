#Imprime o indice do maior valor dentro de uma lista

def indice_maior(lista):
  maior = lista[0]
  indice = 0
  for i in range(1,len(lista)):
      if maior < lista[i]:
        maior = lista[i]
        indice = i
        
  print("O indice do maior numero é %d" % indice)

lista = [1, 2, 3, 10, 9, 7, 100, 0, -200]
indice_maior(lista)