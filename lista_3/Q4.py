def f(x):
    if x < 1 or x > 7:
        return 1
    elif x >= 4:
        return 1 - (x - 3)**2 - 2
    return (x - 1)**2 + 1


variable = int(input())
print(f'f({variable}) = {f(variable)}')