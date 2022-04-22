# Curso intensivo de Python
#
# Exercício 4.8-Um número elevado a terceira potência é chamado de cubo. Por exemplo o cubo de 2 é escrito 2**3 em
# # python. Crie uma lista dos dez primeiros cubos (isto é, o cubo de cada inteiro de 1 a 10), e utilize um laço for
# # para exibir o valor de cada cubo.

# modelo 01
#
# aoCubo = []
# for value in range(1, 11):
#     value = value**3
#     aoCubo.append(value)
# print(aoCubo)

# modelo 02 (list comprehension)

aoCubo = [value**3 for value in range(1, 11)]
print(aoCubo)
