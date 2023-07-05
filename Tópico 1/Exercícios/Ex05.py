#Separa os numeros de uma lista em duas novas listas, uma para pares e outra para impares

lista = []
lista_par=[]
lista_impar=[]

for i in range(1, 11):
    lista.append(i)

for numero in lista:
    if numero % 2 == 0:
        lista_par.append(numero)
    else:
        lista_impar.append(numero)

print(lista)
print(lista_par)
print(lista_impar)