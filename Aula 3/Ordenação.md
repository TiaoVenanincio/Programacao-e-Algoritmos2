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