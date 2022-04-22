# Curso intensivo de Python
#
# Exercício 6.2-Use um dicionário para armazenar os números favoritos de algumas pessoas. Pense em cinco nomes e
# use-os como chave em seu dicionário. Pense em um número favorito para cada pessoa e armazene cada um como um
# valor em seu dicionário. Exiba o nome de cada pessoa e seu número favorito.

numeros_favoritos = {
    'Anderson': 7,
    'Jackeline': 10,
    'Flávia': 21,
    'Bruna': 25,
    'Shermann': 3,
}
print('\nO número favorito de Anderson é:.........' + str(numeros_favoritos['Anderson']))
print('O número favorito de Jackeline é:........' + str(numeros_favoritos['Jackeline']))
print('O número favorito de Flávia é:...........' + str(numeros_favoritos['Flávia']))
print('O número favorito de Bruna é:............' + str(numeros_favoritos['Bruna']))
print('O número favorito de Shermann é:.........' + str(numeros_favoritos['Shermann']))
