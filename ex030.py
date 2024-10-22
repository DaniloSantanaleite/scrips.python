def eh_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):  
        if num % i == 0:
            return False
    return True

n = int(input("Digite o tamanho da lista: "))
v = [0] * n
i = 0
j = 2 

while i < n:
    v[i] = j
    j += 1  
    i += 1  

print("Lista preenchida:", v)


for d in range(n):
    if eh_primo(v[d]):
        print(v[d], end='-')
    