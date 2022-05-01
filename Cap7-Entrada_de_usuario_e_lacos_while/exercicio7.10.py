# Curso intensivo de Python
#
# Exercício 7.10-Escreva um programa que faça uma enquete sobre as férias dos sonhos dos usuários. Escreva um
# prompt semelhante a este: Se pudesse visitar um lugar do mundo, para onde você iria? Inclua um bloco de código
# que apresente os resultados da enquete.

ferias_desejadas = {}

active = True

while active:
    nome = input('\nInforme o seu nome: ')
    resposta = input('Se pudesse visitar um lugar do mundo, para onde você iria? ')
    ferias_desejadas[nome] = resposta

    repeat = input('Gostaria de continuar respondendo (yes/no)?')
    if repeat == "no":
        active = False

print('Resultado: \n')
for nome, resposta in ferias_desejadas.items():
    print(nome.title() + ': ' + resposta.title())
