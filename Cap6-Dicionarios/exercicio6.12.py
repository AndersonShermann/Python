# Curso intensivo de Python
#
# Exercício 6.12-Estamos trabalhando agora com exemplos complexos o bastante para poderem ser estendidos de várias
# maneiras. Use um dos programas de exemplo deste capítulo e estenda-o acrescentando novas chaves e valores,
# alterando o contexto do programa ou melhorando a formatação da saída.


users = {
    'user_0': {
        'login': 'admin',
        'password': 123456,
        'email': 'admin@gmail.com',
    },

    'user_1': {
        'login': 'anderson',
        'password': 123456,
        'email': 'anderson@gmail.com',
    },

    'user_2': {
        'login': 'shermann',
        'password': 123456,
        'email': 'shermann@gmail.com',
    },
}
for user, user_info in users.items():
    print('\n Dados do ' + user + ': ')
    for key, value in user_info.items():
        print('\t' + key + ': ' + str(value))
