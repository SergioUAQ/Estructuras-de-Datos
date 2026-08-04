# Introduccion a Python para Estructuras de Datos

**Materia:** Estructuras de Datos y Modelos Discretos

---

## 1. Como estudiar este repaso

Python se aprende entendiendo tres ideas:

1. **Dato:** que valor tengo y que tipo representa.
2. **Operacion:** que puedo hacer con ese dato.
3. **Estructura:** como organizo muchos datos para resolver un problema.

---

## 2. Entorno minimo

Verificar Python:

```bash
python3 --version
```

Ejecutar un archivo:

```bash
python3 programa.py
```

Usar el interprete interactivo:

```bash
python3
```

Salir del interprete:

```python
exit()
```

Primer programa:

```python
print("Hola Mundo")
print("Estructuras de Datos")
```
Ejemplo:

```python
edad = 20

if edad >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")
```

La sangria es parte de la sintaxis.

---

## 3. Variables, objetos y nombres

En Python una variable es un **nombre** que apunta a un objeto.

```python
x = 10
nombre = "Ana"
activo = True
```

No se declara el tipo antes del nombre. Python lo determina a partir del valor.

```python
x = 10
print(type(x))      # <class 'int'>

x = "diez"
print(type(x))      # <class 'str'>
```

Esto es flexible, pero exige disciplina. Para estructura de datos conviene que una variable conserve un significado claro.

Mal:

```python
x = 10
x = [1, 2, 3]
x = "resultado"
```

Mejor:

```python
cantidad = 10
valores = [1, 2, 3]
mensaje = "resultado"
```

Regla practica: si el nombre de la variable no explica para que sirve, el codigo se vuelve dificil de depurar.

---

## 4. Tipos fundamentales

### Enteros

```python
a = 42
b = -7
c = 1_000_000
```

En Python, `int` no tiene un limite fijo como `int32_t` o `uint32_t` en C++. Puede crecer mientras haya memoria disponible.

```python
grande = 2 ** 100
print(grande)
```

### Flotantes

```python
temperatura = 23.5
promedio = 8.75
```

`float` usa representacion de punto flotante. No todos los decimales se representan exactamente:

```python
print(0.1 + 0.2)
```


### Booleanos

```python
activo = True
error = False
```

Operadores logicos:

```python
a = True
b = False

print(a and b)  # False
print(a or b)   # True
print(not a)    # False
```

Python tambien usa evaluacion de corto circuito:

```python
def revisar():
    print("Se ejecuto revisar")
    return True

estado = False

if estado and revisar():
    print("Activo")
```

Como `estado` es `False`, `revisar()` no se ejecuta.

### Cadenas

```python
nombre = "Ana"
materia = 'Estructuras de Datos'
```

Concatenar:

```python
print("Hola, " + nombre)
```

Interpolar con f-strings:

```python
edad = 20
print(f"{nombre} tiene {edad} años")
```

Acceder por indice:

```python
texto = "Python"
print(texto[0])   # P
print(texto[-1])  # n
```

Las cadenas son **inmutables**:

```python
texto = "Python"
# texto[0] = "J"  # Error
texto = "J" + texto[1:]
```

---

## 5. Entrada y salida

Salida:

```python
print("Hola")
print("Valor:", 10)
```

Entrada:

```python
nombre = input("Nombre: ")
print(f"Hola, {nombre}")
```

`input()` siempre devuelve texto (`str`). Si se necesita un numero, hay que convertir:

```python
edad = int(input("Edad: "))
print(edad + 10)
```

Para decimal:

```python
altura = float(input("Altura: "))
```

Si el usuario escribe algo invalido, la conversion falla:

```python
numero = int("abc")  # ValueError
```

Mas adelante se puede manejar con `try / except`.

---

## 6. Operadores

### Aritmeticos

```python
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a // b)  # 3, division entera
print(a % b)   # 1, modulo
print(a ** b)  # 1000, potencia
```

El modulo `%` es clave para:

- saber si un numero es par o impar;
- recorrer arreglos circulares;
- implementar colas circulares;
- repartir elementos en buckets de una tabla hash.

```python
n = 7
if n % 2 == 0:
    print("par")
else:
    print("impar")
```

### Comparaciones

```python
x = 10
y = 5

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
```

Python permite encadenar comparaciones:

```python
edad = 20

if 18 <= edad <= 30:
    print("Rango valido")
```

### Operaciones bit a bit

Python conserva los operadores bit a bit:

