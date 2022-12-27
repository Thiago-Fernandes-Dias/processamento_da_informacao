def readMatrix():
    matrix, readLine = [], input()
    while readLine:
        matrix.append([int(i) for i in readLine.split(' ') if i])
        readLine = input()
    return matrix


def whiteMatrix(matrix):
    for line in matrix:
        print(*matrix)


def lookInColumn10():
    matrix = readMatrix()
    for i in range(0, len(matrix)):
        if matrix[i][10] == 1:
            print(f'{i}')
            return
    print(f'{-1}')


lookInColumn10()