import math
angulo = float(input(" Digite o ângulo que você deseja: "))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f" O valor do SENO é: {seno:.2f}")
print(f" O valor do COSSENO é: {cosseno:.2f}")
print(f" O valor do TANGENTE é: {tangente:.2f}")