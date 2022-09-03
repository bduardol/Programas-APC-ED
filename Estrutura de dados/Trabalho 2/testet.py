from collections import defaultdict

class grafos:
    def __init__(self,dado,vertices):
        self.dado = dado
        self.vertices = vertices
        self.grafo = [[] for i in range(self.vertices)]
    def adicionar_aresta(self,dado, u, v):
        self.grafo[u-1].append(v)
listag=[]
def g(l):
    for i in l:
        x,y=i[-1]
        for j in range(x,x+y-1):
            listag.append((i[0],l[j][0]))
        
            
    return listag
        
        
    
    
    
    
lista = []
cont=0
v=1
while True:   
    x=input().split()
    if x[0] == 'ok':
        a = g(lista)
        print(a)
        break
    cont+=1
    lista.append([cont-1,x[0],(v,int(x[-1]))])
    v=int(x[-1])+1
    
    