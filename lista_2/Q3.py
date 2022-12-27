pontoDado = (-13, 3)


def calcula_distancia_Euclidiana(x, y):
    distanceInX = (x - pontoDado[0])**2
    distanceInY = (y - pontoDado[1])**2
    return (distanceInX + distanceInY)**.5


x = int(input())
y = int(input())
distanceBetweenP1 = calcula_distancia_Euclidiana(x, y)

print(f'distancia Euclidiana = {distanceBetweenP1:.2f}')