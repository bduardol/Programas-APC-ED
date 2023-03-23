def armstrong(n):
    b = str(n)
    aux = 0
    num = n
    total = 0
    for i in b:
        aux = aux + 1
        pass
    if n >=10 and n < 100:
        while n > 0:
            if n > 9:
                if n == num:
                    b = n%10
                    print(f'{b}^{aux}',end="")
                    n = int((n-b)/10)
                    c = n%10
                if aux > 2:
                    print(f' + {c}^{aux}',end="")
                    n = int((n-c)/10)
                else:
                    print(f' + {n}^{aux} =')
                    n = num
                    break
        while n > 0:
            if n > 9:
                if n == num:
                    b = n%10
                    total = b**aux
                    print(f'{b**aux}',end="")
                    n = int((n-b)/10)
                    c = n%10
                    total = total + (c**aux)
                if aux > 2:
                    print(f' + {c**aux}',end="")
                    n = int((n-c)/10)
            else:
                total = total + n
                if total == num:
                    print(f' + {n} = {num}')
                    print(f'{num} é um número de Armstrong de {aux} ordem.')
                    break
                elif total != num:
                    print(f' + {n} != {num}')
                    print(f'{num} não é um número de Armstrong de {aux} ordem.')
                    break 
    
    
    
    elif n > 0 and n < 10:
        print(f'{n}^{aux} =')
        print(f'{n**aux} = {n}')
        print(f'{n} é um número de Armstrong de {aux} ordem.')
    else:
        while n > 0:
            for i in range(aux-2):
                if n == num:
                    b = n%10
                    print(f'{b}^{aux}',end="")
                    n = int((n-b)/10)
                    c = n%10
                if aux > 2:
                    print(f' + {c}^{aux}',end="")
                    n = int((n-c)/10)
                    c = n%10
            ##else:
            print(f' + {n}^{aux} =')
            n = num
            break
        while n > 0:
            for i in range(aux-2):
                if n == num:
                    b = n%10
                    total = b**aux
                    print(f'{b**aux}',end="")
                    n = int((n-b)/10)
                    c = n%10
                    total = total + (c**aux)
                if aux > 2:
                    print(f' + {c**aux}',end="")
                    n = int((n-c)/10)
                    c = n%10
                    
            total = total + (n**aux)
            if total == num:
                print(f' + {n**aux} = {num}')
                print(f'{num} é um número de Armstrong de {aux} ordem.')
                break
            elif total != num:
                print(f' + {n**aux} != {num}')
                print(f'{num} não é um número de Armstrong de {aux} ordem.')
                break
        
armstrong(int(input()))