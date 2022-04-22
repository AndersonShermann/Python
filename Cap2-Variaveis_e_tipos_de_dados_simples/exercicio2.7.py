# Curso intensivo de Python
#
# Exercício 2.7-Armazene o nome de uma pessoa e inclua alguns caracteres em branco no início e no final do
# nome. Lembre-se de usar cada combinação de caracteres "\t" e "\n" pelo menos uma vez. Exiba o nome uma
# vez, de modo que os espaços em branco em torno do nome sejam mostrados. Em seguida exiba o nome usando
# cada uma das três funções de remoção de espaços.

nome = "\tAnderson\n" #\t tabulação; \n quebra de linha
print(nome) #string com tabulação e quebra de linha
print(nome.strip()) #string sem parágrafo e quebra de linha
print(nome.rstrip()) #string sem quebra de linha
print(nome.lstrip()) #string sem parágrafo
