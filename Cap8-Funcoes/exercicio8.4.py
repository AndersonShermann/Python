# Curso intensivo de Python
#
# Exercício 8.4-Camisetas grandes: Modifique a função make_shirt() de modo que as camisetas sejam grandes por
# default, com uma mensagem Eu amo Python. Crie uma camiseta grande e outra média com a mensagem default, e
# uma camiseta de qualquer tamanho com uma mensagem diferente.

def make_shirt(texto="I Love Python", tamanho="G"):
    print("\nT-Shirt \nTamanho: " + tamanho + "\nEstampa: " + texto + ".")

make_shirt()
make_shirt(tamanho="M")
make_shirt("Never Give Up", "P")