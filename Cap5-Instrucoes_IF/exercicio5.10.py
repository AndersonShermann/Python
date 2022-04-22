# Curso intensivo de Python
#
# Exercício 5.10-Faça o seguinte para criar um programa que simule o modo como os sites garantem que todos tenham um
# nome de usuário único.
#
# ►Crie uma lista chamada current_users com cinco ou mais nomes de usuários.
# ►Crie outra lista chamada new_users com cinco nomes de usuários. Garanta que um ou dois dos novos usuários também
# estejam na lista current_users.
# ►Percorra a lista new_users com um laço para ver se cada novo nome de usuários ja foi usado. Em caso afirmativo,
# mostre uma mensagem informando que a pessoa deverá fornecer um novo nome. Se um nome de usuário não foi usado,
# apresente uma mensagem dizendo que o nome do usuário está disponível.
# ►Certifique-se de que sua comparação não levará em contas a diferença entre letras maiúsculas e minúsculas. Se
# 'John' ja foi usado, 'JOHN' não deverá ser aceito.

current_users = ['admin', 'anderson', 'lucas', 'jackeline', 'nathalia']
new_users = ['fernanda', 'Anderson', 'paula', 'ana', 'nathalia']

for new_user in new_users:
    if new_user.lower() in current_users:
        print('\nO login ' + new_user + ' não está disponível.')
    else:
        print('\nO login ' + new_user + ' está disponível.')


