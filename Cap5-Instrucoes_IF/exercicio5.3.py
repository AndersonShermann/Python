# Curso intensivo de Python
#
# Exercício 5.3-Suponha que um alienígena acabou de ser atingido em um jogo. Crie uma variável chamada alien_color
# e atribua-lhe um valor igual a 'green', 'yellow' ou 'red'.
#
# ► escreva uma instrução if para testar se a cor do alienígena é verde. Se for, mostre uma mensagem informando que
# o jogador acabou de ganhar cinco pontos.

alien_color = 'green'

if alien_color == 'green':
    print('Parabéns,você ganhou 5 pontos.')

# ► Escreva uma versão desse programa em que o teste if passe e outro em que ele falhe. (a versão que falha nao
# terá saida.)

if alien_color == 'red': #aqui o código não apresenta menssagem pois o teste falhou e nao tem instrução else
    print('Que pena você errou.')