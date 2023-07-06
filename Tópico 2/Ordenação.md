# Algoritmos de ordenação:
## Bubble Sort:
- Se o indice L[i] for < L[i-1], troca ambos
- O passo anterior é repetido até que não haja mais trocas
- melhor caso: O(n) - Apenas se tiver a melhoria, senão é O(n²)
- pior caso: O(n²)

## Selection sort:
- Varre o vetor procurando o menor número e troca ele de posicao com o primeiro da lista
- Assim para o segundo, terceiro...
- Melhor e pior caso: O(n²)

## Insertion sort:
- Varre o vetor, pega o indice do primeiro numero, desloca os numeros anteriores a ele para a direita
- Coloca o menor numero na posicao á esquerda que foi liberada
- melhor caso = O(n)
- pior caso = O(n²)

## Ordenação por índices:
- Cria uma lista com os índices na ordem de ordenação
- Ex: idades[4, 2, 1, 6]
-     nomes [Tiao, Marcos, Ana, Paula]
-     lista_indices[2, 1, 3, 0]  <- representa os indices das idades em ordem crescente
-     Depois, é só criar duas novas listas e usar o append para cada um desses indices da lista para gerar as listas ordenadas

## Merge sort:
- Dividir e conquistar
- Pilha de recursão
- Pior caso: O(n log n)
- O problema é divido em sub-problemas menores, do mesmo tipo e, se possível, do mesmo tamanho
- É feita a ordenação desses sub-problemas
- No fim, as soluções são unificadas sendo adicionadas a uma nova lista do menor para o maior das duas soluções

## Quick sort:
- O mais utilizado para ordenar sequencia de valores
- Pior caso: O(n log n) ou O(n²), caso extremamente raro, mas em geral é mais rápido que o merge sort
- Dividir e conquistar
- 1. Escolhe o pivô, parte a lista em elementos que vão estar a esquerda e a direita do pivô
- 2. Varre a lista do inicio ao fim para encontrar um elemento maior que o pivô
- 3. Varre do final do inicio até encontrar um elemento menor que o pivô
- 4. Troca esses elementos e faz a recursão ate o indice da esquerda (do inicio ao fim) cruze com o indice da direita (do fim ao inicio)
- 5. Agora troca o pivô pelo indice da direita e aplica os passos de 1 a 4 nas listas a esquerda e a direta do pivô e faz a recursão

## Counting sort:
- Ordenação por contagem, sem comparação
- Sabemos o valor do maior número -> k
- Dada uma lista de números inteiros, cria-se uma lista de contagem da frequência dos números da lista desordenada
- Através da lista de contagem da freqûencia, cria-se o vetor ordenado
