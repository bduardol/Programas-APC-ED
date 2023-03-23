u = ['o', 'ô', 'õ', 'ó','ò','ø','ö']
def não_possui_a_letra_o(palavra):
    strn = palavra.lower()
    for letra in u:
        if letra in strn:
            return False
    return True


print(não_possui_a_letra_o("asdfasij uooo"))