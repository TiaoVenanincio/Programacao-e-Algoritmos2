# Estrutura de Dados
- É uma forma de organizar e gerenciar um conjuto de dados, de modo a facilitar o acesso e modificação dos mesmos

## Pilhas
- Um dado é sempre adicionado ou removido ao final da sequência (topo)
- last-in-first-out (LIFO)

## Filas
- Um dado é sempre adicionado ao fim da fila, ao remover, o dado removido é sempre o do ínicio
- first-in-first-out (FIFO)

## Deque
- Parecidos com filas, porém itens podem ser adicionados ou removidos de qualquer lado
- Possuem implementações mais complexas que filas e podem possuir operações mais ineficientes

## Lista encadeada
- Cada elemento possui duas informações, um valor e o endereço do proximo elemento
- Diferença pra vetores é que os vetores alocam de forma contígua os dados na memória. Tais vetores possuem tamanho fixo.

## Árvores
- Forma simples e intuitiva de organizar informações
- Possibilida armazenamento de forma hierárquica
- É uma estrutura de dado não linear
- Nó: Armazena informação
- Aresta: Conecta dois nós para indicar uma relação entre eles
- Raiz: Único nó que não possui uma aresta apontando para ele
- Caminho: Sequencia ordenada de nós conectados por arestas
- Filhos: Conjunto de nós que recebem conexões de um mesmo nó i (pai)
- Folha: Nó que não possui filhos
- Altura da árvore: Maior nível de qualquer nó

## Árvore binária
- Cada nó possui no máximo 2 filhos

## Grafos
- Composto por vértices (nós que representam uma entidade) e arestas
- Representado por G = (V, A) -> G é o nome do grafo, V é o conjunto de vértices e A de arestas
- Ordem de um grafo é o número de vértices (|V|)
- Número de arestas: |A|
- Vértices adjacentes (vizinhos) e Arestas adjacentes (vizinhas)
- Grafo trivial: Apenas um vértice
- Grafo simples: sem laços ou arestas múltiplas
- Grafo completo: todos os vértices (n) tem arestas ligando a todos os outros vértices, é chamado de Kn (ex: k4)
- Grau de entrada e saída de um vértice: número de arestas que entram e saem
- Caminho é uma sequência de vértices adjacentes
- Ciclo: começa e termina no mesmo vértice
- Caminho hamiltoniano: contém cada vértice do grafo exatamente uma vez
- Caminho euleriano: contém cada aresta do grafo exatamente uma vez
- Grafo conexo: se cada vértice tem um caminho a qualquer outro vértice
- Grafo desconexo: quando não há caminho para um ou mais vértices
- Densidade de grafos: 2|A| / (|V|(|V|-1)) (máximo 1, min 0)
- Pode ser representado por uma matriz de adjacência (alto custo de memoria) ou lista de adjacência (menor custo de memoria)


## Grafos direcionados ou dígrafos
- Arestas tem direção indicadas por seta
- Pode haver Loop ou referenciar o próprio vértice
- Arestas podem ter pesos
- Arestas podem ser múltiplas, ou seja, mais de uma aresta ligando dois mesmos vértices