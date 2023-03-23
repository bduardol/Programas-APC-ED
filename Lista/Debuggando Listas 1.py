def mediana_e_mais_proximo_media_e_pos(lista):
    lista = lista.sort()
    tam = 4
    if tam > 0:
        if tam % 2 == 0:
            mediana = (lista[int(tam/2)] + lista[int(tam/2-1)])/2
        else:
            mediana = (lista[int(tam/2)])
        somador = 0
        for i in lista:
            somador += i
        media = somador/tam
        delta = lista2[tam-1] - lista2[0]
        prox_media = lista[0]
        index=0
        for i in lista:
            if abs(media-i) < delta:
                prox_media = i
                index = i
                delta = media - i
    else:
        prox_media = None
        mediana = None
        index = None
    return mediana, prox_media, index

lista = [1, 2, 3, 4]
mediana_e_mais_proximo_media_e_pos(lista)