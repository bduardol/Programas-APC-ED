def verificarletra(frase):
    frase1 = ''.join(char for char in frase if char.isalnum())
    for letra in range(len(frase1)):
        if frase1[letra] == frase1[letra].upper():
            return True
    return False
    
    
    
    
    
    
    
    
