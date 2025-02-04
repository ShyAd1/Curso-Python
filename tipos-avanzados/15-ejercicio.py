def deleteSpaces(texto):
    texto = texto.replace(" ", "").lower()
    lista = list(texto)
    return lista


def countDictionary(lista):
    diccionario = {}
    for char in lista:
        diccionario[char] = lista.count(char)
    return diccionario


def orderDictionary(diccionario):
    lista1 = []
    lista2 = []
    lista3 = []
    for llave, char in diccionario.items():
        lista1 = [llave, char]
        lista2 += [lista1]
    lista2.sort(key=lambda el: el[1], reverse=True)
    for lista in lista2:
        lista3 += [tuple(lista)]
    return lista3


def biggerTupla(listat):
    lista = []
    cont = 1
    for tuplas in listat:
        if cont < len(listat) and tuplas[1] == listat[cont][1]:
            lista += [tupla]
            cont += 1
        else:
            lista += [listat[cont - 1]]
            break
    return lista


oracion = "Hola mundo este es mi string"
sinEspacios = deleteSpaces(oracion)
print(sinEspacios)
conteoDiccionario = countDictionary(sinEspacios)
print(conteoDiccionario)
listaDeTuplas = orderDictionary(conteoDiccionario)
print(listaDeTuplas)
mayorListaDeTuplas = biggerTupla(listaDeTuplas)

print("Los caracteres que mas se repiten son:")
for tupla in mayorListaDeTuplas:
    print(f"- {tupla[0].upper()} con {tupla[1]} repeticiones")
