def quitarEspacios(texto):
    texto = texto.replace(" ", "").lower()
    return texto


def reverse(texto):
    resultado = ""
    for _ in texto[::-1]:  # for _ in texto:
        resultado += _  # resultado = char + resultado (esto es la forma tradicional)
    return resultado


def es_palindromo(texto):
    texto = quitarEspacios(texto)
    texto1 = reverse(texto)
    if texto == texto1:  #
        return True  #
    else:  #
        return False  # return texto == texto1 (ya regresa verdadero o falso mas rapido)


print("Hola mundo", es_palindromo("Hola mundo"))
