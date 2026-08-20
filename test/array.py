class ArregloFijo:
    def __init__(self, tamano):
        self.datos = [None] * tamano
        self.tamano = tamano

    def obtener(self, i):
        if not (0 <= i < self.tamano):
            raise IndexError("Indice fuera de rango")
        return self.datos[i]

    def asignar(self, i, valor):
        if not (0 <= i < self.tamano):
            raise IndexError("Indice fuera de rango")
        self.datos[i] = valor


a = ArregloFijo(5)
a.asignar(0, 100)
print(a.obtener(0))     # 100
a.obtener(10)       
