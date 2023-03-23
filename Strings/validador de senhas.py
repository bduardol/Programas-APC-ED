def validar1(sequencia):
    if len(sequencia) >= 6 and len(sequencia)<= 32:
        while True:
            if sequencia.isalpha():
                print("Senha invalida.")
                break
            elif sequencia.isdecimal():
                print("Senha invalida.")
                break
            elif sequencia.isalnum():
                validador(sequencia)
                break
            else:
                print("Senha invalida.")
                break
    else:
        print('Senha invalida.')
            
def validador(senha):
    x = 0
    x1 = 0
    x2 = 0
    x3 = 0
    for letra in range(len(senha)):
        if senha[letra].isalpha() == (senha[letra] == senha[letra].upper()):
            x = 1 
    for letra in range(len(senha)):
        if senha[letra].isalpha() == (senha[letra] == senha[letra].lower()):
            x1 = 1
    for letra in range(len(senha)):
        if senha[letra].isdigit():
            x2 = 1
    for letra in range(len(senha)):
        if senha[letra].isalnum():
            x3 = 1
    result = x*x1*x2*x3
    if result == 0:
        print('Senha invalida.')
    elif result == 1:
        print('Senha valida.')
    
validar1(input())