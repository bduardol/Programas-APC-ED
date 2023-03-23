def loop(n):
    ehverdade = True
    if n > 0:
        while ehverdade:
            if n <= 1000000000 and n > 0:
                print('nossa o programa foi rapido')
                n = int(input())
            elif n > 1000000000:
                print('isso ai tem cara de loop infinito')
                n = int(input())
            else:
                break
            
loop(int(input()))