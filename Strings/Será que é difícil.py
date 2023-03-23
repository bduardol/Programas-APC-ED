def alfabeto(n):
    total = len(n)
    metade = int(total/2)
    primeirametade = n[:metade]
    segundametade = n[metade:]
    a = [ord(character) for character in primeirametade]
    b = [ord(character) for character in segundametade]
    if a[0] > b[0]:
        print(primeirametade*2)
    else:
        print(segundametade*2)
    
    
    
alfabeto(input())