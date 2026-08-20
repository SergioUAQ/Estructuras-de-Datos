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
    valores_set = set(valores)
    inicio = time.perf_counter()
    busqueda_lineal(valores, -1)  # peor caso: no está
    duracion = time.perf_counter() - inicio
    inicio2 = time.perf_counter()
    busqueda_en_set(valores_set, -1)
    duracion2 = time.perf_counter() - inicio2
    print(f"n={n:>9}  tiempo={duracion:.4f}s tiempo2={duracion2:.10f}s")
