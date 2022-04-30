# Curso intensivo de Python
#
# Exercício 7.2-Escreva um programa que pergunte ao usuário quantas pessoas estão em seu grupo para jantar. Se a
# resposta for maior que oito, exiba uma mensagem dizendo que eles deverão esperar uma mesa. Caso contrário, informe
# que sua mesa está pronta.

prompt = 'Por gentileza, informe o número de pessoas para a reserva: '

reserva = int(input(prompt))
if reserva > 8:
    print('No momento não temos uma mesa com ' + str(reserva) + ' lugares disponível. Pedimos por gentileza que aguardem.')
else:
    print('Sua mesa está pronta. Bom apetite.')
