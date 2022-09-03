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
        p=0
        if dado == 'V':
            p=100
        none = Node()
        if self.raiz == None:
            none.setPai([dado,qnt])
            self.raiz = none
        else:
            if len(self.raiz.filho) != int(self.raiz.dado[-1]):
                none.setPai([dado,p,qnt])
                x = arvore()
                x.raiz = none
                self.raiz.filho.append(x)
                return True
            else:
                x=0
                for i in range(self.raiz.dado[-1]):
                    if self.raiz.filho[i].raiz.dado[0] == '?':
                        pass

                    if self.raiz.filho[i].inserir(dado,int(qnt)):
                        return True
                        
                
    def printaA(self):
        print(self.raiz.dado)
        for i in range(int(self.raiz.dado[-1])):
            self.raiz.filho[i].printaA()
    def gametree(self,cont=0):
        print('__'*cont,end='')
        print(self.raiz.dado[0])
        cont+=1
        for i in range(self.raiz.dado[-1]):
            self.raiz.filho[i].gametree(cont)
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
    def probtree(self,cont=0):
        print('..'*cont,end='')
        print(f'{self.raiz.dado[0]} ({self.raiz.dado[1]:.2f}%)')
        cont+=1
        for i in range(self.raiz.dado[-1]):
            self.raiz.filho[i].probtree(cont)
            
            
            
            
arv = None



while True:
    comando = input().split()
    if comando[0] == 'gametree':
        arv.gametree()
        break
    elif comando[0]=='ok':
        arv.printaA()
    elif comando[0] == 'probtree':
        arv.addPorce()
        arv.probtree()
        break
        
    else:
        if arv == None:
            arv= arvore()
            arv.inserir('?', int(comando[-1]))
        else:
            arv.inserir(comando[0],int(comando[-1]))

        #arv.inFilhos(comando) 
        #arv.adiciP()
        #arv.printaA() isso eh so para printar a arvore
        #arv.probtree()
