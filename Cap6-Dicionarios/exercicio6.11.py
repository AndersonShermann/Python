# Curso intensivo de Python
#
# Exercício 6.11-Crie um dicionário chamado cities. Use os nomes de três cidades como chaves em seu dicionário. Crie
# um dicionário com informações sobre cada cidade e inclua o país em que a cidade está localizada, a população
# aproximada e um fato sobre essa cidade. As chaves do dicionário de cada cidade devem ser algo como country,
# population e fact. Apresente o nome de cada cidade e todas as informações que você armazenou sobre ela.

cities = {
    'niterói': {
        'country': 'brasil',
        'population': '500 mil',
        'area': '129,3 Km²',
    },

    'roma': {
        'country': 'itália',
        'population': '2,873 milhões',
        'area': '1.285 Km²',
    },

    'flórida': {
        'country': 'estados unidos',
        'population': '21,14 milhões',
        'area': '170,311 Km²',
    },
}

for citie, citie_info in cities.items():
    print('\n Localizada no(a) ' + citie_info['country'].title() + ', a cidade de(a) ' + citie.title() + ' possui uma população aproximada de ' + citie_info['population'] + ' e um espaço territorial de ' + citie_info['area'] + '.')