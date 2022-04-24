# Curso intensivo de Python
#
# Exercício 6.6-Utilize o código em favorite_languages.py (página 150).
#
# • Crie uma lista de pessoas que devam participar da enquete sobre linguagem favorita. Inclua alguns nomes que
# já estejam no dicionário e outros que não estão.
#
# • Percorra a lista de pessoas que devem participar da enquete. Se elas já tiverem respondido à enquete, mostre
# uma mensagem agradecendo-lhes por responder. Se ainda não participaram da enquete, apresente uma mensagem
# convidando-as a responder.

#Exercício da pag. 150

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

enquete = ['jen', 'phil', 'jack', 'will']

for name in enquete:
    if name in favorite_languages.keys():
        print('\nOlá ' + name.title() + '. Agradecemos por ter participado de nossa pesquisa. ')
    else:
        print('\nOlá ' + name.title() + '. Gostaria de participar da nossa pesquisa?')

