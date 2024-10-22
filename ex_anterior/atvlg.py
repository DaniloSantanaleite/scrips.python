n = int(input("Digite o tamanho da lista:"))
v = [0] * n
i = 0
j = 2 
while i < n:
 v[i] = j 
 j += 1  

for d in range(n):
    num = v[d]
    primo = True 
    if num < 2:
        primo = False  
    else:
        for i in range(2, int(num ** 0.5) + 1): 
            if num % i == 0:
                primo = False 
                break
    if primo:
        print(num, end='(P)')
    else:
        print(num, end='(NP)')
