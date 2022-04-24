# Curso intensivo de Python
#
# Exercício 6.7-Comece com o programa que você escreveu no Exercício 6.1 (página 147). Crie dois novos dicionários
# que representem pessoas diferentes e armazene os três dicionários em uma lista chamada people. Percorra sua lista
# de pessoas com um laço. À medida que percorrer a lista, apresente tudo que você sabe sobre cada pessoa.

dados_pessoais_1 = {
    'first_name': 'anderson',
    'last_name': 'oliveira',
    'age': 29,
    'city': 'niterói',
}
dados_pessoais_2 = {
    'first_name': 'jackeline',
    'last_name': 'nascimento',
    'age': 33,
    'city': 'rio das ostras',
}
dados_pessoais_3 = {
    'first_name': 'junior',
    'last_name': 'pardini',
    'age': 40,
    'city': 'são gonçalo',
}
peoples = [dados_pessoais_1, dados_pessoais_2, dados_pessoais_3]

for dados_pessoais in peoples:
    print(
        '\n Nome: ' + dados_pessoais['first_name'].title(),
        '\n Sobrenome: ' + dados_pessoais['last_name'].title(),
        '\n Idade: ' + str(dados_pessoais['age']),
        '\n Cidade: ' + dados_pessoais['city'].title()
    )