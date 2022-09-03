
lista=[]
from math import sqrt

lista=[]

def quadrado(n):
    x = int(n**(1/2))
    if n == x*x:
        return False
    else:
        return True
def verificar(n):
    x = quadrado((5*(n**2))+4)
    y = quadrado((5*(n**2))-4)
    if x == True and y == True:
        return True
    else:
        return False
    
def criarT(n):
    i=1
    while n>0:
        x = verificar(i)
        if x == True:
            lista.append(i)
            n-=1
        i+=1

x = int(input())
criarT(x)


for i in lista:
    if i == lista[-1]:
        print(f'{i}',end=" ")
    else:
        print(f'{i},',end=" ")
    

    

