#Criando duas listas iguais com 10000 números desordenados e verificando o tempo 
#que cada algoritmo levará para ordená-las

import random
import time

def selection_sort(lista):
    indice_minimo = 0
    for i in range(len(lista)-1):
        #atualiza o indicide minimo
        indice_minimo = i
        for j in range(i+1, len(lista)):
            #encontra a posicao do minimo na lista nao ordenada
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j
        #troca o menor elemento com o primeiro nao ordenado
        aux = lista[i]
        lista[i] = lista[indice_minimo]
        lista[indice_minimo] = aux
    return lista

def insertion_sort(lista):
    #percorre a partir do segundo elemento
    for i in range(1, len(lista)):
        j = i
        while j > 0 and lista[j-1] > lista[j]:
        #Desloca os itens da esqueda para direta e, no espaço que sobra na direita(j),
        #insere o menor número
            aux = lista[j]
            lista[j] = lista[j-1]
            lista[j-1] = aux
            j = j - 1
    return lista



lista_1, lista_2 = [], []
for i in range(10000):
    x = random.randint(0, 10000)
    lista_1.append(x)
    lista_2.append(x)

#calcula o tempo do selection
t_inicio = time.time()
lista_1 = selection_sort(lista_1)
t_fim = time.time()
t_selection =  t_fim - t_inicio
print(t_selection)

#calcula o tempo do insertion
t_inicio = time.time()
lista_2 = insertion_sort(lista_2)
t_fim = time.time()
t_insertion =  t_fim - t_inicio
print(t_insertion)


#Conclusão: O selection se mostrou mais eficiente em relação ao tempo
# Execução do selection: aprox. 3,05s
# Execução do insertion: aprox. 6,12s

#Config. da máquina: i5 - 8265U, 8GB RAM

#Possíveis motivos: O processo de mover os elementos para a posicao correta
#no insertion pode ser um pouco mais lento do que o método de troca do selection
