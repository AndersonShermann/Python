# Curso intensivo de Python
#
# Exercício 7.7-Escreva um laço que nunca termine e execute-o. (Para encerrar o laço, pressione CTRL-C ou feche a
# janela que está exibindo a saída.)

active = True
contagem_infinita = 0

while active:
    contagem_infinita = contagem_infinita + 1
    print(contagem_infinita)