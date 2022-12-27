vogais = ['a', 'e', 'i', 'o']

frase = list(input())
for i in frase:
    if i.lower() in vogais:
        frase.remove(i)
print(''.join(frase) + 'flR0OA')