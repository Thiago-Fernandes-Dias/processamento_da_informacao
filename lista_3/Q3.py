def distanceFromOrigin(x, y):
    return (x**2 + y**2)**.5


def canTravel(x, y, engineEfficiency, gasAvailabel):
    distance = distanceFromOrigin(x, y)
    gasNeeded = distance / engineEfficiency
    if gasNeeded > gasAvailable:
        return 'N'
    return 'S'


x = float(input())
y = float(input())
engineEfficiency = float(input())
gasAvailable = float(input())
print(canTravel(x, y, engineEfficiency, gasAvailable))