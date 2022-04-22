# Curso intensivo de Python
#
# Exercício 3.5-Você acabou de saber que um de seus convidados não poderá comparecer ao jantar, portanto
# será necessário enviar um novo conjunto de convites. Você deverá pensar em outra pessoa para convidar.
#
# 1-Comece com seu programa do exercício 3.4. Acrescente uma instrução print no final de seu programa,
# especificando o nome do convidado que não poderá comparecer.

convidados = ["Guinet Borges", "Keanu Reeves", "Warren Buffett", "Jorge P. Lemann"]

print("\nOlá " + convidados[0] + ", como você está? Gostaria de convida-lo para un jantar este final de semana.")
print("\nOlá " + convidados[1] + ", como você está? Gostaria de convida-lo para un jantar este final de semana.")
print("\nOlá " + convidados[2] + ", como você está? Gostaria de convida-lo para un jantar este final de semana.")
print("\nOlá " + convidados[3] + ", como você está? Gostaria de convida-lo para un jantar este final de semana.")

print(convidados[1] + " não comparecerá no jantar")

# 2-Modifique sua lista, substituindo o nome do convidado que não poderá comparecer pelo nome da nova pessoa
# que você está convidando.

convidados[1] = "Vladimir Putin"

# 3-Exiba um segundo conjunto de mensagens com o convite, uma para cada pessoa que continua presente em
# sua lista.

print("\nOlá " + convidados[0] + ", sua presença está confirmada para o jantar neste final de semana")
print("\nOlá " + convidados[1] + ", sua presença está confirmada para o jantar neste final de semana")
print("\nOlá " + convidados[2] + ", sua presença está confirmada para o jantar neste final de semana")
print("\nOlá " + convidados[3] + ", sua presença está confirmada para o jantar neste final de semana")
