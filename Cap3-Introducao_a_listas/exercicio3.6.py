# Curso intensivo de Python
#
# Exercício 3.6-Você acabou de encontrar uma mesa de jantar maior, portanto agora tem mais espaço disponível.
# Pense em mais três convidados para o jantar
#
# 1-Comece com o programa do exercício 3.4 ou do exercício 3.5. Acrescente uma instrução print no final de
# seu programa informando às pessoas que você encontrou uma mesa de jantar maior.

convidados = ["Guinet Borges", "Keanu Reeves", "Warren Buffett", "Jorge P. Lemann"]

print("\nOlá " + convidados[0] + " gostaria de informá-lo que consegui uma mesa de jantar maior, por isso teremos mais convidados em nosso jantar.")
print("\nOlá " + convidados[1] + " gostaria de informá-lo que consegui uma mesa de jantar maior, por isso teremos mais convidados em nosso jantar.")
print("\nOlá " + convidados[2] + " gostaria de informá-lo que consegui uma mesa de jantar maior, por isso teremos mais convidados em nosso jantar.")
print("\nOlá " + convidados[3] + " gostaria de informá-lo que consegui uma mesa de jantar maior, por isso teremos mais convidados em nosso jantar.")

# 2-Utilize insert() para adicionar um novo convidado no início de sua lista.

convidados.insert(0, "John McAfee")
print(convidados)

# 3-Utilize insert() para adicionar um novo convidado no meio de sua lista.

convidados.insert(3, "Tony Stark")
print(convidados)

# 4-Utilize append() para adicionar um novo convidado no final de sua lista.

convidados.append("Michael Jackson")
print(convidados)
