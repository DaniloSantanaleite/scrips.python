tabela = float(input("Digite o valor da tabela do veículo: "))
fabricacao_ano = int(input('Digite o ano de fabricação do veículo: '))

if fabricacao_ano >= 2010:
    soma = tabela * 3.5 / 100  # Calcula 3,5% da tabela
    juros = tabela + soma
    print(f"O valor com juros é de R$ {juros:.3f}")
else:
    soma = tabela * 2.5 / 100  # Calcula 2,5% da tabela
    juros = tabela + soma
    print(f"O valor com juros é de R$ {juros:.3f}")

