import sys
sys.setrecursionlimit(10**4)
lista=[]
li=[]
def ageitar(n):
    p=input().split()
    for i in range(n):
        c = fibonacci(int(p[i])-1)
        lista.append(c)
    li = tuple(lista)
    print(li)

def fibonacci(n):
    if n > 1:
        return fibonacci(n-1) + fibonacci(n-2)
    return n

if __name__ == '__main__':
    a=int(input())
    ageitar(a)

