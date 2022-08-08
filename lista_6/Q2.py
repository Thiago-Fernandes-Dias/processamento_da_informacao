def readVetor():
    return [float(i) for i in input().split(' ') if i]
    
def lowestBetween3(vetor):
    lowest = vetor[0]
    for value in vetor:
        if value < lowest:
            lowest = value
    return lowest

g1 = readVetor()
g2 = []
for i in range(0, len(g1)):
    max = 0
    if i == 0:
        max = lowestBetween3([g1[21], g1[0], g1[1]])
    elif i == 21:
        max = lowestBetween3([g1[20], g1[21], g1[0]])
    else:
        max = lowestBetween3(g1[i - 1 : i + 2])
    g2.append(max)
    
for value in g2:
    print(f'{value:.0f}', end = ' ')
        