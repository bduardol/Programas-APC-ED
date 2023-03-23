def verificar(n):
    cont=0
    p=0
    for i in range(len(n)):
        for j in range(p,len(n)):
            if n[i] > n[j]:
                cont+=1
        p+=1
    print(cont)
t = []    
c = input().split()

for i in c:
    t.append(int(i))
    
verificar(t)