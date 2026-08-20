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


# 1. Arreglo de capacidad 7 (una temperatura por día de la semana)
temperaturas = ArregloFijo(7)

# 2. Llenarlo con 7 valores de prueba
valores_prueba = [21.5, 23.0, 19.8, 25.2, 24.0, 18.5, 22.3]
for i in range(7):
    temperaturas.asignar(i, valores_prueba[i])


# 3. Valor más alto, sin usar max()
def temperatura_maxima(arreglo):
    maximo = arreglo.obtener(0)
    for i in range(1, arreglo.tamano):
        if arreglo.obtener(i) > maximo:
            maximo = arreglo.obtener(i)
    return maximo


# 4. Índice del valor más bajo
def dia_mas_frio(arreglo):
    indice_minimo = 0
    for i in range(1, arreglo.tamano):
        if arreglo.obtener(i) < arreglo.obtener(indice_minimo):
            indice_minimo = i
    return indice_minimo


dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

print("Temperaturas:", valores_prueba)
print("Temperatura máxima:", temperatura_maxima(temperaturas))

indice_frio = dia_mas_frio(temperaturas)
print(f"Día más frío: {dias[indice_frio]} (índice {indice_frio}), con {temperaturas.obtener(indice_frio)} grados")

# 5. Leer una posición fuera de rango
try:
    indice_que_no_existe = 10
    temperaturas.obtener(indice_que_no_existe)
except IndexError as error:
    # El error es preferible a un valor incorrecto silencioso porque avisa
    # inmediatamente que el programa está mal (pidiendo una posición que no
    # existe), en vez de dejar pasar el bug y devolver, por ejemplo, None
    # o un dato de otra parte de la memoria sin que nadie se dé cuenta.
    # Un error visible se corrige rápido; un valor incorrecto silencioso
    # puede arrastrarse por el resto del programa y dar resultados falsos
    # mucho más difíciles de rastrear.
    print(f"Error esperado al pedir la posición que no existe ({indice_que_no_existe}): {error}")
