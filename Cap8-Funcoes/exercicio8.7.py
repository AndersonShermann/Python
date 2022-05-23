# Curso intensivo de Python
#
# Exercício 8.7-Álbum: Escreva uma função chamada make_album() que construa um dicionário descrevendo um
# álbum musical. A função deve aceitar o nome de um artista e o título de um álbum e deve devolver um
# dicionário contendo essas duas informações. Use a função para criar três dicionários que representem
# álbuns diferentes. Apresente cada valor devolvido para mostrar que os dicionários estão armazenando as
# informações do álbum corretamente. Acrescente um parâmetro opcional em make_album() que permita armazenar
# o número de faixas em um álbum. Se a linha que fizer a chamada incluir um valor para o número de faixas,
# acrescente esse valor ao dicionário do álbum. Faça pelo menos uma nova chamada da função incluindo o
# número de faixas em um álbum.

def make_album(nome, titulo, faixas=""):
    """Devolve um dicionário com informações sobre um album musical"""
    album_musical = {
        "nome": nome,
        "titulo": titulo,
    }
    if faixas:
        album_musical["faixas"] = faixas
    return album_musical

album_1 = make_album("System of a Down", "Hipnotize")
print(album_1)

album_2 = make_album("System os a Down", "Steal this album!")
print(album_2)

album_3 = make_album("Foo Fighters", "Echoes, Silence, Patience & Grace")
print(album_3)

album_4 = make_album("Iron Maiden", "Fear of the Dark", 12)
print(album_4)