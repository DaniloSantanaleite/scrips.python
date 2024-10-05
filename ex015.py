dia = int(input('Quantidade de dias utilizados: '))
km = int(input('Quantidade de kms utilizados: '))
valor_total = (dia * 60) + (km * 0.15)
print(f' O valor do dia é de R$60.00 e o valor do Km é de R$ 0.15, valor total do aluguel é de {valor_total:.2f}')