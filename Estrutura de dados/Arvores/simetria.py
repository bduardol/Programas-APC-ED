class ArvoreBinaria():
    def __init__(self, dado, esq = None, dir = None):
        self.dado = dado
        self.esq = esq
        self.dir = dir

def verificador(a, b):
    if a is None and b is None:
        return True
    if a == None:
        if b == None:
            return (a == b) and verificador(a.esq, b.dir) and verificador(a.dir, b.esq)
        else:
            return (a == b.dado) and verificador(x.esq, y.dir) and verificador(a.dir, b.esq)
    elif b == None:
        if a == None:
            return (a == b) and verificador(a.esq, b.dir) and verificador(a.dir, b.esq)
        else:
            return (a.dado == b) and verificador(x.esq, y.dir) and verificador(a.dir, b.esq)
    else:
        return (a.dado == b.dado) and verificador(a.esq, b.dir) and verificador(a.dir, b.esq)

def verificaSimetria(self):
    if not self:
        return True
    return verificador(self.esq, self.dir)

raiz = ArvoreBinaria(1, ArvoreBinaria(0, ArvoreBinaria(1), ArvoreBinaria(0)), ArvoreBinaria(0, ArvoreBinaria(0), ArvoreBinaria(1)))
print(verificaSimetria(raiz))