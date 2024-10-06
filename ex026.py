frase = str(input('DIGITE A FRASE: ')).strip() .upper()
print('Nesta frase tem', frase.count('A'),'Letras A')
print('A primeira letra A aparece na posição', frase.find('A')+1)
print('A ultima letra A aparece na posição', frase.rfind('A')+1)