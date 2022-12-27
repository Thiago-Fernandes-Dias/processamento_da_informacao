from math import sqrt
g = float(input())
f = float(input())
denominator = 5 * sqrt(g * f)
numerator = pow(g, 2)
print(f'F = {(numerator / denominator):.3f}')