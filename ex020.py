import random
p1 = str (input("PRIMEIRO NOME: "))
p2 = str (input("SEGUNDO NOME: "))
p3 = str (input("TERCEIRO NOME: "))
p4 = str (input("QUARTO NOME: "))
lista = [p1, p2, p3, p4]
random.shuffle(lista)
print(lista)