| Operacion | Operador | Ejemplo |
|---|---|---|
| AND | `&` | `a & b` |
| OR | `|` | `a | b` |
| XOR | `^` | `a ^ b` |
| NOT | `~` | `~a` |
| Desplazar izquierda | `<<` | `a << 2` |
| Desplazar derecha | `>>` | `a >> 2` |

Ejemplo:

```python
registro = 0b10101101_11100110_00010101_00110010

sensor = registro & 0xFFF
estado = (registro >> 12) & 1
error = (registro >> 13) & 1
modo = (registro >> 14) & 0b11
temperatura = (registro >> 16) & 0xFF
checksum = (registro >> 24) & 0xFF

print(f"sensor: {sensor}")
print(f"estado: {estado}")
print(f"error: {error}")
print(f"modo: {modo}")
print(f"temperatura cruda: {temperatura}")
print(f"checksum: {checksum}")
```

Visualizar binario:

```python
print(format(registro, "032b"))
```

Extraer un campo de bits entre las posiciones `inicio` y `fin`:

```python
def extraer_bits(valor, inicio, fin):
    ancho = fin - inicio + 1
    mascara = (1 << ancho) - 1
    return (valor >> inicio) & mascara

modo = extraer_bits(registro, 14, 15)
```

Esta funcion ya tiene forma de algoritmo reutilizable: recibe datos, aplica pasos y devuelve resultado.

---

## 7. Control de flujo

### `if / elif / else`

```python
numero = int(input("Numero: "))

if numero < 0:
    print("negativo")
elif numero == 0:
    print("cero")
else:
    print("positivo")
```

No hay `switch` tradicional en versiones antiguas de Python. Para menus simples, se puede usar `if / elif`.

```python
opcion = input("Opcion: ")

if opcion == "1":
    print("Saludar")
elif opcion == "2":
    print("Mostrar datos")
elif opcion == "3":
    print("Salir")
else:
    print("Opcion invalida")
```

Tambien existe `match` en Python moderno:

```python
opcion = input("Opcion: ")

match opcion:
    case "1":
        print("Saludar")
    case "2":
        print("Mostrar datos")
    case "3":
        print("Salir")
    case _:
        print("Opcion invalida")
```

### Expresion condicional

Equivalente al ternario de C++:

```python
x = 15
resultado = 100 if x > 10 else 0
print(resultado)
```

### `for`

Recorrer una lista:

```python
valores = [10, 20, 30]

for valor in valores:
    print(valor)
```

Recorrer indices:

```python
valores = [10, 20, 30]

for i in range(len(valores)):
    print(i, valores[i])
```

Recorrer indice y valor:

```python
for i, valor in enumerate(valores):
    print(i, valor)
```

`range(n)` genera valores desde `0` hasta `n - 1`:

```python
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4
```

### `while`

Se usa cuando no se sabe de antemano cuantas iteraciones habra.

```python
numeros = []

while True:
    n = int(input("Numero, 0 para terminar: "))
    if n == 0:
        break
    numeros.append(n)

print(numeros)
```

`break` termina el ciclo. `continue` salta a la siguiente iteracion.

```python
for n in [1, 2, 3, 4, 5]:
    if n == 3:
        continue
    print(n)
```

---

## 8. Listas: el arreglo dinamico de Python


```python
valores = [2, 7, 9]

print(len(valores))  # 3
print(valores[0])    # 2
print(valores[1])    # 7

valores[1] = 4
print(valores)       # [2, 4, 9]
```

Indice negativo:

```python
print(valores[-1])   # ultimo elemento
```

Agregar:

```python
valores.append(10)
```

Eliminar ultimo:

```python
ultimo = valores.pop()
```

Insertar en una posicion:

```python
valores.insert(1, 99)
```

Eliminar por valor:

```python
valores.remove(99)
```

Vaciar:

```python
valores.clear()
```

### Costo aproximado de operaciones en listas

| Operacion | Complejidad | Comentario |
|---|---:|---|
| `valores[i]` | O(1) | Acceso directo por indice |
| `append(x)` | O(1) amortizado | Agregar al final |
| `pop()` | O(1) | Quitar del final |
| `insert(0, x)` | O(n) | Desplaza elementos |
| `pop(0)` | O(n) | Desplaza elementos |
| `x in valores` | O(n) | Busqueda lineal |

Esto importa porque estructura de datos no es solo "guardar cosas"; tambien es elegir operaciones eficientes.

### Copias

