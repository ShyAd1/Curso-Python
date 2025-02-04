class Perro:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.edad = edad

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, newNombre):
        self.__nombre = newNombre

    def habla(self):
        print(f"{self.__nombre} dice: Guau!")

    @classmethod
    def factory(cls):
        return cls("Chanchito feliz", 4)


perro1 = Perro.factory()
perro1.habla()
print(perro1.get_nombre())
