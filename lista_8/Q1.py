def readMatrix():
    m, ler_linha = [], input()
    while ler_linha:
        m.append([int(i) for i in ler_linha.split(" ") if i])
        ler_linha = input()
    return m

def weriteMatrix(matrix):
    for line in matrix:
        print(*line)
    
def testeLinhaPermutavel(matrix):
    for line in matrix:
        for i in range(0, len(line)):
            if i in line:
                continue
            return False
    return True
    
linhaPermutavel = testeLinhaPermutavel(readMatrix())
print('SIM' if linhaPermutavel else 'NAO')
