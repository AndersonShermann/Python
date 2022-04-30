# Curso intensivo de Python
#
# Exercício 7.5-Um cinema cobra preços diferentes para os ingressos de acordo com a idade de uma pessoa. Se uma
# pessoa tiver menos de 3 anos de idade, o ingresso será gratuito; se tiver entre 3 e 12 anos, o ingresso custará
# 10 dólares; se tiver mais de 12 anos, o ingresso custará 15 dólares. Escreva um laço em que você pergunte a idade
# aos usuários e, então, informe-lhes o preço do ingresso do cinema.

prompt = 'Para verificar o valor do ingresso, informe sua idade: '
prompt += '\nDigite "quit" para sair.'

active = True

idade = input(prompt)

while active:
    if idade == 'quit':
        active = False
    elif int(idade) <= 3:
        print('Ingresso gratuito para crianças de até 3 anos de idade.')
    elif int(idade) <= 12:
        print('Valor do ingresso: $10.')
    else:
        print('Valor do ingresso: $15.')
    break