Asignar no copia la lista:

```python
a = [1, 2, 3]
b = a

a[0] = 99
print(b)  # [99, 2, 3]
```

`a` y `b` apuntan al mismo objeto.

Copia superficial:

```python
a = [1, 2, 3]
b = a.copy()

a[0] = 99
print(b)  # [1, 2, 3]
```

En listas anidadas hay que tener cuidado:

```python
matriz = [[0, 0], [0, 0]]
copia = matriz.copy()

matriz[0][0] = 1
print(copia)  # [[1, 0], [0, 0]]
```

Para copias profundas:

```python
import copy

copia = copy.deepcopy(matriz)
```

---

## 9. Tuplas, conjuntos y diccionarios

### Tuplas

Una tupla es una secuencia inmutable:

```python
punto = (3, 4)
x, y = punto
```

Sirve para representar pares, coordenadas, aristas o retornos multiples.

```python
def dividir(a, b):
    cociente = a // b
    residuo = a % b
    return cociente, residuo

q, r = dividir(17, 5)
```

### Conjuntos

Un conjunto guarda valores unicos.

```python
visitados = set()

visitados.add("A")
visitados.add("B")
visitados.add("A")

print(visitados)  # {'A', 'B'}
```

Operaciones utiles:

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # union
print(a & b)  # interseccion
print(a - b)  # diferencia
```

En grafos, `set` se usa mucho para recordar nodos visitados.

### Diccionarios

Un diccionario guarda pares llave-valor.

```python
edades = {
    "Ana": 20,
    "Luis": 21,
}

print(edades["Ana"])
edades["Marta"] = 19
```

Recorrer:

```python
for nombre, edad in edades.items():
    print(nombre, edad)
```

Uso en estructuras de datos:

```python
grafo = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": [],
    "D": [],
}
```

El diccionario permite modelar relaciones sin crear todavia clases.

---

## 10. Funciones

Una funcion encapsula una idea.

```python
def media(a, b):
    return (a + b) / 2

print(media(2, 6))
```

Funcion sin retorno explicito:

```python
def saludar(nombre):
    print(f"Hola, {nombre}")
```

Si una funcion no tiene `return`, devuelve `None`.

Parametros con valor por defecto:

```python
def escalar(valor, factor=1.5):
    return valor * factor

print(escalar(2))     # 3.0
print(escalar(2, 3))  # 6
```

Nombrar argumentos:

```python
def crear_usuario(nombre, edad, activo=True):
    return {"nombre": nombre, "edad": edad, "activo": activo}

usuario = crear_usuario(edad=20, nombre="Ana")
```

### Contratos

Al disenar una funcion hay que pensar:

- **Precondiciones:** que debe cumplirse antes de llamarla.
- **Postcondiciones:** que promete devolver o modificar.
- **Invariantes:** que no debe cambiar.

Ejemplo:

```python
def primero(valores):
    """Devuelve el primer elemento de una lista no vacia."""
    if len(valores) == 0:
        raise ValueError("La lista no debe estar vacia")
    return valores[0]
```

En estructuras de datos esto es esencial: no es lo mismo hacer `pop()` en una pila con elementos que en una pila vacia.

### Type hints

Python permite anotar tipos:

```python
def suma(a: int, b: int) -> int:
    return a + b
```

No obliga al interprete a verificar tipos en tiempo de ejecucion, pero documenta la intencion y ayuda a editores.

```python
def promedio(valores: list[float]) -> float:
    return sum(valores) / len(valores)
```

---

## 11. Recursion

Una funcion recursiva se llama a si misma. Necesita:

1. Caso base.
2. Paso recursivo.

Factorial:

```python
def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n - 1)
```

Suma de una lista:

```python
def suma_recursiva(valores):
    if len(valores) == 0:
        return 0
    return valores[0] + suma_recursiva(valores[1:])
```

Esta version es clara, pero no siempre eficiente porque `valores[1:]` crea una copia.

Mejor con indice:

```python
def suma_desde(valores, i=0):
    if i == len(valores):
        return 0
    return valores[i] + suma_desde(valores, i + 1)
```


```python
def contar_nodos(nodo):
    if nodo is None:
        return 0
    return 1 + contar_nodos(nodo.izq) + contar_nodos(nodo.der)
```

---

## 12. Errores y excepciones

Python detiene el programa cuando ocurre una excepcion no manejada.

```python
numero = int("abc")  # ValueError
```

Manejo basico:

```python
try:
    numero = int(input("Numero: "))
    print(10 / numero)
