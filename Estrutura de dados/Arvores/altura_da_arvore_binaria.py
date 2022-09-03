def altura(raiz):    
    if raiz is None:
        return 0
    else:
        if raiz.esq or raiz.dir:
            return max(altura(raiz.esq), altura(raiz.dir)) + 1
        else:
            return 0

    