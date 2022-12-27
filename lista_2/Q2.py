def calculaDinheiro(valorEmOZ):
    jb1, jb7, jb19, jb20, jb35 = 0, 0, 0, 0, 0
    while valorEmOZ - 35 >= 0:
        valorEmOZ -= 35
        jb35 += 1
    while valorEmOZ - 20 >= 0:
        valorEmOZ -= 20
        jb20 += 1
    while jb19 - 19 >= 0:
        valorEmOZ -= 19
        jb19 += 1
    while valorEmOZ - 7 >= 0:
        valorEmOZ -= 7
        jb7 += 1
    while valorEmOZ - 1 >= 0:
        valorEmOZ -= 1
        jb1 += 1
    return jb1, jb7, jb19, jb20, jb35

valorEmJabuticabaCoins = int(input())
jabuticabaCoins = calculaDinheiro(valorEmJabuticabaCoins)
print(f"""
{jabuticabaCoins[4]} JabuticabaCoin(s) de OZ$ 35
{jabuticabaCoins[3]} JabuticabaCoin(s) de OZ$ 20
{jabuticabaCoins[2]} JabuticabaCoin(s) de OZ$ 19
{jabuticabaCoins[1]} JabuticabaCoin(s) de OZ$ 7
{jabuticabaCoins[0]} JabuticabaCoin(s) de OZ$ 1
""")