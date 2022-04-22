# Curso intensivo de Python
#
# Exercício 4.10-Usando um dos programas que você escreveu neste capítulo, acrescente várias linhas no final do programa
# que façam o seguinte:

numerosImpares = [value for value in range(1, 21, 2)]
print(numerosImpares)

# 1-Exiba a mensagem: "Os três primeiros itens da lista são:". Em seguida use a fatia para percorrer os três primeiros
# itens dessa lista
#
print("Os três primeiros itens da lista são:", numerosImpares[:3], "\n")
#
# 2-Exiba a mensagem: "Os três itens do meio da lista são:". Em seguida use a fatia para percorrer os três itens do
# meio dessa lista.
#
print("Os três itens do meio da lista são:", numerosImpares[4:7], "\n")
#
# 3-Exiba a mensagem: "Os três últimos itens da lista são:" Em seguida use a fatia para percorrer os três ultimos
# itens dessa lista Em seguida use a fatia para percorrer os três primeiros itens dessa lista
#
print("Os três últimos itens dessa lista são:", numerosImpares[-3:], "\n")