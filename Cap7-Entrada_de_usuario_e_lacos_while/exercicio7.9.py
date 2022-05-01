# Curso intensivo de Python
#
# Exercício 7.9-Usando a lista sandwich_orders do Exercício 7.8, garanta que o sanduíche de 'pastrami' apareça na
# lista pelo menos três vezes. Acrescente um código próximo ao início de seu programa para exibir uma mensagem
# informando que a lanchonete está sem pastrami e, então, use um laço while para remover todas as ocorrências de
# 'pastrami' de sandwich_orders. Garanta que nenhum sanduíche de pastrami acabe em finished_sandwiches.

sandwich_orders = ['presunto', 'pastrami', 'picanha', 'pastrami', 'provolone', 'pastrami', 'churrasco', 'atum']
finished_sandwich = []

print('\nPrezado cliente, no momento estamos sem pastrami em nosso restaurante.')
while sandwich_orders:
    if 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')
    else:
        current_sandwich = sandwich_orders.pop()
        finished_sandwich.append(current_sandwich)

for value in finished_sandwich:
    print('\t' + value.title())