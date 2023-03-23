### ex2
t = int(input())
maximo = float("-inf")
minimo = float("inf")
while t > 0:
    a,n = input().split()
    a,n = [int(a),int(n)]
    soma = 0
    while n > 0:
        if a%2 == 1:#impar
            soma += a
            a += 2
            n -= 1
        else:
            a += 1
    if soma > maximo:
        maximo = soma
    if soma < minimo:
        minimo = soma
    print(soma)
    t -= 1
print(maximo)
print(minimo)
print(f"{(maximo+minimo)/2:.2f}")



### ex1
t = int(input())
while t > 0:
    a,n = input().split()
    a,n = [int(a),int(n)]
    soma = 0
    while n > 0:
        soma += a
        print(a,end=" ")
        a += 1
        n -= 1
    print(f"\n{soma}")
    t -= 1
    