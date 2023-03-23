def gg(n):
    if n == 201:
        print('gente')
    else:
        print(n, end=" ")
        gg(n+1)
        
gg(100)