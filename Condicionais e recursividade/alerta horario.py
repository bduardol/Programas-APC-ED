def alerta(a,b):
    if a == b:
        print(f'Ja chegou o disco voador!!!!')
    else:
        print(f'Ta sussa, {a} horas ainda.')
        alerta(a+1,b)
        return
    
alerta(16,20)