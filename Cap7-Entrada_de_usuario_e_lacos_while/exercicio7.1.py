# Curso intensivo de Python
#
# Exercício 7.1-Escreva um programa que pergunte ao usuário qual tipo de carro ele gostaria de alugar. Mostre uma
# # mensagem sobre esse carro, por exemplo, “Deixe-me ver se consigo um Subaru para você.”

prompt = 'Informe o modelo do carro: '

reserva = input(prompt)
print('Deixe-me ver se consigo um ' + reserva.title() + ' para você.')