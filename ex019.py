from random import choice
p1 = str(input("PRIMEIRO ALUNO: "))
p2 = str(input("SEGUNDO ALUNO: "))
p3 = str(input("TERCEIRO ALUNO: "))
p4 = str(input("QUATRO ALUNO: "))
lista = [p1, p2, p3, p4]
escolha = choice(lista)
print(f"O Aluno escolhido foi {escolha}")