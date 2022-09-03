from platform import node

class Node:
    def __init__(self):
        self.dado = None
        self.esq = None
        self.dir = None
    def getPai(self):
        return self.dado
    def setPai(self, dado):
        self.dado = dado
    def getEsq(self):
        return self.esq
    def setEsq(self, dado):
        self.esq = dado
    def getDir(self):
        return self.dir
    def setDir(self, dado):
        self.dir = dado

class arvoreB:
    def __init__(self):
        self.raiz = None
    def getRaiz(self):
        return self.raiz
    def inserir(self, dado):
        none = Node()
        if self.raiz == None:
            none.setPai(dado)
            self.raiz = none
        else:
            if self.raiz.dado < dado:
                if self.raiz.esq == None:
                    none.setPai(dado)
                    x = arvoreB()
                    x.inserir(dado)
                    self.raiz.setEsq(x)
                else:
                    self.raiz.esq.inserir(dado)
            else:
                if self.raiz.dir == None:
                    none.setPai(dado)
                    x = arvoreB()
                    x.inserir(dado)
                    self.raiz.setDir(x)
                else:
                    self.raiz.dir.inserir(dado)
                    
    def printarA(self):
        if self.raiz != None:
            print(self.raiz.dado)
            if self.raiz.esq:
                self.raiz.esq.printarA()
            if self.raiz.dir:
                self.raiz.dir.printarA()
        else:
            print('arvore vazia')
            
    def printarAA(self):
        global x
        if self.raiz:
            if self.raiz.dado or self.raiz.dado == 0:
                if x:
                    print('(',end="")
                    x=False
                else:   
                    print(' (',end="")
                print(self.raiz.dado,end='')
                if self.raiz.dir or self.raiz.esq:
                    if self.raiz.dir:
                        self.raiz.dir.printarAA()
                    else:
                        print(' ()',end='')
                    if self.raiz.esq:
                        self.raiz.esq.printarAA()
                    else:
                        print(' ()',end='')
                else:
                    print(' () ()',end='')
                print(')',end='')
            
            else:
                print(' ()',end=' ')
            
        else:
            print('()')
            
            
x = True                
a = arvoreB()
'''print(a.inserir(1))
print(a.inserir(2))
print(a.inserir(3))
#print(a.inserir(12))
print(a.getRaiz().getEsq().getRaiz().getPai())'''
qnt=int(input())
if qnt:
    termos=list(map(int, input().split()))
    for i in termos:
        a.inserir(i)
a.printarAA()
    

