# Curso intensivo de Python
#
# Exercício 6.2-Um dicionário Python pode ser usado para modelar um dicionário de verdade. No entanto, para
# evitar confusão, vamos chamá-lo de glossário.
#
# • Pense em cinco palavras relacionadas à programação que você conheceu nos capítulos anteriores. Use essas
# palavras como chaves em seu glossário e armazene seus significados como valores.
#
# • Mostre cada palavra e seu significado em uma saída formatada de modo elegante. Você pode exibir a palavra
# seguida de dois-pontos e depois o seu significado, ou apresentar a palavra em uma linha e então exibir seu
# significado indentado em uma segunda linha. Utilize o caractere de quebra de linha (\n) para inserir uma linha
# em branco entre cada par palavra significado em sua saída.

glossario = {
    'indentar': 'O termo indentar vem do inglês indentation e significa o recuo de um texto em relação a sua margem esquerda',
    'string': 'Conjunto de caracteres numa determinada ordem',
    'concatenar': 'Juntar duas ou mais sequências de caracteres',
    'interpolar': 'Inserir uma string no meio de outra',
    'looping': 'Em programação, o termo looping é comumente entendido como ciclos. Repetição de um trecho de código',
}

for key, value in glossario.items():
    print('\n' + key.title() + ': \n\t' + value + '.')