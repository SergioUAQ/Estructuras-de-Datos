import time

def busqueda_lineal(valores, objetivo):
    for i, v in enumerate(valores):
        if v == objetivo:
            return i
    return -1

def busqueda_en_set(valores, objetivo):
    return objetivo in valores

for n in [1_000, 10_000, 100_000, 1_000_000]:
    valores = list(range(n))
    valores_set = set(valores)  # conversión FUERA del cronómetro

    inicio = time.perf_counter()
    busqueda_lineal(valores, -1)
    duracion_lista = time.perf_counter() - inicio

    inicio = time.perf_counter()
    busqueda_en_set(valores_set, -1)
    duracion_set = time.perf_counter() - inicio

    print(f"n={n:>9}  lista={duracion_lista:.4f}s  set={duracion_set:.6f}s")
