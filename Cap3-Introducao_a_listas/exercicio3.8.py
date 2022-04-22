# Curso intensivo de Python
#
# Exercício 3.8-Pense em pelo menos cinco lugares do mundo que você gostaria de visitar.
#
# 1-Armazene as localidades em uma lista. Certifique-se de que a lista não esteja em ordem alfabética.

locais = ["egito", "inglaterra", "rússia", "holanda", "alaska"]

# 2-Exiba sua lista na ordem original. Não se preocupe em exibir a lista de forma elegante; basta exibi-la
# como uma lista python pura.

print(locais)

# 3-Utilize sorted() para exibir sua lista em ordem alfabética, sem modificar a lista propriamente dita.

print(sorted(locais))

# 4-Mostre que sua lista manteve sua ordem original exibindo-a.

print(locais)

# 5-Utilize sorted()para exibir sua lista em ordem alfabética inversa sem alterar a ordem da lista original.

print(sorted(locais, reverse=True))

# 6-Mostre que sua lista manteve sua ordem original exibindo-a novamente.

print(locais)

# 7-Utilize reverse() para mudar a ordem de sua lista. Exiba a lista para mostrar que sua ordem mudou.

locais.reverse()
print(locais)

# 8-Utilize reverse() para mudar a ordem de sua lista novamente. Exiba a lista para mostrar que ela voltou
# a sua ordem original.

locais.reverse()
print(locais)

# 9-Utilize sort() para mudar sua lista de modo que ela seja armazenada em ordem alfabética. Exiba a lista
# para mostrar que sua ordem mudou.

locais.sort()
print(locais)

# 10-Utilize sort() para mudar sua lista de modo que ela seja armazenada em ordem alfabética inversa. Exiba
# a lista para mostrar que sua ordem mudou.

locais.sort(reverse=True)
print(locais)