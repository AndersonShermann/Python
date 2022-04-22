# Curso intensivo de Python
#
# Exercício 4.13-Um restaurante do tipo buffet oferece apenas cinco tipos básicos de comida. Pense em cinco
# pratos simples e armazene-os em uma tupla.
#
pratos = ("Bife de panela", "Frango à milanesa", "Lasanha", "Strognoff", "Filé de tilápia\n")

# 1-Use um laço for para exibir cada prato oferecido pelo restaurante
#
for value in pratos:
    print(value)

# 2-Tente modificar um dos itens e certifique-se de que Python rejeita a mudança.
#
# pratos[0] = "Ovo"

# 3-O restaurante muda seu cardápio, substituindo dois dos itens com pratos diferentes. Acrescente um bloco
# de código que reescreva a tupla e, em seguida, use um laço for para exibir cada um dos itens do cardápio
# revisado.

pratos = ("Bife de panela", "Frango à milanesa", "Lasanha", "Escondidinho", "Filé de frango")
for value in pratos:
    print(value)