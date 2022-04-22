# Curso intensivo de Python
#
# Exercício 4.5-Crie uma lista de números de um a um milhão e em seguida, use min() e max() para garantir que sua lista
# realmente começa em um e termina em um milhão. Além disse, use a função sum() para ver a rapidez com que python é
# capaz de somar um milhão de números.

# # modelo 01
#
# numeros = []
# for value in range(1, 1000001):
#     numeros.append(value)
# print(min(numeros))
# print(max(numeros))
# print(sum(numeros))

# # modelo 02 (list comprehension)
#
numeros = [value for value in range(1, 1000001)]
print("\nO menor número da lista é: ", min(numeros),
      "\nO maior número da lista é: ", max(numeros),
      "\nA soma de todos os números da lista é: ", sum(numeros))
