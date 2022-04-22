# Curso intensivo de Python
#
# Exercício 6.1-Use um dicionario para armazenar informações de uma pessoa que você conheça. Armazene seu primeiro
# nome, o sobrenome, a idade, a cidade em que ela vive. Você deverá ter chaves como first_name, last_name, age.
# city. Mostre cada informação armazenada no seu dicionário.

dados_pessoais = {
    'first_name': 'anderson',
    'last_name': 'oliveira',
    'age': 29,
    'city': 'niterói',
}
print("\nPrimeiro Nome: " + dados_pessoais['first_name'].title())
print("Último nome: " + dados_pessoais['last_name'].title())
print("Idade: " + str(dados_pessoais['age']))
print("Cidade: " + dados_pessoais['city'].title())