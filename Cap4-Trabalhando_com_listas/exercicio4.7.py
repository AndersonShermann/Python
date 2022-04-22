# Curso intensivo de Python
#
# Exercício 4.7-Crie uma lista de múltiplos de três de 3 a 30. Use um laço for para exibir os números da sua lista.

# # modelo 01
#
# multiplosDeTres = []
# for value in range(3, 31):
#     value = value*3
#     multiplosDeTres.append(value)
# print(multiplosDeTres)

# # modelo 02 (list comprehension)
#
multiplosDeTres = [value*3 for value in range(3, 31)]
print(multiplosDeTres)


