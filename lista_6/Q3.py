def readVetor() -> list:
    vet = [float(i) for i in input().split(' ') if i]
    return vet

def findIndexes(k: int, vector: list) -> tuple:
    """
    O(n^2)
    """
    n = len(vector)
    for i in range(0, n):
        for j in range(0, n):
            if vector[i] + vector[j] == k:
                return (i, j)
    return (n, n)

print(findIndexes(10, readVetor()))
