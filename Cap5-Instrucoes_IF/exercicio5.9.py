# Curso intensivo de Python
#
# Exercício 5.9-Acrescente um teste if em hello_admin.py para garantir que a lista de usuários não esteja vazia.
#
# ►Se a lista estiver vazia, mostre a mensagem: "Precisamos encontrar alguns usuários"
# ►Remova todos os nomes de usuários de sua lista e certifique-se que a mensagem correta seja exibida.

usuarios = []


if usuarios:
    for usuario in usuarios:
        if usuario == 'admin':
            print('\nOlá ' + usuario.title() + '! Gostaria de ver os relatórios do mês?')
        else:
            print('\nOlá ' + usuario.title() + '. Obrigado por fazer login novamente')
else:
    print('A lista de usuários está vazia.')