def calculaComissao(vendas, porcentagem):
    return vendas * porcentagem/100

salarioFixo = float(input())
totalDeVendas = float(input())
salarioComComissao = salarioFixo + calculaComissao(totalDeVendas, 8)

print(f'Retha Sharpe deve receber R$ {salarioComComissao:.2f} no final do mês')