u = ['u', 'ú', 'ù', 'û','ü']
x = int()
def não_possui_a_letra_u(palavra):
    x = 0
    palavra = palavra.lower()
    for letra in palavra:
        if letra in u:
            x = 1
            var = bool(False)
        else:
            var2 = bool(True)
    if x == 1:
        return var
    else:
        return var2

print(não_possui_a_letra_u("ü"))