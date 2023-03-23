def jkk(x):
    while x > 0:
        if x%2 == 1:
            print('Boa noite!')
        else:
            print('Bom dia!')  
        x = x - 1
    print('Ué? Já acabou?')
    
jkk(int(input()))