produto = float(input('Qual o valor do produto? '))
desconto = produto - (produto * 10 / 100) 
print(f'O valor do produto é de R${produto} com desconto de 5% você pagará R${desconto:.2f} .')

