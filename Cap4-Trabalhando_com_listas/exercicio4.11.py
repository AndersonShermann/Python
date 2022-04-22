# Curso intensivo de Python
#
# Exercício 4.11-Comece com o seu programa do exercício 4.1. Faça uma cópia da lista de pizzas e chame de friend_pizzas
# Então faça o seguinte:
#
pizzasFavoritas = ["Lombo Canadense", "Peperoni com Cream Cheese", "Calabresa"]
friendPizzas = pizzasFavoritas[:]

# 1-Adicione uma nova pizza a lista original
#
pizzasFavoritas.append("Portuguesa")
#
# 2-Adicione uma pizza diferente a lista friend_pizzas
#
friendPizzas.append("Bacon com Alho")
#
# 3-Prove que você tem duas listas diferentes. Exiba a mensagem: "Minhas pizzas favoritas são:", em seguida use o laço
# for para exibir a primeira lista.Exiba a mensagem: "As pizzas favoritas do meu amigo são:, em seguida use o laço for
# para exibir a segunda lista. Certifique-se de que cada pizza nova esteja armazenada na lista apropriada.
#
print("\nMinhas pizzas favoritas são:")
for value in pizzasFavoritas:
    print(value)

print("\nAs pizzas favoritas do meu amigo são:")
for value in friendPizzas:
    print(value)