

class Grafos:
    def __init__(self,):
        self.grafo = {}
    def adicionar_aresta(self,dado, u):
        if int(u[0]) != 0:
            self.grafo.update({dado:u[1:]})
        else:
            self.grafo.update({dado:[None]})
        #print(self.grafo)
    def verificar_ciclo(self):
        for i in self.grafo.keys():
            if self.grafo[i] != [None]:
                for j in self.grafo[i]:
                    if i in self.grafo[j]:
                        return True

grafo = Grafos()
x=int(input())
for i in range(x):   
    x=input().split()
    '''if x[0] == 'ok':
        a = g(lista)
        print(a)
        break'''
    grafo.adicionar_aresta(x[0],x[1:])

if grafo.verificar_ciclo():
    print('Hoje tem!')
else:
    print('... que ama ninguem.')
    
    
    