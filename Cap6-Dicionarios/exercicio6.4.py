# Curso intensivo de Python
#
# Exercício 6.4-Agora que você já sabe como percorrer um dicionário com um laço, limpe o código do Exercício 6.3
# (página 148), substituindo sua sequência de instruções print por um laço que percorra as chaves e os valores do
# dicionário. Quando tiver certeza de que seu laço funciona, acrescente mais cinco termos de Python ao seu glossário.
# Ao executar seu programa novamente, essas palavras e significados novos deverão ser automaticamente incluídos na
# saída.

glossario = {
    'indentar': 'O termo indentar vem do inglês indentation e significa o recuo de um texto em relação a sua margem esquerda',
    'string': 'Conjunto de caracteres numa determinada ordem',
    'concatenar': 'Juntar duas ou mais sequências de caracteres',
    'interpolar': 'Inserir uma string no meio de outra',
    'looping': 'Em programação, o termo looping é comumente entendido como ciclos. Repetição de um trecho de código',
}

glossario['classe'] = 'Projeto de todo objeto'
glossario['instância'] = 'A execução de uma classe'
glossario['objeto'] = 'A execução de uma classe'
glossario['herança'] = 'Capacidade de herdar as características de outra classe'
glossario['polimorfismo'] = 'Capacidade de ter funções com mesmo nome e assinatura, porém, com comportamentos diferentes'

for key, value in glossario.items():
    print('\n' + key.title() + ': \n\t' + value + '.')

