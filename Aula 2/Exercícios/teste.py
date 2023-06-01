import random
import matplotlib.pyplot as plt
import time

movimento_permitido = 0.5

def plot_graph(tempo, media):
    plt.plot(tempo, media, label='Média')
    plt.xlabel('Iterações')
    plt.ylabel('Media')
    plt.title('Gráfico de Média e Maior')
    plt.legend()
    plt.show()

x = 0
y = 0
pos_x = random.randint(-10,10)
pos_y = random.randint(-10,10)

media, maior_, tempo = [], [], []

lista_n = []
for i in range(1,(200+1)):
    lista_n.append(i)
    
for n in lista_n:
    
    lista_ = []
    print("Processando: %d iterações..." % n)
    t_ini =  time.time()
    for j in range(n):
        #pos_x = random.randint(-10,10)
        #pos_y = random.randint(-10,10)
    
        i=1
        while True:
            sentido = random.randint(0, 7)
            if sentido == 0 and y < 10:  # cima
                y += movimento_permitido
            elif sentido == 1 and y > -10:  # baixo
                y -= movimento_permitido
            elif sentido == 2 and x > -10:  # esquerda
                x -= movimento_permitido
            elif sentido == 3 and x < 10:  # direita
                x += movimento_permitido
            elif sentido == 4 and x > -10 and y < 10:  # sup esq
                x -= movimento_permitido
                y += movimento_permitido
            elif sentido == 5 and x < 10 and y < 10:  # sup dir
                x += movimento_permitido
                y += movimento_permitido
            elif sentido == 6 and x > -10 and y > -10:  # inf esq
                x -= movimento_permitido
                y -= movimento_permitido
            elif sentido == 7 and x < 10 and y > -10:  # inf dir
                x += movimento_permitido
                y -= movimento_permitido


            if x == pos_x and y == pos_y:
                break
            i += 1

    lista_.append(i)
    t_fim = time.time()
    t_total = t_fim - t_ini
    print("Tempo gasto: %f" % t_total)

    soma = 0
    for dado in lista_:
        soma += dado
    media.append(soma / (len(lista_)))

soma_medias = 0
print("Gerando média das médias...")
for dado in media:
    soma_medias += dado
media_da_media = soma_medias / len(media)
print("Media das medias: %f " % media_da_media)
print("Gerando gráficos... Concluido.")
plot_graph(lista_n, media)