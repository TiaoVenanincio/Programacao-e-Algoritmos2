import timeit
import matplotlib.pyplot as plt

def soma(n):
    soma = 0
    for i in range(n):
        soma = soma + i
    return soma

lista_n = [100, 1_000, 10_000, 100_000, 1_000_000]
tempos = []

for n in lista_n:
    t_ini = timeit.default_timer()
    res = soma(n)
    t_fim = timeit.default_timer()
    t_total = t_fim - t_ini
    print(t_total)
    tempos.append(t_total)

print(tempos)
plt.plot(lista_n, tempos)
plt.xlabel('Tamanho da lista')
plt.ylabel('Tempo de execução')
plt.show()
