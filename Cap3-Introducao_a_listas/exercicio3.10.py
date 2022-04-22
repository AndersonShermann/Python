# Curso intensivo de Python
#
# Exercício 3.10-Pensa em algo que poderia armazenar em uma lista. Por exemplo, voce poderia criar uma lista
# de montanhas, rios, países, cidades, idiomas ou qualquer outro item que quiser.Escreva um programa que crie
# uma lista contendo esses itens e então utilize cada função apresentada neste capítulo pelo menos uma vez.

animes = ["Hunter X Hunter", "Naruto", "Death Note", "Bleach", "Attack on Titan", "Fairy Tail"]
series = ["Supernatural", "Vikings", "Lucifer", "Brooklyn 99", "O Justiceiro", "Ragnarok"]
personagens = ["Coringa", "Orochimaru", "Gin Icimaru", "Hisoka", "Levi", "Neo", "Ragnar", "Egbert", "Thor", "loki"]
filmes = ["B-13U", "Vingadores Ultimato", "Intocáveis", "Titanic", "Matrix", "Harry Potter"]

#.appended: adiciona um elemento á direita da lista

animes.append("Animatrix")
print(animes)

#.insert: insere um elemento na lista na posição indicada (posição + elemento)

series.insert(2, "Game of Thrones")
print(series)

#del: exclui um elemento da lista de forma permanente

del personagens[4]
print(personagens)

#.pop: remove o ultimo elemento de uma lista, se nao for indicada posição e mantém este elemento disponível para ser usado
#posteriormente

filmes.pop() #não inticando posição do elemento
print(filmes)
removeFilme2 = filmes.pop(2) #inticando posição do elemento.
print(removeFilme2) #elemento removido com o .pop() e armazenado em uma variável

#.remove: remove um elemento quando o valor deste é conhecido

animes.remove("Naruto")
print(animes)

#.sort: organiza os elementos de uma lista em ordem alfabetica de forma permanente

series.sort()
print(series)
series.sort(reverse=True) #indicar reverse=True retorna a ordem alfabetica inversa de forma permanente
print(series)

#.sorted: organiza os elementos de uma lista em ordem albabética de forma temporária

print(sorted(series))
print(series) #lista na mesma ordem anterior
print(sorted(personagens, reverse=True)) #organiza os elementos de forma temporaria, em ordem alfabetica reversa
print(personagens)

#.reverse: inverte a posição da lista de forma permanente

filmes.reverse()
print(filmes)
filmes.reverse() #usar .reverse novamente faz a lista voltar a posição inicial
print(filmes)

#.len: calcula o número de elementos dentro de uma lista

print(len(animes))
print(len(series))
print(len(personagens))
print(len(filmes))
