class Grafos:
    def __init__(self,):
        self.grafo = {}
    def getDados(self):
        return self.grafo
    def IV(self,dado, u=0):
        if dado not in self.grafo.keys():
            self.grafo.update({dado:[]})
        #print(self.grafo)
    def IA(self,u,v):
        if u in self.grafo.keys() and v in self.grafo.keys():
            if v not in self.grafo[u]:
                self.grafo[u].append(v)
            if u not in self.grafo[v]:
                self.grafo[v].append(u)
    def RV(self, u):
        if u in self.grafo.keys():
            self.grafo.pop(u)
            for i in self.grafo.values():
                if u in i:
                    i.remove(u)
    def RA(self,u,v):
        if u in self.grafo.keys():
            if v in self.grafo[u]:
                self.grafo[u].remove(v)
    def contador(self):
        cont=0
        for i in self.grafo.values():
            if i != []:
                if len(i)>cont:
                    cont=len(i)
        return cont

grafo = Grafos()
x=int(input())
for i in range(x):   
    x=input().split()
    if x[0] == "IV":
        grafo.IV(x[-1])
    elif x[0] == "IA":
        grafo.IA(x[1],x[-1])
    elif x[0] == "RV":
        grafo.RV(x[-1])
    elif x[0] == "RA":
        grafo.RA(x[1],x[-1])
#print(grafo.getDados())
print(grafo.contador())