def readMatrix():
    m, ler_linha = [], input()
    while ler_linha:
        m.append([int(i) for i in ler_linha.split(" ") if i])
        ler_linha = input()
    return m

def oneAloneCheck(matrix):
    ones = []
    for line in matrix:
        for value in line:
            if value == 1:
                ones.append(value)
                continue
            if value != 0:
                return False
    oneCheck = len(ones) == len(matrix)
    return oneCheck

def yesOrNo(bool):
    if bool:
        print('SIM')
        return
    print('NAO')

yesOrNo(oneAloneCheck(readMatrix()))