from math import ceil


def readVector() -> list:
    vector = [int(i) for i in input().split(' ') if i]
    return vector

def semiparticionadoIndiceInpar(vector: list) -> None:
    n = len(vector)
    for i in range(1, ceil(n / 2), 2):
        n1 = vector[i]
        n2 = vector[n - i - 1]
        if n1 > n2:
            hold = n1
            vector[i] = n2
            vector[n - i - 1] = hold

vector = readVector()
semiparticionadoIndiceInpar(vector)
print(*vector)
