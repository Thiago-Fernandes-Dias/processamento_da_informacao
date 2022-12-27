inteiroDado = 3


def calcula_menor(e, f):
    return ((e + f) - abs(e - f)) / 2


n1 = int(input())
n2 = int(input())
entradaMenor = calcula_menor(n1, n2)
menorNumero = calcula_menor(inteiroDado, entradaMenor)

print(f'O menor inteiro: {menorNumero:.0f}')