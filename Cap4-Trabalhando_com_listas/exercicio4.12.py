# Curso intensivo de Python
#
# Exercício 4.12-Todas as versões de food.py nesta seção evitaram usar laços for para fazer a exibição a fim de
# economizar espaço. Escolha uma versão de foods.py e escreva dois laços for para exibir cada lista de comidas.

my_foods = ["pizza", "falafel", "carrot cake"]
friend_food = my_foods[:]

friend_food.append("maça")
my_foods.append("laranja")

print("\nMinhas comidas favoritas são:")
for food in friend_food:
    print(food)

print("\nAs comidas favoritas do meu amigo são:")
for food in my_foods:
    print(food)