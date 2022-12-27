def readMatrix():
    matrix, readLine = [], input()
    while readLine:
        matrix.append([int(i) for i in readLine.split(' ') if i])
        readLine = input()
    return matrix

def getMatrixBorder(matrix):
    matrixColumns = len(matrix[0])
    topBorder = matrix[1][1:matrixColumns - 1]
    bottomBorder = matrix[len(matrix) - 2][1:matrixColumns - 1]
    leftBorder, rightBorder = [], []
    for i in range(2, len(matrix) - 2):
        leftBorder.append(matrix[i][1])
        rightBorder.append(matrix[i][matrixColumns - 2])
    matrixBorder = topBorder + bottomBorder + leftBorder + rightBorder
    return matrixBorder

def sumEvensInMatrixBorder(matrix):
    matrixBorder = getMatrixBorder(matrix)
    evens = []
    for value in matrixBorder:
        if value % 2 != 0:
            continue
        evens.append(value)
    mult = evens[0]
    for i in range(1, len(evens)):
        mult *= evens[i]
    return mult

matrix = readMatrix()
mult = sumEvensInMatrixBorder(matrix)
print(f'multiplicação borda=1 pares = {mult:.0f}')