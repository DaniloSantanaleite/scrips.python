medida_lar = float(input('Qual a largura da area?'))
medida_com = float(input('Qual o comprimento da area?'))
metro_quadrado = medida_lar * medida_com
tinta_necessaria = metro_quadrado / 2
print (f'O metro quadrado da area é de {metro_quadrado:.2f}m² você precisará de {tinta_necessaria} Litros de tinta')