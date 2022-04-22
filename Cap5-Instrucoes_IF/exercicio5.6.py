# Curso intensivo de Python
#
# Exercício 5.6- Escreva uma cadeia if-else-elif que determine o estágio da vida de uma pessoa. Defina um valor
# para a variável age e então:
#
# ► Se a pessoa tiver menos de 2 anos de idade, mostre uma mensagem dizendo que ela é um bebê.
# ► Se a pessoa tiver pelo menos 2 anos, mas menos de 4, mostre uma mensagem dizendo que ela é uma criança.
# ► Se a pessoa tiver pelo menos 4 anos, mas nenos de 13, mostra uma mensagem dizendo que ele(a) é um(a) garoto(a).
# ► Se a pessoa tiver pelo menos 13 anos, mas nenos de 20, mostra uma mensagem dizendo que ele(a) é um(a) adolescente.
# ► Se a pessoa tiver pelo menos 20 anos, mas nenos de 65, mostra uma mensagem dizendo que ele(a) é um(a) adulto(a).
# ► Se a pessoa tiver 65 anos ou mais, mostra uma mensagem dizendo que ela é uma pessoa idosa.

age = 29

if age < 2:
    print('Você é um bebê.')
elif age < 4:
    print('Você é um criança.')
elif age < 13:
    print('Você é um(a) garoto(a).')
elif age < 20:
    print('Você é um adolescente.')
elif age < 65:
    print('Você é  um adulto.')
else:
    print('Você é um(a) idoso(a).')
