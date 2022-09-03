#p = (2*o) + (3*d) + t
lista=[]
lista2=[]
cadi = list(map(int, input().split()))

def pontuiacao(o,d,t,i):
    return (2*o) + (3*d) + t


e = int(input())
for i in range(e):
    cadi2 = list(map(int, input().split()))
    lista.append(cadi2[:])
    #print(lista)
    

for i in range(len(lista)):
    x = lista[i]
    p = [x[0], x[1], x[-1], pontuiacao(x[0],x[1],x[2],x[-1])]
    if lista2 == []:
        lista2.append(p)
    else:
        if lista2[i-1][-1] > p[-1]:
            lista2.insert(i,p)
        elif lista2[i-1][-1] < p[-1]:
            lista2.insert(i-1,p)
        else:
            if lista2[i-1][-1] > 60:
                lista2.insert(i,p)
            elif 60 < p[-1]:
                lista2.insert(i-1,p)
            else:
                if lista2[i-1][1] > p[1]:
                    lista2.insert(i,p)
                elif lista2[i-1][1] < p[1]:
                    lista2.insert(i-1,p)
                else:
                    if lista2[i-1][0] > p[0]:
                        lista2.insert(i,p)
                    elif lista2[i-1][0] < p[0]:
                        lista2.insert(i-1,p)
                    else:
                        if lista2[i-1][-1] > p[-1]:
                            lista2.insert(i,p)
                        elif lista2[i-1][-1] < p[-1]:
                            lista2.insert(i-1,p)
                        
            
            
            
    
        
#for i in lista:
    #print(pontuiacao(i[0],i[1],i[2],i[-1]))
    

print(lista2)
#print(lista2.index(cadi)+1)

                