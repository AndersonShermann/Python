# Curso intensivo de Python
#
# Exercício 7.3-Peça um número ao usuário e, em seguida, informe se o número é múltiplo de dez ou não.

prompt = 'Digite um número para verificar se é múltiplo de 10 (dez): '

numero = int(input(prompt))
if numero % 10 == 0:
    print('O número ' + str(numero) + ' é divisível por 10.')
else:
    print('O número ' + str(numero) + ' não é divisível por 10.')