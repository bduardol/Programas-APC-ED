class Node:
    def __init__(self):
        self.dado = None
        self.filho = []
    def getPai(self):
        return self.dado
    def setPai(self, dado):
        self.dado = dado
    def setFilho(self, dado):
        self.filho = dado
    def getFilho(self):
        return self.filho

class arvore:
    def __init__(self):
        self.raiz = None
    def getRaiz(self):
        return self.raiz
    def inserir(self, dado, qnt):
        none = Node()
        if self.raiz == None:
            none.setPai([dado,qnt])
            self.raiz = none
        else:
            none.setPai([dado,qnt])
            x = arvore()
            x.raiz = none
            self.raiz.filho.append(x)
    def addPorce(self):
        s=0
        for i in range(len(self.raiz.filho)):
            if self.raiz.filho[i].raiz.dado[0] == '?':
                self.raiz.filho[i].addPorce()
                s+=self.raiz.filho[i].raiz.dado[1]
            else:
                s+=self.raiz.filho[i].raiz.dado[1]
        if self.raiz.dado[-1] != 0:
            self.raiz.dado.insert(1,s/self.raiz.dado[-1])
        else:
            self.raiz.dado.insert(1,0)
        
    def inFilhos(self,x,c=True):
        
        verificador = self.raiz.dado[-1]
        if verificador != len(self.raiz.filho) and self.raiz.dado[-1] != 0:
            s=0
            s1=0
            c=True
            #for i in range(verificador):
            if x[0] == '?':
                x = input().split()
            p=0
            if x[0] == 'V':
                p = 100
            y = Node()
            y.setPai([x[0],p,int(x[1])])
            t = arvore()
            t.raiz = y
            self.raiz.filho.append(t)
            return c
            '''if len(self.raiz.filho) != verificador:
                x = input().split()'''
            '''if x[0] != '?':
                self.raiz.dado.insert(1,s/self.raiz.dado[-1])'''
        
        else:
            c=False
            for i in range(self.raiz.dado[-1]):
                if self.raiz.filho[i].inFilhos(x):
                    break
    def printaA(self):
        print(self.raiz.dado)
        for i in range(self.raiz.dado[-1]):
            self.raiz.filho[i].printaA()
    def adiciP(self):
        s1=0
        for i in range(self.raiz.dado[-1]):
            s1+=self.raiz.filho[i].raiz.dado[1]
        if self.raiz.dado[-1] != 0:
            self.raiz.dado.insert(1,s1/self.raiz.dado[-1])
        else:
            self.raiz.dado.insert(1,0)
    def gametree(self,cont=0):
        print('__'*cont,end='')
        print(self.raiz.dado[0])
        cont+=1
        for i in range(self.raiz.dado[-1]):
            self.raiz.filho[i].gametree(cont)
    
    def probtree(self,cont=0):
        print('..'*cont,end='')
        print(f'{self.raiz.dado[0]} ({self.raiz.dado[1]:.2f}%)')
        cont+=1
        for i in range(self.raiz.dado[-1]):
            self.raiz.filho[i].probtree(cont)
            
        

def adiciArv(arv):
    if len(arv.getRaiz().filho) != arv.getRaiz().dado[-1]:
        arv.inserir('?', int(comando[-1]))
    else:
        for i in range(len(arv.getRaiz().filho)):
            adiciArv(arv.getRaiz().filho[i])
            
    



arv = None



while True:
    comando = input().split()
    if comando[0] == 'gametree':
        arv.gametree()
        break
    elif comando[0] == 'ok':
        #arv.addPorce()
        arv.printaA() #isso eh so para printar a arvore
        
        break
    elif comando[0] == 'probtree':
        arv.addPorce()
        arv.probtree()
        break
    elif comando[0] == '?':
        if arv == None:
            arv= arvore()
            arv.inserir('?', int(comando[-1]))
        else:
            adiciArv(arv)
        #arv.inFilhos(comando) 
        #arv.adiciP()
        #arv.printaA() isso eh so para printar a arvore
        #arv.probtree()
    else:
        arv.inFilhos(comando)
        
        

