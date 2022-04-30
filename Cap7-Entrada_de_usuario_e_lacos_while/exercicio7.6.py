# Curso intensivo de Python
#
# Exercício 7.6-Escreva versões diferentes do Exercício 7.4 ou do Exercício 7.5 que faça o seguinte, pelo menos uma
# vez:
# • use um teste condicional na instrução while para encerrar o laço;
# • use uma variável active para controlar o tempo que o laço executará;
# • use uma instrução break para sair do laço quando o usuário fornecer o valor 'quit'.

"""Saida para o usuário"""
prompt = 'Informe um item que deseja adicionar à sua lista de compras: '
prompt += '\nDigite "v" para verificar a lista ou "q" para encerrar.'

"""Variável para controlar o tempo de execução do laço"""
active = True

"""Lista para armazenar os itens"""
lista_de_compras = []

"""Laço para verificar entrada do usuário"""
while active:
    """Entrada do usuário"""
    item = input(prompt)
    """Verifica se o usuário deseja encerrar o programa, exibir a lista ou continuar adicionando itens na lista"""
    if item == 'q':
        active = False
        break
    elif item == 'v':
        for value in lista_de_compras:
            print('\t' + value)
    else:
        lista_de_compras.append(item)
        print('\nO item ' + item + ' foi adicionado a lista.')