#Realiza a soma dos números de 0 a n para valores de n variaveis
#Conta o tempo gasto para cada valor de n
#Plota um grafico comparando o tamanho do n e o tempo de execucao

import timeit
import matplotlib.pyplot as plt

def soma(n):
    soma = 0
    for i in range(n+1):
        soma += i
    return soma

lista_n = [100, 1_000, 10_000, 100_000, 1_000_000]
tempos, resultados = [], []

for n in lista_n:
    t_ini = timeit.default_timer()
    resultado = soma(n)
    t_fim = timeit.default_timer()
    t_total = t_fim - t_ini
    resultados.append(resultado)
    tempos.append(t_total)
    
print(resultados)
plt.plot(tempos, lista_n)
plt.ylabel('Tamanho de N')
plt.xlabel('Tempo de execução')
plt.show()
