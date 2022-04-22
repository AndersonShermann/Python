# Curso intensivo de Python
#
# Exercício 4.6-Use o terceiro argumento da função range() para criar uma lista de números ímpares de 1 a 20. Utilize
# um laço for para exibir os números.

# # modelo 01
# numerosImpares = []
# for value in range(1, 21, 2):
#     numerosImpares.append(value)
# print(numerosImpares)

# # modelo 02 (list comprehension)
numerosImpares = [value for value in range(1, 21, 2)]
print(numerosImpares)