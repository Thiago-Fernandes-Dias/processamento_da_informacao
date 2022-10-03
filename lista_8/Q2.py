import math

def readMatrix():
    m, ler_linha = [], input()
    while ler_linha:
        m.append([int(i) for i in ler_linha.split(" ") if i])
        ler_linha = input()
    return m

def getBottomTriangle(matrix):
    bottomHalf = matrix[ math.floor(len(matrix) / 2) : ]
    bottomHalf.reverse()
    triangle = []
    for i in range(0, len(bottomHalf)):
        line = bottomHalf[i]
        triangle.append(line[ i : len(line) - i])
    return triangle

def getTriangleOddsSum(triangle):
    result = 0
    for line in triangle:
        for value in line:
            if value % 2 == 0:
                continue
            result += value
    return result

matrix = readMatrix()
triangle = getBottomTriangle(matrix)
oddsSum = getTriangleOddsSum(triangle)
print(f'soma ímpares triângulo inferior é {oddsSum}')
