u = ['o', 'ô', 'õ', 'ó','ò','ø','ö']
x = int()
def não_possui_a_letra_o(palavra):
    x = 0
    palavra = palavra.lower()
    for letra in u:
        if letra in palavra[] and not letra.isdecimal():
            x = 1
            var = bool(False)
        else:
            var2 = bool(True)
    if x == 1:
        return var
    else:
        return var2
print(não_possui_a_letra_o("ajsdjasjdu"))