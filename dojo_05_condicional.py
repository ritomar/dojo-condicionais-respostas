# Exercícios by Nick Parlante (CodingBat)
# Diff 21
# dado um inteiro n retorna a diferença absoluta entre n e 21
# porém se o número for maior que 21 retorna dobro da diferença absoluta
# diff21(19) -> 2
# diff21(25) -> 8
# dica: abs(x) retorna o valor absoluto de x
from Testes import teste, msg_sucesso, msg_inicio


def diff21(n):
    if n < 21:
        return 21 - n
    else:
        return (n - 21) * 2


msg_inicio('Diff 21')
teste(diff21(19), 2)
teste(diff21(10), 11)
teste(diff21(21), 0)
teste(diff21(22), 2)
teste(diff21(25), 8)
teste(diff21(30), 18)
msg_sucesso()
