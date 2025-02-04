try:
    n1 = int(input("Ingresa pimer número: "))
except Exception as e:
    print("Ocurrió un error!")
else:
    print("No ocurrió ningn error")
finally:
    print("Se ejecuta siempre")
