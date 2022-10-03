def readMatrix():
    m, ler_linha = [], input()
    while ler_linha:
        m.append([int(i) for i in ler_linha.split(" ") if i])
        ler_linha = input()
    return m

def writeMatrix(matrix) -> None:
    for line in matrix:
        print(*line)

def generateBackgroudMatrix(matrix):
    lines = len(matrix)
    columns = len(matrix[0])
    backgroundMatrix = [[-1 for _ in range(0, columns)] for _ in range(0, lines)] 
    return backgroundMatrix

def activateSEPoints(matrix, backgroundMatrix):
    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[i]) - 1):
            selectedEntry = matrix[i][j]
            westEntry = matrix[i][j - 1]
            southwestEntry = matrix[i + 1][j - 1]
            southEntry = matrix[i + 1][j]
            if selectedEntry >= westEntry:
                continue
            if selectedEntry >= southwestEntry:
                continue
            if selectedEntry >= southEntry:
                continue
            backgroundMatrix[i][j] = selectedEntry

def main():
    inputedMatrix = readMatrix()
    backgroundMatrix = generateBackgroudMatrix(inputedMatrix)
    activateSEPoints(inputedMatrix, backgroundMatrix)
    writeMatrix(backgroundMatrix)

main()
