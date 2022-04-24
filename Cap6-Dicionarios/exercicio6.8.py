# Curso intensivo de Python
#
# Exercício 6.8-Crie vários dicionários, em que o nome de cada dicionário seja o nome de um animal de estimação.
# Em cada dicionário, inclua o tipo do animal e o nome do dono. Armazene esses dicionários em uma lista chamada pets.
# Em seguida, percorra sua lista com um laço e, à medida que fizer isso, apresente tudo que você sabe sobre cada
# animal de estimação.

leo = {
    'tipo': 'gato',
    'raça': 'vira lata',
    'idade': 5,
    'dono': 'anderson',
}

thor = {
    'tipo': 'cachorro',
    'raça': 'pitbull',
    'idade': 8,
    'dono': 'shermann',
}

dragnel = {
    'tipo': 'salamandra',
    'raça': 'axolote',
    'idade': 3,
    'dono': 'anderson shermann',
}

pets = [leo, thor, dragnel]

for pet in pets:
    print('\n O animal de estimação de ' + pet['dono'].title() + ' é um ' + pet['tipo'] + ' da raça ' + pet['raça'] + '. Ele tem ' + str(pet['idade']) + ' de idade.')