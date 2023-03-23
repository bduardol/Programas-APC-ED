quantidade = int(input())
numeros= input().split()
numerosint=[]

for i in numeros:
    numerosint.append(int(i))
x=1
while quantidade > 0:
    for i in range(len(numerosint)):
        for j in range(len(numerosint)):
            if numerosint[i] + numerosint[j] == 42 and x:
                x = 0
                break
        quantidade-=1
if x==0:
    print('sim')
else:
    print('nao')
        
