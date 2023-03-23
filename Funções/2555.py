def vestimentas (bota,chapeu):
    import math
    a = math.factorial(2) / (math.factorial(bota) * math.factorial(2-bota))
    b = math.factorial(2) / (math.factorial(chapeu) * math.factorial(2-chapeu))
    x = a * b
    
vestimentas(2,2)