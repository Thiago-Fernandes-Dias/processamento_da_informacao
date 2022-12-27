def genNullMatrix(lines, columns):
    matrix = [[0 for i in range(0, columns)] for _ in range(0, lines)]
    return matrix


def writeMatrix(matrix):
    for line in matrix:
        print(*line)


def readVector():
    vector = [int(i) for i in input().split(' ') if i]
    return vector


def asignValues(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            matrix[i][j] = (2 * i + 2 * j) % 5


dimentions = readVector()
matrix = genNullMatrix(dimentions[0], dimentions[1])
asignValues(matrix)
writeMatrix(matrix)