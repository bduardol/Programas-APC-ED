def acredita(n1,n2):
    if n1 > n2:
        return acredita(n1/n2, n2)
    elif n1 == n2:
        return 'Pode Acreditar'
    else:
        return "Fake News"
        
        
print(acredita(1099511627776,4))