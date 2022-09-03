class arvore:
    def __init__(self,dado):
        self.dado = dado
        self.filho = []
    def setFilho(self):
        return len(self.filho)
    def getPai(self):
        return self.dado
    def getFilho(self):
        return self.filho
    def getCheio(self):
        return self.dado[-1] == len(self.filho)
    def getVazio(self):
        return self.dado[-1] != len(self.filho)
    
    def add(self,x,b=True):
        valor = arvore(x)
        if self.getVazio():
            self.filho.append(valor)
            return True
        else:
            for i in self.filho:
                if i.getVazio():
                    i.addLista(x)
                    return True
            
                    
        
    def printaA(self):
        print(self.dado)
        for i in range(int(self.dado[-1])):
            self.filho[i].printaA()
    def gametree(self,cont=0):
        print('__'*cont,end='')
        print(self.dado[0])
        cont+=1
        for i in range(self.dado[-1]):
            self.filho[i].gametree(cont)
    def probtree(self,cont=0):
        print('..'*cont,end='')
        print(f'{self.dado[0]} ({self.dado[1]:.2f}%)')
        cont+=1
        for i in range(self.dado[-1]):
            self.filho[i].probtree(cont)
    
def criar_arvore(n):
    lista2=n[1:]
    lista77=[]
    for i in n:
        x=0
        a=arvore(i)
        for j in range(i[-1]):
            if lista2[0][0] != '?':
                a.add(lista2.pop(0))
            x=1
        if x:
            lista77.append(a)
    return lista77
def arrumar(a,n):
    while n!= []:
        if a.getVazio():
            for i in range(a.dado[-1]):
                a.filho.append(n.pop(0))
        else:
            for i in a.filho:
                arrumar(i,n)
        
                

lista = []    
b=True
while True:
    x = input().split()
    if x[0] == 'go':   
        arv.probtree()
        #arv.printaA()
    elif x[0] == 'gametree':
        arv = criar_arvore(lista)
        a=arv.pop(0)
        arrumar(a,arv)
        break
    elif x[0] == 'probtree':
        criar_arvore(lista)
        arv.probtree()
        break
    else:
        p = 100 if x[0] == 'V' else 0
        lista.append([x[0],p,int(x[-1])])
    
            
        
        