# Curso intensivo de Python
#
# Exercício 7.8-Crie uma lista chamada sandwich_orders e a preencha com os nomes de vários sanduíches. Em seguida,
# crie uma lista vazia chamada finished_sandwiches. Percorra a lista de pedidos de sanduíches com um laço e mostre
# uma mensagem para cada pedido, por exemplo, Preparei seu sanduíche de atum. À medida que cada sanduíche for
# preparado, transfira-o para a lista de sanduíches prontos. Depois que todos os sanduíches estiverem prontos,
# mostre uma mensagem que liste cada sanduíche preparado.

sandwich_orders = ['presunto', 'picanha', 'provolone', 'churrasco', 'atum']
finished_sandwich = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print('O sanduíche de ' + current_sandwich + ' está sendo preparado.')
    finished_sandwich.append(current_sandwich)

print('\nSanduíches prontos: ')
for value in finished_sandwich:
    print('\t' + value.title())