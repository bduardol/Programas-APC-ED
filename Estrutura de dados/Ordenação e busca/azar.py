p,q=list(map(int, input().split()))

#print(x,y)
lista = []

for k in range(p):
    x=int(input())
    y= x%q
    w = 'impar' if x%2 else 'par'
    z= [y,x,w]
   
    lista.append(z)
    lista.sort(reverse = True)
for i in range(len(lista)):
    for j in range(i):
        if lista[j][0] == lista[j+1][0]:
            if lista[j][-1] == 'par' and lista[j+1][-1] == 'par':
                if lista[j][1] > lista[j+1][1]:
                    pass
                else:
                    lista[j],lista[j+1] = lista[j+1],lista[j]
            elif lista[j][-1] == 'par':
                pass
            elif lista[j+1][-1] == 'par':
                lista[j],lista[j+1] = lista[j+1],lista[j]
            else:
                if lista[j][-1] == 'impar' and lista[j+1][-1] == 'impar':
                    if lista[j][1] < lista[j+1][1]:
                        pass
                    else:
                        lista[j],lista[j+1] = lista[j+1],lista[j]
               
print(lista)                    
c=''                
x=1                
for i in lista:
    if x:
        c=str(i[1])
        c+=' '
        x=0
    else:
        c+=str(i[1])
        c+=' '

       
print(c[:-1])                    
