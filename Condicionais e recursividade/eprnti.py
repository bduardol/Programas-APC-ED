def formaçãoDeVoo(offset, n):
    global N
    N = N + 1
    print(offset*" " + n*"V")
    if n <= 1:
        print(" ")
        return
    formaçãoDeVoo(offset+1, n-2)
    formaçãoDeVoo(offset+1, n-2)
    return N
    
N = 0
formaçãoDeVoo(10,5)
print(N)