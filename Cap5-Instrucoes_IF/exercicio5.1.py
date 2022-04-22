# Curso intensivo de Python
#
# Exercício 5.1-Escreva uma série de testes condicionais.Exiba uma frase que descreva o teste e o resultado previsto
# para cada um. Seu código deverá ser semelhante a:

# ====================
# car = "subaru"
# print("Is car=='subaru'? I predict True")
# print(car == "subaru")
#
# print("\nIs car=='audi'? I predict False")
# print(car == "audi")
# ====================

# ►Observe atentamente seus resultados e certifique-se de que compreende por que cada linha é avaliada como True
# ou False.
# ►Crie pelo menos dez testes. Tenha no minimo cinco testes avaliados como True e cinco avaliados como False.

anime = "Hunter x Hunter"
print("\nIs anime == 'hunter x hunter'? I predict False")
print(anime == "hunter x hunter")

print("\nIs anime != 'Hunter x hunter'? I predict True.")
print(anime != "Hunter x hunter")

color = "red"
print("\nIs color.title() == 'Red'? I predict True.")
print(color.title() == "Red")

print("\nIs color.upper() != 'RED' I Predict False")
print(color.upper() != "RED")

numero = "549"
print("\nIs numero > '386'? I predict True.")
print(numero > '386')

print("\nIs color == 'red' and numero == '549'? I Predict True.")
print(color == 'red' and numero == '549')

print("\nIs anime.lower() == 'hunter x hunter' and color.title() == 'Red'? I Predict True.")
print(anime.lower() == 'hunter x hunter' and color.title() == 'Red')

idade = 18
print("\nIs anime == 'Hunter x Hunter' and idade < 18? I Predict False")
print(anime == 'Hunter x Hunter' and idade < 18)

print("\nIs idade > '18' or color == 'Blue'? I predict False.")
print(idade > 18 or color == 'Blue')

print("\nIs anime == 'Hunter x hunter or idade != 18 ? I predict False.")
print(anime == 'Hunter x hunter' or idade != 18)
