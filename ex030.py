n = int(input("Digite o tamanho da lista:"))
v = [0] * n
i = 0
j = 2
while i < n:
    v[i] = j
    j += 1
    i += 1
d = 0
while d < n:
    num = v[d]
    primo = True

    if num < 2:
        primo = False
    else:
        i = 2
        while i <= int(num ** 0.5): 
            if num % i == 0:
                primo = False
                break
            i += 1
    if primo:
        print(num, end=' ')
    
    d += 1