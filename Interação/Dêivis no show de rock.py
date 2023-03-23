def rock(n,i):
    aux = n
    a = int(0)
    while aux > 0:
        k = int(input())
        a = a + k
        aux = aux - 1
    a = int(a / n)
    print(f'media: {a}')
    if a >= i:
        print('o rock reinara mais uma vez')
    else:
        print('rockeiros trabalhando ja')
        
n,i = (map(int, input().split()))
rock(n,i)