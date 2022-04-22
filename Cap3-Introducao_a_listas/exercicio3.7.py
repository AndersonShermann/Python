# Curso intensivo de Python
#
# Exercício 3.7-Você acabou de descobrir que sua nova mesa de jantar não chegará a tempo para o jantar e tem
# espaço para somente dois convidados.
#
# 1-Comece com seu programa do exercício 3.6. Acrescente uma nova linha que mostre uma mensagem informando
# que você pode convidar apenas duas pessoas para o jantar.

convidados = ["Guinet Borges", "Keanu Reeves", "Warren Buffett", "Jorge P. Lemann"]
convidados.insert(0, "John McAfee")
convidados.insert(3, "Tony Stark")
convidados.append("Michael Jackson")

lista_convidados = str(convidados)
mensagem = "Olá " + lista_convidados + ", infelizmente por problemas técnicos, teremos apenas 2 lugares no jantar"
print(mensagem)

# 2-Utilize pop() para remover os convidados de sua lista, um de cada vez, até que apenas dois nomes
# permaneçam em sua lista. Sempre que remover um nome de sua lista, mostre uma mensagem a essa pessoa,
# permitindo que ela saiba que você sente muito por não poder convidá-lo para o jantar.

excluido_1 = convidados.pop()
print("\nOlá " + excluido_1 + " peço desculpas por não poder convidá-lo. Agendaremos uma nova data para nosso jantar.")
excluido_2 = convidados.pop()
print("\nOlá " + excluido_2 + " peço desculpas por não poder convidá-lo. Agendaremos uma nova data para nosso jantar.")
excluido_3 = convidados.pop()
print("\nOlá " + excluido_3 + " peço desculpas por não poder convidá-lo. Agendaremos uma nova data para nosso jantar.")
excluido_4 = convidados.pop()
print("\nOlá " + excluido_4 + " peço desculpas por não poder convidá-lo. Agendaremos uma nova data para nosso jantar.")
excluido_5 = convidados.pop()
print("\nOlá " + excluido_5 + " peço desculpas por não poder convidá-lo. Agendaremos uma nova data para nosso jantar.")

# 3- apresente uma mensagem para cada uma das duas pessoas que continuam na lista, permitindo que elas
# saibam que ainda estão convidadas.

print("\nOlá " + convidados[0] + ", apesar dos imprevistos, sua presença está confirmada para o jantar.")
print("\nOlá " + convidados[1] + ", apesar dos imprevistos, sua presença está confirmada para o jantar.")

#
# 4-Utilize del para remover os dois últimos nomes de sua lista, de modo que você tenha uma lista vazia.
# Mostre sua lista para garantir que você realmente tem uma lista vazia no final do seu programa.

del convidados[1]
del convidados[0]

print(convidados)