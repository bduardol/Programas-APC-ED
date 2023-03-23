import math
from time import sleep

print("Vamos calcular baskara automaticamente?\n(Tecle 1 para sim - 2 para não)")
i1 = int(input())
if i1 == 1: 
    print("informe valor de a")
elif i1 == 2:
    print("obrigado")
    exit(0)
else:
    exit(
        print("O seu espertinho, ein, achou que ia da erro kkk")) 
a = int(input())
print("informe valor de b")
b = int(input())
print("informe o valor de c")
c = int(input())

print("e vamos de calcular...\n__________________")
b2 = int(b ** 2)
ac = int(-4 * a * c) 
delta = int(b2 + ac)

if delta <= 0:
    exit(print("seu delta não existe"))
    
else:
    print("seu delta existe, continuando......\n\n")

sleep(5)
raiz = int(math.sqrt(delta))

x1 = int((-(b)+raiz)/2*a)
x2 = int((-(b)-raiz)/2*a)

print("aqui esta seu X1 =", x1, "\ne seu X2 =",x2, "\n\nObrigado por usar!!!\n---------------------------")