# Curso intensivo de Python
#
# Exercício 7.4-Escreva um laço que peça ao usuário para fornecer uma série de ingredientes para uma pizza até que
# o valor 'quit' seja fornecido. À medida que cada ingrediente é especificado, apresente uma mensagem informando
# que você acrescentará esse ingrediente à pizza.

prompt = 'Informe os ingredientes da pizza: '
prompt += '\nPara sair digite "quit".'

active = True

while active:
    ingrediente = input(prompt)
    if ingrediente == 'quit':
        active = False
    else:
        print('\n' + ingrediente.title() + ' adicionado a lista de pedidos.')