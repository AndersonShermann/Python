# Curso intensivo de Python
#
# Exercício 6.10-Modifique o seu programa do Exercício 6.2 (página 147) para que cada pessoa possa ter mais de um
# número favorito. Em seguida, apresente o nome de cada pessoa, juntamente com seus números favoritos.

numeros_favoritos = {
    'Anderson': [7, 10, 33],
    'Jackeline': [10, 8, 12],
    'Flávia': [21, 9, 3],
    'Bruna': [25, 21, 5],
    'Shermann': [3, 7, 9],
}

for name, numbers in numeros_favoritos.items():
    print('\n Os números favoritos de ' + name.title() + ' são: ')
    for number in numbers:
        print('\t' + str(number))