except ValueError:
    print("Debes escribir un entero")
except ZeroDivisionError:
    print("No se puede dividir entre cero")
```

Lanzar una excepcion:

```python
def desapilar(pila):
    if len(pila) == 0:
        raise IndexError("No se puede desapilar una pila vacia")
    return pila.pop()
```

En estructuras de datos, los errores no deben esconderse. Una operacion invalida debe ser clara.

---

## 13. Archivos y modulos

Un modulo es un archivo `.py` que puede importarse.

Archivo `utilidades.py`:

```python
def es_par(n):
    return n % 2 == 0
```

Archivo `main.py`:

```python
from utilidades import es_par

print(es_par(10))
```

Estructura recomendada para practicas:

```text
practica/
├── main.py
├── estructuras.py
└── pruebas.py
```

Separar archivos ayuda a distinguir:

- uso del programa (`main.py`);
- implementacion de estructuras (`estructuras.py`);
- validacion (`pruebas.py`).

---

## 14. Clases y objetos

Una clase define un tipo propio.

```python
class Sensor:
    def __init__(self, nombre, valor=0):
        self.nombre = nombre
        self.valor = valor

    def leer(self):
        return self.valor

    def actualizar(self, nuevo_valor):
        self.valor = nuevo_valor
```

Uso:

```python
s = Sensor("temperatura", 25)
print(s.leer())
s.actualizar(27)
print(s.leer())
```

`self` representa al objeto actual.

Para estructuras de datos, las clases permiten modelar nodos.

```python
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
```

Crear nodos enlazados:

```python
a = Nodo(10)
b = Nodo(20)
c = Nodo(30)

a.siguiente = b
b.siguiente = c
```

Recorrer:

```python
actual = a

while actual is not None:
    print(actual.valor)
    actual = actual.siguiente
```

Esta es la base de una lista enlazada.

### `dataclass`

Para clases que principalmente guardan datos:

```python
from dataclasses import dataclass

@dataclass
class Punto:
    x: int
    y: int

p = Punto(3, 4)
print(p)
```

Para nodos:

```python
from dataclasses import dataclass

@dataclass
class Nodo:
    valor: int
    siguiente: "Nodo | None" = None
```

---

## Estilo mínimo para entregar practicas

Usar nombres claros:

```python
temperaturas = [23.5, 24.0, 22.8]
promedio = sum(temperaturas) / len(temperaturas)
```

Evitar nombres genericos sin contexto:

```python
x = [23.5, 24.0, 22.8]
y = sum(x) / len(x)
```

Separar logica en funciones:

```python
def promedio(valores):
    if len(valores) == 0:
        raise ValueError("No se puede calcular promedio de lista vacia")
    return sum(valores) / len(valores)
```

Usar bloque principal:

```python
def main():
    valores = [10, 20, 30]
    print(promedio(valores))

if __name__ == "__main__":
    main()
