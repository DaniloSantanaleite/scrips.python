metro = float(input('Digite um valor em metros:'))
conversor_cm = metro * 100
conversor_mm = metro * 1000
conversor_km = metro / 1000
print(f'{metro}Metros é equivalente a {conversor_cm} cm e equivalente a {conversor_mm} mm. e equivalente a {conversor_km} km')
#Neste caso não coloquei a propriedade .:0f pois o conversor em km iria falhar