def positivo():
    a = int(input())
    if (-100 <= a < 0):
        print('Que negatividade...')
        positivo()
    elif (0 < a <= 100):
        print('Viva a positividade!')
    else:
        return

positivo()