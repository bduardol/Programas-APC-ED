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
            
    def add(self,dados,x=True):
        if self.getVazio():
            self.filho.append(dados)
            return True
        else:
            
            for i in self.filho:
                if i.getVazio():
                    i.filho.append(dados)
                    return True
            if x:
                for i in self.filho:
                    if i.add(dados,x=True):
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
    def addPorce(self):
        s=0
        for i in range(len(self.filho)):
            if self.filho[i].dado[0] == '?':
                self.filho[i].addPorce()
                s+=self.filho[i].dado[1]
            else:
                s+=self.filho[i].dado[1]
        if self.dado[-1] != 0:
            self.dado.insert(1,s/self.dado[-1])
        else:
            self.dado.insert(1,0)
    def porcentagem(self,s=0,cont=0):
        for i in range(self.dado[-1]):
            if self.filho[i].dado[0] != '?':
                s+=self.filho[i].dado[1]
                cont+=1
            else:
                s,cont= self.filho[i].porcentagem(s,cont)
        #self.dado.insert(1,s/cont)
        return s,cont
    
    def addp(self):
        s=0
        cont=0
        x=0
        for i in range(self.dado[-1]):
            if self.filho[i].dado[0] == '?':
                s,cont = self.filho[i].porcentagem()
                self.filho[i].dado.insert(1,s/cont)
        for i in range(self.dado[-1]):
            x=1
            if self.filho[i].dado[0] == '?':
                s,cont = self.porcentagem()
            else:
                s+=self.filho[i].dado[1]
                cont+=1
        if x:
            self.dado.insert(1,s/cont)
    def porDNV(self,s=0,cont=0):
        for i in range(self.dado[-1]):
            if self.filho[i].dado[0] == '?':
                x = self.filho[i].porDNV(s,cont)
                s+=x[0]
                cont+=x[-1]
                self.filho[i].dado.insert(1,s/cont)
        for i in range(self.dado[-1]):
            s+=self.filho[i].dado[1]
            cont+=1
        return s,cont
            
        

    
b=True
while True:
    x = input().split()
    if b:
        arv=arvore([x[0],1,int(x[-1])])
        b=False
    elif x[0] == 'go':
        
        arv.porDNV()
        arv.probtree()
        #arv.printaA()
    elif x[0] == 'gametree':
        arv.gametree()
        break
    elif x[0] == 'probtree':
        arv.addp()
        arv.probtree()
        break
    else:
        p = 100 if x[0] == 'V' else 0
        none = arvore([x[0],p,int(x[-1])])
        arv.add(none)
    
            
        
        