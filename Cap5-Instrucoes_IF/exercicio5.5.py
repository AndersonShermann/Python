# Curso intensivo de Python
#
# Exercício 5.5-Transforme sua cadeia if-else do exercício 5.4 em uma cadeia if-else-elif.
#
# ► Se o alienígena for verde, mostre uma mensagem informando que o jogador ganhou cinco pontos.
# ► Se o alienígena for amarelo, mostre uma mensagem informando que o jogador ganhou dez pontos.
# ► Se o alienígena for vermelho, mostre uma mensagem informando que o jogador ganhou quinze pontos.
# ► Escreva três versões desse programa garantindo que cada mensagem seja exibida para a cor apropriada do alienígena.

alien_color = 'red'

if alien_color == 'green':
    print('Você ganhou 5 pontos.')
elif alien_color == 'yellow':
    print('Você ganhou 10 pontos.')
else:
    print('Você ganhou 15 pontos.')

alien_color = 'yellow'

if alien_color == 'green':
    print('Você ganhou 5 pontos.')
elif alien_color == 'yellow':
    print('Você ganhou 10 pontos.')
else:
    print('Você ganhou 15 pontos.')

alien_color = 'green'

if alien_color == 'green':
    print('Você ganhou 5 pontos.')
elif alien_color == 'yellow':
    print('Você ganhou 10 pontos.')
else:
    print('Você ganhou 15 pontos.')