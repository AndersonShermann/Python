# Curso intensivo de Python
#
# Exercício 4.2-Pense em pelo menos três animais diferentes que tenham uma característica em comum. Armazene o nome
# desses animais em uma lista, e então utilize o laço for para exibir o nome de cada animal.
#
# 1-Modifique seu programa para exibir uma frase sobre cada animal, por exemplo: "Um cachorro seria um ótimo animal de
# estimação.".

animais =["leão", "cavalo", "águia"]
for animais in animais:
    print(animais.title() + " é um animal incrível.")

# 2-Acrescente uma linha no final do programa informando o que esses animais tem em comum. Você poderia exibir uma frase
# como: "Qualquer um desses animais seria um ótimo animal de estimação.".

print("\nQualquer um desses animais é um excelente companheiro de estimação.")