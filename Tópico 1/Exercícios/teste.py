##Dado um plano cartesiano cujas as coordenadas de x e y vão de -10 a 10
#Esse algoritmo coloca um ponto fixo em uma posicão aleatória nesse plano
#Em seguida, a partir da posicao (0,0) um ponto que pode se mover é criado
#e pode se mover em 8 direções diferentes.
#Então é calculado quantos movimentos esse ponto variavel leva para chegar
#até o ponto fixo. Também é calculada a média desses movimentos, o tempo
#para n iterações e a média das médias.
#Por fim é mostrado um gráfico com a média para cada N iterações

import random
import matplotlib.pyplot as plt
import time

movimento_permitido = 1

def plot_graph(tempo, media):
    plt.plot(tempo, media, label='Média')
    plt.xlabel('Iterações')
    plt.ylabel('Media')
    plt.title('Gráfico de Média Vs Iterações')
    plt.legend()
    plt.show()

#Posicao fixa aleatória
pos_x = random.randint(-10,10)
pos_y = random.randint(-10,10)

media, maior_, tempo = [], [], []

lista_n = [1000, 2000, 3000, 4000, 5000, 6000, 7000]
    
for n in lista_n:
    x = 0
    y = 0
    
    lista_ = []
    print("Processando: %d iterações..." % n)
    t_ini =  time.time()
    for j in range(n): 
        i=1
        while True:
            #faz a movimentação aleatória do ponto variável
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
            #verifica se ele encontrou o ponto fixo
                break
            i += 1 #senão, conta mais uma iteração

        #Registra quantas iterações foram realizadas
        lista_.append(i)
          
    t_fim = time.time()
    t_total = t_fim - t_ini
    print("Tempo gasto: %f" % t_total)

    soma = 0
    for dado in lista_:
        soma += dado
    #Faz a média das iterações para cada n
    media.append(soma / (len(lista_)))

print("Gerando média das médias...")
soma_medias = 0
for dado in media:
    soma_medias += dado
media_da_media = soma_medias / len(media)

print("Media das medias: %f " % media_da_media)
print("Gerando gráficos... Concluido.")
plot_graph(lista_n, media)