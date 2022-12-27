def readMatrix():
    matrix, readLine = [], input()
    while readLine:
        matrix.append([int(i) for i in readLine.split(' ') if i])
        readLine = input()
    return matrix


def isEven(n):
    return n % 2 == 0


matrix = readMatrix()
cor3 = 0
outraCor = 0
for i in range(0, len(matrix)):
    for j in range(0, len(matrix[i])):
        if isEven(i):
            if isEven(j):
                if isEven(matrix[i][j]):
                    outraCor += matrix[i][j]
            else:
                if isEven(matrix[i][j]):
                    cor3 += matrix[i][j]
        else:
            if isEven(j):
                if isEven(matrix[i][j]):
                    cor3 += matrix[i][j]
            else:
                if isEven(matrix[i][j]):
                    outraCor += matrix[i][j]

print(f'soma pares na cor=3 é {cor3}; e na outra cor é {outraCor}')