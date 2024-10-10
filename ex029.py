km = int(input('QUAL A SUA VELOCIDADE: '))
if km >= 81:
    print('Você ultrapassou o limite da via')
    multa = (km - 80) * 7
    print(f'O valor da multa é {multa:.0f}')
else:
    print('Parabêns! Você está no limite da via')