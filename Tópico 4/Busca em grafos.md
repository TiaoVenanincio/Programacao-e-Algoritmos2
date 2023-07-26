# Buscas em grafos

## Busca em largura
- Visita os nós do grafo utilizando uma fila
- A partir de um nó inicial, todos os nós são adicionados a fila.
- Os nós da fila são analisados e os vizinhos adicionados ao final da fila
- O processo é repetido até que não haja mais nós na fila
- Precisa de um tratamento para os nós que já foram visitados

## Busca em profundidade
- Em geral, é implementada de forma recursiva
- Começa a partir de um nó inicial e explora um de seus vizinhos não visitados
- Para o nó vizinho escolhido, aplica-se a mesma estratégia de exploração para esse novo nó (recursão)
- Caso não haja mais vizinhos não visitados, volta-se para o nó anterior e explora outros caminhos possíveis.
- Os nós visitados são marcados para evitar ciclos infinitos

## Algoritmo de Dijkstra - Menor caminho
- Encontra o camnho mais curto de um vértice de origem a outro vértice no grafo
- Inicialmente, define-se uma distância infinita para todos os vértices, exceto o de origem, o qual a distância é 0.
- Em cada iteração, seleciona-se o vértice não visitado com a menor distância conhecida a partir da origem.
- Para o vérice selecionado, atualiza-se a distância dos seus vizinhos não visitados.
- O vértice é marcado e repete os 2 passos anteriores até chegar ao objetivo.