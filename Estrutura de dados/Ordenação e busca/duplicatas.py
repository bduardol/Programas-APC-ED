qnt = input()
roupas=input().split()
contados=[]
tudo = 0
co = []
for i in roupas:
    cont=0
    for j in roupas:
        if i == j and i not in contados:
            cont +=1
    co.append(cont)
    contados.append(i)

for i in co:
    if i>1:
        b= i-1
        tudo+=b    

print(tudo)       