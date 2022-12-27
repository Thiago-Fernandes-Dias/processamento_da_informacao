contaminados = 1595
diasDePandemia = -1  # Por que ????
population = int(input())
txContagio = float(input())
imunidadeDeRebanho = population * .61
contaminadosOntem = contaminados

while contaminados < imunidadeDeRebanho:
    contaminadosHoje = contaminadosOntem * txContagio
    contaminados += contaminadosOntem
    diasDePandemia += 1
    contaminadosOntem = contaminadosHoje

print(f'A cidade conseguiu imunidade coletiva em {diasDePandemia} dias')