# Curso intensivo de Python
#
# Exercício 6.5-Crie um dicionário que contenha três rios importantes e o país que cada rio corta.
# Um par chave-valor poderia ser 'nilo': 'egito'.
#
rios = {
    'nilo': 'egito',
    'amazonas': 'brasil',
    'mackenzie': 'canadá',
}

# • Use um laço para exibir uma frase sobre cada rio, por exemplo, O Nilo corre pelo Egito.
for key, value in rios.items():
    print('O rio ' + key.title() + ' corre pelo ' + value.title() + '.')

# • Use um laço para exibir o nome de cada rio incluído no dicionário.
for key, value in rios.items():
    print('\n' + key.title())

# • Use um laço para exibir o nome de cada país incluído no dicionário.
for key, value in rios.items():
    print('\n' + value.title())


