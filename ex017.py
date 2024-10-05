from math import hypot
cat_adj = float(input('Digite o valor do cateto adj: '))
cat_opo = float(input('Digite o valor do cateto opo: '))
hipotenusa = hypot (cat_adj, cat_opo)
print(f'O valor da hipotenusa é de {hipotenusa:.2f}')