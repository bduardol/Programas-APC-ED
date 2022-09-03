qnt = int(input())
listam = []
listaM = []
oq=[]
def repetidos(n):
    l = []
    for i in n:
        if i not in l:
            l.append(i)
    l.sort()
    return l

for i in range(qnt):
    listam.clear()
    for i in range(4):
        materia = input()
        if materia != '':
            listam.append(materia)
    listaM.append(listam[:])

x=0
todas=[]
for i in listaM:
    x=0
    plano = i[0]
    plano1 = []
    estudo = i[1:]
    estudo1=[]
    for i in estudo:
        for j in i:
            todas.append(j)
    #print(todas)
    for i in plano:
        plano1.append(i)
    for i in estudo:
        for j in i:
            estudo1.append(j)
            
    lixo=[]
    estudo2=[]
    x=1
    for j in estudo1:
        if j in plano1:
            plano1.remove(j)
            estudo2.append(j)
        else:
            print('You died!')
            x=0
            break
    if x:        
        if plano1 != [] :
            plano1 = repetidos(plano1)
            a=''
            for i in plano1:
                a+=i
            print(f'Bora ralar: {a}')
        else:
            print("It's in the box!")
                

        
        


        