```

Este patron permite importar funciones desde otros archivos sin ejecutar todo el programa.

---

## Prácticas

### Práctica 1: entrada, salida y tipos

Escribe un programa que:

1. Pida nombre, edad y promedio.
2. Imprima un reporte con f-string.
3. Indique si el estudiante es mayor de edad.
4. Indique si el promedio es aprobatorio.

Conceptos: `input`, `int`, `float`, `bool`, `if`.

### Practica 2: clasificador de numeros

Pide numeros hasta que el usuario escriba `0`. Al final muestra:

1. cantidad de numeros ingresados;
2. cuantos fueron positivos;
3. cuantos fueron negativos;
4. cuantos fueron pares;
5. suma total.

Conceptos: `while`, listas, acumuladores, modulo.

### Practica 3: manipulacion de listas

Con una lista de enteros:

```python
valores = [12, 5, 9, 20, 1, 15]
```

Calcula sin usar funciones magicas al inicio:

1. minimo;
2. maximo;
3. suma;
4. promedio;
5. cantidad de valores mayores que 10.

Luego compara con `min`, `max`, `sum` y `len`.

Conceptos: recorrido, acumuladores, busqueda lineal.

### Practica 4: frecuencias

Pide una frase y cuenta cuantas veces aparece cada palabra.

Ejemplo:

```text
python es claro python es util
```

Salida esperada aproximada:

```python
{"python": 2, "es": 2, "claro": 1, "util": 1}
```

Conceptos: `split`, diccionarios, conteo.

### Practica 5: bits en Python

Usa este registro:

```python
registro = 0b10101101_11100110_00010101_00110010
```

Extrae:

| Bits | Campo |
|---|---|
| 0-11 | valor del sensor |
| 12 | estado |
| 13 | error |
| 14-15 | modo |
| 16-23 | temperatura cruda |
| 24-31 | checksum |

Conceptos: `&`, `>>`, mascaras, funciones.

### Practica 6: pila

Implementa una pila usando lista y funciones:

- `apilar(pila, valor)`
- `desapilar(pila)`
- `ver_tope(pila)`
- `esta_vacia(pila)`

Valida que `desapilar` y `ver_tope` no funcionen silenciosamente con una pila vacia.

Conceptos: LIFO, `append`, `pop`, manejo de errores.

### Practica 7: cola

Implementa una cola con `collections.deque`:

- `encolar(cola, valor)`
- `desencolar(cola)`
- `ver_frente(cola)`
- `esta_vacia(cola)`

Simula una fila de atencion con nombres.

Conceptos: FIFO, `append`, `popleft`.

### Practica 8: nodos

Crea tres nodos enlazados manualmente:

```text
10 -> 20 -> 30 -> None
```

Luego recorre desde el primer nodo e imprime los valores.

Conceptos: clases, referencias, lista enlazada.

### Practica 9: grafo basico

Representa este grafo con diccionario:

```text
A -> B, C
B -> D
C -> D
D -> E
E -> []
```

Implementa DFS y BFS.

Conceptos: diccionario, conjunto, pila/cola, recorrido.

---

## Complejidad: el puente hacia la materia

La pregunta central de estructuras de datos no es solo "funciona?", sino:

> Cuanto tarda y cuanta memoria usa cuando crece la cantidad de datos?

Ejemplo:

```python
def buscar_lineal(valores, objetivo):
    for valor in valores:
        if valor == objetivo:
            return True
    return False
```

Si la lista tiene `n` elementos, en el peor caso se revisan `n` elementos. Complejidad: **O(n)**.

Acceso por indice:

```python
valores = [10, 20, 30]
print(valores[1])
```

Complejidad: **O(1)**.

Tabla de referencia inicial:

| Operacion | Estructura Python | Complejidad promedio |
|---|---|---:|
| Acceso por indice | `list` | O(1) |
| Agregar al final | `list.append` | O(1) amortizado |
| Buscar valor | `x in list` | O(n) |
| Insertar al inicio | `list.insert(0, x)` | O(n) |
| Agregar/quitar extremos | `collections.deque` | O(1) |
| Buscar llave | `dict` | O(1) promedio |
| Pertenencia | `set` | O(1) promedio |

Estas complejidades guian decisiones:

- Si necesito acceder por posicion: lista.
- Si necesito cola eficiente: `deque`.
- Si necesito busqueda rapida por llave: diccionario.
- Si necesito evitar duplicados: conjunto.

---

## Preguntas de cierre

1. Que diferencia hay entre una lista y una tupla?
2. Por que `pop(0)` en una lista puede ser costoso?
3. Cuando conviene usar un diccionario?
4. Que significa que dos variables apunten a la misma lista?
5. Cual es el caso base de una funcion recursiva?
6. Por que una pila se puede implementar facilmente con una lista?
7. Por que una cola conviene implementarla con `deque`?
8. Que ventaja tiene separar un algoritmo en funciones?
9. Como se relaciona un nodo enlazado con una lista enlazada?
10. Que significa O(n)?

---

## Checklist antes de continuar con estructuras de datos

Antes de iniciar listas enlazadas, pilas, colas, arboles y grafos, el estudiante debe poder:

- Ejecutar un archivo `.py` desde terminal.
- Usar `print`, `input`, `int`, `float` y `str`.
- Escribir condiciones con `if / elif / else`.
- Escribir ciclos `for` y `while`.
- Recorrer listas por valor, por indice y con `enumerate`.
- Usar `append`, `pop`, `len` y acceso por indice.
- Entender la diferencia entre asignar una lista y copiarla.
- Usar diccionarios para mapear llaves a valores.
- Usar conjuntos para evitar duplicados.
- Escribir funciones con parametros y retorno.
- Explicar un caso base en recursion.
- Crear una clase simple con `__init__`.
- Enlazar objetos mediante referencias.
- Leer una tabla simple de complejidad Big-O.

Si estos puntos estan claros, el grupo ya esta listo para implementar estructuras de datos en Python.
