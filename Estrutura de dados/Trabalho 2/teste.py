codigos = []
def arruma(x):
    for i in x:
        d = x.pop(0)
        y = [x.pop(0) for c in range(0,int(i[-1]))]
        print(x)
        print(i)
        print(y)


while True:
    x=input().split()  
    if x[0] == 'go':
        print(codigos)
        arruma(codigos)
        break
    codigos.append(x)