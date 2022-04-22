# Curso intensivo de Python
#
# Exercício 4.4-Crie uma lista de números de um a um milhão e então use um laço for para exibir os números.

# modelo 01

numeros = []
for value in range(1, 1000001):
    numeros.append(value)#cria a lista de 1 a 100000
for value in numeros: #laço para exibir a lista e exibir os numeros
    print(value)

# modelo 02 (list comprehension)
#
numeros = [value for value in range (1, 1000001)]
for value in numeros:
    print(value)