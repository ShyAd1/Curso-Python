mascotas = ["Wolfgang", "Pelusa", "Pulga", "Felipe", "Pulga", "Chanchito feliz"]

mascotas.insert(1, "Melvin")
mascotas.append("Chanchito triste")

mascotas.remove("Pulga")
mascotas.pop(1)
print(mascotas)
del mascotas[0]
mascotas.clear()
print(mascotas)
