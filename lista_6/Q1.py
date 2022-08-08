from math import sqrt

def readVetor():
    vet = [float(i) for i in input().split(' ') if i]
    return vet

def average(vetor):
    sum = 0
    for value in vetor:
        sum += value
    return sum/len(vetor)

def hagridSummation(vetor):
    valuesAverage = average(vetor)
    sum = 0
    for value in vetor:
        sum += pow(value * (4 * value - 5 * valuesAverage), 2)
    return sum

def hagridFactor(vetor):
    hagridFactor = 125 / (2 * pow(len(vetor), 2))
    return hagridFactor

def hagrid(vetor):
    hagrid = sqrt(hagridFactor(vetor) * hagridSummation(vetor))
    return hagrid

hagridFromInput = hagrid(readVetor())
print(f'{hagridFromInput:.2f}')
