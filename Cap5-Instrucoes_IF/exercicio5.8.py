# Curso intensivo de Python
#
# Exercício 5.8-Crie uma lista com cinco ou mais nomes de usuários, incluindo o nome 'admin'. Suponha que você está
# escrevendo um código que exibirá uma saudação à cada usuário depois que eles fizerem login em um site. Percorra a
# lista com um laço e mostre uma saudação para cada usuário:
#
# ►Se o nome do usuário for 'admin', mostre uma saudação especial, por exemplo "Olá admin gostaria de ver um relatório
# de status?
# ►Caso contrário, mostre uma saudação genérica, como: "Olá Eric, obrigado por fazer login novamente.

usuarios = ['admin', 'anderson', 'lucas', 'jackeline', 'nathalia']
for usuario in usuarios:
    if usuario == 'admin':
        print('\nOlá ' + usuario.title() + '! Gostaria de ver os relatórios do mês?')
    else:
        print('\n0Olá ' + usuario.title() + '. Obrigado por fazer login novamente')