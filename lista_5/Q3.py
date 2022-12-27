def readVetor():
    return [float(i) for i in input().split(' ') if i]


def escalarProduct(v1, v2):
    result = 0
    for i in range(0, len(v1)):
        result += v1[i] * v2[i]
    return result


vetA = readVetor()
vetB = readVetor()
result = escalarProduct(vetA, vetB)
print(f'{result}')