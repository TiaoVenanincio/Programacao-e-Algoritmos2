# Programação Orientada a Objetos

## Classe:
- Um molde para a criação do objeto

## Objeto:
- É uma instância de uma classe
- Um objeto tem propriedades específicas e comportamentos
- Propridades: Cor, peso
- Comportamentos: Andar, carregar

## Métodos:
- Construtor: def __init__(self):
- O construtor é sempre executado quando cria-se uma nova instância de uma classe
- Setters e Getters

## Encapsulamento:
- Os dados ficam encapsulados, protegidos do usuário
- Esses dados só podem ser acessados e alterados pelos métodos

## Abstração:
- Identificar elementos do mundo real e abstraí-los para o algoritmo

## POO em python:
- Python segue fortemente o conceito de orientação a objetos
- Mais comum para criar uma classe: class

## Herança:
- Ex de subclasse: class Programador(Funcionario) #pode ter mais classes pai
- Herda os atributos da classe pai (super classe)
- Inicializa a subclasse, usa o __init__, depois usa o super().__init___ para pegar os atributos do pai
- Pode chamar os métodos da classe pai com super(). 
- Ver exemplo no slide.

## Polimorfismo:
- Descreve situações nas quais uma mesma função pode ser aplicada em objetos diferentes
- Não necessita de tratamento especial no momento da chamada
- Ex: def soma (x, y): return (x+y)
- Pode ser inteiro, float ou string
- Método fora das classes
