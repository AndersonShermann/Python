# Curso intensivo de Python
#
# Exercício 6.9-Crie um dicionário chamado favorite_places. Pense em três nomes para usar como chaves do dicionário
# e armazene de um a três lugares favoritos para cada pessoa. Para deixar este exercício um pouco mais interessante,
# peça a alguns amigos que nomeiem alguns de seus lugares favoritos. Percorra o dicionário com um laço e apresente o
# nome de cada pessoa e seus lugares favoritos.

favorite_places = {
    'anderson': ['egito', 'inglaterra', 'canadá'],
    'will': ['paris', 'portugal', 'miami'],
    'jack': ['china', 'russia', 'roma']
}

for name, places in favorite_places.items():
    print('\n Os lugares favoritos de ' + name.title() + ' são: ')
    for place in places:
        print('\t' + place.title())