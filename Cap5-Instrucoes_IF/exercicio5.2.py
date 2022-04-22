# Curso intensivo de Python
#
# Exercício 5.2-Você não precisa limitar o numero de testes que criar em dez. Se quiser testar mais comparações,
# escreva outros testes e acrescente-os em condicional_tests.py. Tenha pelo menos um resultado True e um False para
# cada um dos casos a seguir:

animes = ['Naruto', 'Bleach', 'Death Note']
series = ['Sobrenatural', 'Game Of Thrones', 'Gotham']
numeros = [2, 4, 8, 16, 32]

# ►teste de igualdade e de não igual dade de strings
print("anime[1].title == 'Bleach'? I predict True")
print(animes[1].title() == 'Bleach')
print("\nanimes[2] != 'Death note'? I predict False.")
print(animes[2] != 'Death Note')

# ►testes usando a função lower()
print("\nseries[1].lower == 'sobrenatural'? I predict False.")
print(series[1].lower() == 'sobrenatural')
print("\nseries[2].lower == 'gotham'? I predict True.")
print(series[2].lower() == 'gotham')

# ►Testes numéricos que envolvam igualdade e não igualdade, maior e menor que, maior ou igual a e menor ou igual a.
print("\nnumeros[1] == numero[0]*2? I predict True.")
print(numeros[1] == numeros[0]*2)
print("\nnumeros[3] != 16? I Predict False")
print(numeros[3] != 16)
print("\nnumeros[3] > numeros[4]? I predict False")
print(numeros[3] > numeros[4])
print("\nnumeros[2]*3 < numeros[4]? I predict True")
print(numeros[2]*3 < numeros[4])
print("\nnumeros[2] >= numeros[1]*2? I predict True")
print(numeros[2] >= numeros[1]*2)
print("\nnumeros[4] <= numeros[3]/3? I predict False")
print(numeros[4] <= numeros[3]/3)

# ►testes usando as palavras reservadas and e or

print("\nanimes[0] == 'Naruto' or series[0] == 'Gotham'? I predict True.")
print(animes[0] == 'Naruto' or series[0] == 'Gotham')
print("\nanimes[1].lower != 'bleach' and numeros[1] == 2? I predict False")
print(animes[1].lower != 'bleach' and numeros[1] == 2)

# ►testes para verificar se um item está em uma lista
print("\nNaruto in animes? I predict True")
print("Naruto" in animes)
print("\nMr. Robot in series? I predict False")
print('Mr. Robot' in series)

# ►testes para verificar se um item não está em uma lista
print("\n4 not numeros? I predict False")
print(4 not in numeros)