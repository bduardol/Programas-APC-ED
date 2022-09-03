lista = []

def fibonacci(n):
    lista.append(n)
    if n<=1: 
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
entrada = int(input())

lixo = []
contagem=[]

resultado = fibonacci(entrada)

lista.sort()

for i in lista:
    if i not in lixo:
        x = lista.count(i)
        contagem.append([i,x])
        lixo.append(i)
        
#print(lista)
#print(contagem)
#print(lixo)
print(f'fibonacci({entrada}) = {resultado}.')
if entrada == 1:
    print(f'0 chamada(s) a fibonacci(0).')
for i in contagem:
    print(f'{i[-1]} chamada(s) a fibonacci({i[0]}).')
    
    
    
    
    
    