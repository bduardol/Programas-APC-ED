
def deivis_sequence(q):
    return fib(q, 0) + 1

def fib(n, passou_aqui):
    if passou_aqui == 0:
        n = n - 1
        passou_aqui = 1
    if n == 1 or n == 00:
        return n
    else:
         return fib(n-1, passou_aqui) + fib(n-2, passou_aqui)
        

        
    
print(deivis_sequence(10))
