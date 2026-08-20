# Estructuras de Datos

## Qué vamos a ver

Cada estructura de este documento resuelve una limitación concreta de la anterior.

1. **Complejidad (Big-O)** — el lenguaje para decir "qué tan rápido es esto", antes de comparar nada.
2. **Arreglos** — acceso directo a cualquier posición, `O(1)`, pero insertar en medio es caro.
3. **Listas enlazadas** — insertar y quitar al inicio en `O(1)`, a cambio de perder el acceso directo.
4. **Pilas** — LIFO: lo último que entra es lo primero que sale (deshacer, la pila de llamadas).
5. **Colas** — FIFO: se respeta el orden de llegada (filas, colas de impresión).
6. **Heaps** — siempre entregan el elemento más urgente, sin importar cuándo llegó.
7. **Árboles** — datos con jerarquía natural, búsqueda en `O(log n)`.
8. **Grafos** — relaciones que no son jerárquicas: redes, mapas, conexiones.
9. **Tablas hash** — búsqueda por llave en `O(1)` en promedio, el techo práctico.
10. **Ordenamiento y búsqueda** — algoritmos que usan las estructuras anteriores como caja de herramientas.


---

## Complejidad: cómo comparar estructuras

Antes de ver la primera estructura, necesitamos un lenguaje común para decir "qué tan rápido es esto". Ese lenguaje es la **notación Big-O**: describe cómo crece el tiempo (o la memoria) de una operación cuando crece `n`, la cantidad de datos.

![Comparación de curvas de complejidad computacional: O(1), O(log n), O(raíz de n), O(n), O(n log n), O(n^2), O(2^n), O(n!)](img/bigo_chart.svg)

*Número de operaciones (eje vertical) según el tamaño de la entrada `n` (eje horizontal), para las complejidades más comunes. Autor: Cmglee, CC BY-SA 4.0 — Wikimedia Commons.*

Lean la gráfica de abajo hacia arriba: las curvas planas (`O(1)`, `O(log n)`) casi no suben aunque `n` crezca; las de en medio (`O(n)`, `O(n log n)`) suben más o menos parejo con `n`; y las de arriba (`O(n^2)`, `O(2^n)`) se disparan tan rápido que, para valores de `n` no muy grandes, salen literalmente de la gráfica.

| Notación | Nombre | Ejemplo |
|---|---|---|
| `O(1)` | Constante | acceder a `lista[i]` |
| `O(log n)` | Logarítmica | búsqueda binaria |
| `O(n)` | Lineal | recorrer una lista completa |
| `O(n log n)` | Casi lineal | `sorted(lista)` |
| `O(n^2)` | Cuadrática | comparar cada elemento contra todos los demás |

Ejemplo:

```python
import time

def busqueda_lineal(valores, objetivo):
    for i, v in enumerate(valores):
        if v == objetivo:
            return i
    return -1

for n in [1_000, 10_000, 100_000, 1_000_000]:
    valores = list(range(n))
    inicio = time.perf_counter()
    busqueda_lineal(valores, -1)  # peor caso: no está
    duracion = time.perf_counter() - inicio
    print(f"n={n:>9}  tiempo={duracion:.4f}s")
```

Al correrlo van a ver que el tiempo crece **proporcional a `n`**: eso es `O(n)` en la práctica.

`time` es parte de la librería estándar de Python. `time.perf_counter()` es un cronómetro de precisión: cada vez que lo llaman regresa un número que marca el instante actual. Para medir cuánto tarda algo, se lee el cronómetro **antes**, se ejecuta lo que se quiere medir, se lee el cronómetro **después**, y se restan los dos números — esa resta es el tiempo transcurrido:

```python
inicio = time.perf_counter()        # cronómetro: antes
busqueda_lineal(valores, -1)        # esto es lo que se mide
duracion = time.perf_counter() - inicio   # cronómetro: después, y se resta
```

### Cuando "finito" no es lo mismo que "posible"

`O(n^2)` ya duele. `O(2^n)` (exponencial) y `O(n!)` (factorial) no duelen: **son intratables**, aunque el resultado siga siendo un número finito y exacto, no infinito de verdad.

![El problema del trigo y el tablero de ajedrez: granos duplicandose en cada casilla](img/bigo_tablero_trigo.jpg)

*El problema del trigo y el tablero de ajedrez: 1 grano en la primera casilla, 2 en la segunda, 4 en la tercera... duplicando en cada una de las 64 casillas. Foto: McGeddon, CC BY-SA 4.0 — Wikimedia Commons.*

La leyenda cuenta que alguien pidió como pago 1 grano de trigo en la primera casilla de un tablero de ajedrez, 2 en la segunda, 4 en la tercera, duplicando en cada una de las 64 casillas. El total es `2^64 - 1`, aproximadamente 18.4 trillones de granos — más trigo del que se ha cosechado en **toda la historia de la humanidad**. El número es perfectamente finito y calculable (no es "infinito" matemáticamente), pero es *inalcanzable* en la práctica. Eso es exactamente lo que le pasa a un algoritmo `O(2^n)`: para una entrada de tamaño 64, ya no importa que tan rápida sea la computadora.

Otros dos ejemplos reales de lo mismo:

- **Romper una clave AES-256 probando todas las combinaciones:** hay `2^256` claves posibles. Aunque cada computadora en la Tierra hubiera estado probando claves sin parar desde el Big Bang (hace unos 13,800 millones de años), no alcanzarían a revisar una fracción significativa de todas las combinaciones.
- **El problema del viajante (TSP) por fuerza bruta:** con solo 20 ciudades hay `20!` rutas posibles (aproximadamente 2.4 trillones, es decir 2.4 seguido de 18 ceros). Una computadora que revise mil millones de rutas por segundo tardaría más de 77 años en revisarlas todas — y basta con agregar 5 ciudades más para que el tiempo se dispare a miles de millones de años.

La lección para este curso: cuando una estructura o un algoritmo es `O(n^2)` van a sentirlo (se pondrá lento), pero cuando es `O(2^n)` o `O(n!)` **ni siquiera van a poder terminar de correrlo** con una entrada moderadamente grande. Por eso elegir bien la estructura de datos —para que las operaciones frecuentes queden en `O(1)`, `O(log n)` o `O(n)` es lo que separa un programa que funciona de uno que nunca termina.

### Práctica: medir antes de razonar

1. Copien el código de arriba.
2. Agreguen esta función

   ```python
   def busqueda_en_set(valores, objetivo):
       return objetivo in valores
   ```

3. Dentro del `for n in [...]`, después de crear `valores` pero **antes de empezar a cronometrar**, agreguen una línea que convierta esa lista a un `set`:

   ```python
   valores_set = set(valores)
   ```

4. Completen el patrón de medición que ya tienen (`inicio = time.perf_counter()` ... `duracion = ...`) una segunda vez, pero llamando a `busqueda_en_set(valores_set, -1)` en vez de `busqueda_lineal(valores, -1)`. Al final de cada vuelta del `for` deben quedarles **dos tiempos impresos**, uno junto al otro, para el mismo `n`.
5. Corran el programa completo para `n = 1_000_000` y comparen los dos tiempos.
6. Respondan por escrito (2-3 líneas): ¿por qué la búsqueda en `set` es tan distinta? 

---

## Arreglos (arrays)

### Qué problema resuelve

Guardar varios valores del mismo tipo, uno junto al otro en memoria, para poder llegar a cualquiera de ellos **de un salto**, sin recorrer los anteriores.

### Cómo se ve por dentro

![Casilleros numerados en la estación de tren de Oulu, Finlandia](img/arreglos_lockers.jpg)

*Casilleros numerados, estación de tren de Oulu (Finlandia). Foto: Estormiz, dominio público (CC0) — Wikimedia Commons.*

Es la misma idea que un arreglo: cada casillero tiene una posición fija (81, 82, 83...) y para llegar al que quieren no recorren los demás — van directo. Eso es exactamente lo que hace `arreglo[i]`.

```
indice:   0    1    2    3    4
        [ 7 ][12 ][ 3 ][ 9 ][ 5 ]
```

Como están contiguos en memoria, la posición de `arreglo[i]` se calcula con una formula directa (`inicio + i * tamano_de_cada_elemento`), no buscando. Por eso el acceso es `O(1)`.

`list` de Python **no es** un arreglo clasico de tamaño fijo: es un arreglo dinámico que se agranda solo cuando hace falta. Aquí usamos el módulo `array` para ver un arreglo homogéneo y después volvemos a `list` con más contexto.

### Operaciones y su costo

| Operación | Complejidad | Por que |
|---|---:|---|
| Acceder `arreglo[i]` | O(1) | formula directa |
| Modificar `arreglo[i] = x` | O(1) | ídem |
| Buscar un valor | O(n) | hay que recorrer el arreglo 
| Insertar al final (si hay espacio) | O(1) | no mueve nada |
| Insertar al inicio o en medio | O(n) | hay que recorrer el arreglo completo |

### Dónde se usa en la vida real

- **Imagenes y video:** cada pixel de una foto se guarda en un arreglo (un "framebuffer"). Por eso leer el pixel de la fila 120, columna 45 es instantaneo, sin importar si la foto es de 1 o de 100 megapixeles.
- **Hojas de calculo:** cada celda de Excel o Google Sheets es, por dentro, `arreglo[fila][columna]`.
- **Procesamiento de audio:** una canción digital es un arreglo de miles de muestras de sonido por segundo; el reproductor necesita saltar a cualquier segundo al instante (arrastrar la barra de reproducción).

Se elige un arreglo cuando **se sabe de antemano cuántos elementos va a haber** (o casi) y se va a necesitar entrar directo a posiciones específicas muy seguido — el costo es que agregar o quitar en medio es caro.

### Implementación en Python

```python
from array import array

# 'i' = enteros. A diferencia de una lista, todos los elementos
# deben ser del mismo tipo.
edades = array('i', [20, 21, 19, 22])

print(edades[0])       # 20
edades[0] = 25
print(edades[0])       # 25

# array.array no acepta tipos mezclados:
# edades.append("veinte")  # TypeError
```

Un arreglo de tamaño fijo construido a pulso (para ver el limite explícitamente). Aquí usamos una `list` de Python como "memoria cruda" en vez de `array.array` a propósito: `array.array` obliga a elegir un tipo único desde el inicio (`'i'` para enteros, `'d'` para flotantes, etc.) y no acepta `None`, así que no podría representar una casilla "todavía vacía" como hace `self.datos = [None] * tamano` aquí abajo. Lo que hace que esto siga siendo un arreglo de verdad no es la clase de Python que usamos por dentro, sino la regla que nosotros imponemos: `tamano` se fija una vez en `__init__` y nunca cambia.

```python
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
a.obtener(10)           # IndexError, no hay posicion 10
```

### Práctica: arreglo de temperaturas

Usando `ArregloFijo`:

1. Creen un arreglo de capacidad 7 (una temperatura por día de la semana).
2. Llenenlo con 7 valores de prueba.
3. Escriban una función `temperatura_maxima(arreglo)` que recorra el arreglo y devuelva el valor más alto, **sin usar `max()`**.
4. Escriban una función `dia_mas_frio(arreglo)` que devuelva el **índice** del valor más bajo.
5. Intenten leer una posición fuera de rango (`arreglo.obtener(10)`) y expliquen en un comentario por qué el error es preferible a que el programa devuelva un valor incorrecto silenciosamente.

---

## Listas enlazadas

### Qué problema resuelve

Insertar y eliminar al **inicio** de la colección en `O(1)`, algo que un arreglo no puede hacer (ahí cuesta `O(n)` porque hay que recorrer todo). El costo a cambio: se pierde el acceso directo por índice.

### Cómo se ve por dentro

Cada elemento (**nodo**) guarda su valor y una referencia al siguiente.

![Enganche entre dos vagones de tren, Museo del Transporte Ferroviario de Nueva Gales del Sur](img/listas_vagones.jpg)

*Enganche entre vagones, Museo del Transporte Ferroviario de Nueva Gales del Sur, Australia. Foto: Maksym Kozlenko, CC BY-SA 4.0 — Wikimedia Commons.*

Un tren es una lista enlazada física: cada vagón solo sabe a qué vagón está enganchado *después* de el (su `siguiente`), no necesita saber nada de los demás. Para llegar al último vagón hay que pasar por todos los anteriores — no existe forma de "saltar" directo a la mitad del tren, a diferencia de un arreglo.

Cada casilla es un nodo con dos campos (valor y puntero al siguiente), y el último apunta a "nada" (representado aquí con una casilla tachada, equivalente al `None` de Python):

![Diagrama técnico de una lista enlazada simple con tres nodos](img/listas_diagrama.svg)

*Lista enlazada simple: cada nodo guarda un valor y una referencia al siguiente; el último apunta a null. Autor: Lasindi, dominio público — Wikimedia Commons.*


### Operaciones y su costo

| Operación | Complejidad | Por que |
|---|---:|---|
| Insertar al inicio | O(1) | solo cambia una referencia |
| Insertar al final (sin cola guardada) | O(n) | hay que recorrer hasta el final |
| Buscar un valor | O(n) | no hay atajos, se recorre nodo por nodo |
| Eliminar el primero | O(1) | ídem insertar al inicio |
| Acceder al elemento `i` | O(n) | no hay formula directa, hay que caminar |

### Dónde se usa en la vida real

- **Sistemas operativos:** la memoria libre de la computadora se administra con una "free list" — una lista enlazada de bloques de memoria disponibles. Cuando un programa pide memoria, el sistema recorre esa lista buscando un bloque suficientemente grande.
- **Blockchain:** cada bloque guarda una referencia (el hash) del bloque anterior. Es, literalmente, una lista enlazada donde no se puede alterar un eslabón sin romper la cadena completa.
- **Estructuras internas de lenguajes:** `LinkedList` de Java o las listas de Lisp/Scheme son listas enlazadas reales, no arreglos disfrazados como la `list` de Python.

Se elige una lista enlazada cuando **no se sabe cuántos elementos va a haber** y se van a insertar o quitar elementos seguido en posiciones que no son el final — el costo es que no hay acceso directo por índice.

### Implementación en Python

```python
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None  # None = todavia no esta conectado a ningun otro nodo


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None  # referencia al primer nodo; lista vacia si cabeza es None

    def insertar_al_inicio(self, valor):
        nuevo = Nodo(valor)
        # El orden de estas dos lineas importa: primero el nodo nuevo tiene
        # que apuntar a quien ERA la cabeza, y solo despues la lista puede
        # "olvidar" a la cabeza vieja y adoptar al nuevo. Si se invirtiera
        # el orden, se perderia la referencia al resto de la lista antes de
        # guardarla en algun lado, y quedaria inaccesible para siempre.
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def insertar_al_final(self, valor):
        nuevo = Nodo(valor)
        if self.cabeza is None:        # caso especial: la lista esta vacia,
            self.cabeza = nuevo        # el nodo nuevo es toda la lista
            return
        actual = self.cabeza
        # Caminar nodo por nodo hasta el ultimo: un nodo es el ultimo
        # cuando su "siguiente" es None. No hay forma de saltar directo
        # al final como en un arreglo, hay que recorrer todo.
        while actual.siguiente is not None:
            actual = actual.siguiente
        actual.siguiente = nuevo       # aqui "actual" ya es el ultimo nodo

    def buscar(self, valor):
        actual = self.cabeza
        # Patron base de recorrido, reutilizado (con variaciones) en
        # eliminar() y __str__(): arrancar en la cabeza, avanzar de a un
        # nodo con actual = actual.siguiente, y parar cuando actual llega
        # a None (se acabo la lista sin encontrar el valor).
        while actual is not None:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False

    def eliminar(self, valor):
        # Quitar un nodo de en medio exige RECONECTAR al nodo de antes con
        # el nodo de despues, saltandose al que se va. Por eso hacen falta
        # dos referencias avanzando juntas: "actual" (donde estoy parado)
        # y "anterior" (un paso atras de actual).
        anterior = None
        actual = self.cabeza
        while actual is not None:
            if actual.valor == valor:
                if anterior is None:
                    # No hubo "anterior": nunca nos movimos, asi que el
                    # nodo a eliminar es la cabeza misma. La cabeza salta
                    # directo al segundo nodo.
                    self.cabeza = actual.siguiente
                else:
                    # "anterior" se conecta directo con lo que sigue de
                    # "actual", brincandoselo por completo. Python destruye
                    # el nodo de "actual" solo, porque ya nadie lo referencia.
                    anterior.siguiente = actual.siguiente
                return True
            # No coincidio el valor: avanzar los dos punteros, EN ESTE
            # ORDEN. Si se moviera "actual" primero, "anterior" quedaria
            # apuntando un paso mas adelante de donde debe.
            anterior = actual
            actual = actual.siguiente
        return False

    def __str__(self):
        valores = []
        actual = self.cabeza
        while actual is not None:      # mismo patron de recorrido de siempre
            valores.append(str(actual.valor))
            actual = actual.siguiente
        return " -> ".join(valores) if valores else "(vacia)"


lista = ListaEnlazada()
lista.insertar_al_final(10)
lista.insertar_al_final(20)
lista.insertar_al_inicio(5)
print(lista)              # 5 -> 10 -> 20
lista.eliminar(10)
print(lista)              # 5 -> 20
```

Rastreando el ejemplo de arriba:

| Paso | Qué pasa | Estado |
|---|---|---|
| `ListaEnlazada()` | `cabeza = None` | `(vacia)` |
| `insertar_al_final(10)` | `cabeza is None` → caso especial, `10` se vuelve la cabeza | `10` |
| `insertar_al_final(20)` | `actual` camina hasta `10` (el último), le cuelga `20` | `10 -> 20` |
| `insertar_al_inicio(5)` | `5.siguiente = cabeza (10)`, luego `cabeza = 5` | `5 -> 10 -> 20` |
| `eliminar(10)` | `anterior=None,actual=5` no coincide → `anterior=5,actual=10` sí coincide → `5.siguiente = 20` | `5 -> 20` |

### Práctica: lista de reproducción

Extiendan `ListaEnlazada` con:

1. Un método `longitud(self)` que cuente los nodos **sin usar una variable global**, recorriendo la lista.
2. Un método `obtener(self, i)` que devuelva el valor en la posición `i` caminando desde `cabeza` (deben lanzar `IndexError` si `i` está fuera de rango).
3. Un método `invertir(self)` que invierta el orden de la lista **cambiando referencias**, no creando una lista nueva.
4. Prueben con 5 títulos de canciones como strings, por ejemplo `["Bohemian Rhapsody", "Imagine", "Hotel California", "Thriller", "Yesterday"]` (simulan una playlist: cada canción "conoce" solo a la siguiente, igual que cada nodo). Insértenlas en la lista, inviértanla, e impriman el resultado con `print(lista)`.

---

## Pilas (Stack)

### Qué problema resuelve

Procesar cosas en orden **LIFO** (Last In, First Out — el último que entró es el primero que sale). Aparece en deshacer/rehacer, la pila de llamadas de funciones, revisar paréntesis balanceados y navegación "atrás" del navegador.

### Cómo se ve por dentro

![Sillas apiladas de colores en una calle de Palamos, España](img/pilas_sillas.jpg)

*Sillas apiladas, Palamos, Cataluña. Foto: Kritzolina, CC BY-SA 4.0 — Wikimedia Commons.*

Para tomar la silla roja de hasta abajo, primero hay que quitar todas las que están encima. La última silla que se puso es siempre la primera que se puede quitar, así funciona una pila.

La secuencia completa de `push` y `pop`:

![Diagrama técnico de una pila: secuencia de push y pop](img/pilas_diagrama.svg)

*Una pila LIFO: cada `push` agrega arriba, cada `pop` quita de arriba — el orden de salida es exactamente el inverso del orden de entrada. Autor: Alhadis / Maxtremus, dominio público (CC0) — Wikimedia Commons.*
}

Solo se puede tocar la **cima**, no existe forma de leer o quitar el elemento de en medio o de abajo sin antes quitar todo lo que está encima.

### Dos formas de construir una pila por dentro

LIFO es una **regla de comportamiento**, no una estructura de datos concreta, se puede construir sobre cualquiera de las dos que ya conocen, y ambas dan operaciones `O(1)`:

- **Sobre un arreglo dinámico** (`list` de Python): la cima es siempre el **último** elemento de la lista. `push` es `append` (agregar al final); `pop` es `pop()` sin argumentos (quitar del final). Es la implementación de esta sección.
- **Sobre una lista enlazada** (la sección anterior): la cima es siempre la **cabeza**. `push` es exactamente `insertar_al_inicio`; `pop` es leer `cabeza.valor` y luego hacer `cabeza = cabeza.siguiente`. También `O(1)`, por la misma razón que insertar al inicio de una lista enlazada era barato: nunca hay que recorrer nada, solo mover una referencia.

La pila de llamadas real de un programa en ejecución (la que se llena hasta el "stack overflow" en una recursión sin caso base) es, a nivel de hardware, la primera variante: un bloque contiguo de memoria con un **stack pointer** (un registro del procesador) que sube o baja para marcar dónde está la cima, `push` y `pop` son, literalmente, mover ese puntero un espacio.

### Operaciones y su costo

| Operación | Complejidad | Qué hace |
|---|---:|---|
| `push(x)` | O(1) | agrega en la cima |
| `pop()` | O(1) | quita y devuelve la cima |
| `peek()` | O(1) | mira la cima sin quitarla |
| `esta_vacia()` | O(1) | verifica si hay elementos |

### Dónde se usa en la vida real

- **La pila de llamadas de cualquier programa:** cada vez que una función llama a otra, el sistema apila esa llamada; cuando termina, la desapila y regresa a donde iba. La recursión funciona exactamente por esto — y por eso una recursión sin caso base termina en "stack overflow": la pila de llamadas se llena.
- **Deshacer (Ctrl+Z):** Word, Photoshop y la mayoría de editores guardan cada acción en una pila; deshacer es un `pop()`.
- **El botón "Atrás" del navegador:** cada página que visitan se apila; "Atrás" desapila la última.
- **Compiladores y validadores:** revisar que el código tenga bien cerrados sus paréntesis, llaves y corchetes se resuelve con una pila.

Se elige una pila cuando se quiere procesar las cosas en orden inverso a como llegaron — lo último que entro es lo primero que se necesita.

### Implementación en Python

Con `list` (más simple: `append`/`pop` al final son O(1)):

```python
class Pila:
    def __init__(self):
        # Guardamos los datos en una list normal, pero con UNA regla
        # propia: el ULTIMO elemento de la lista siempre representa la
        # cima. Esa regla, no la clase list en si, es lo que hace que
        # esto sea una pila y no cualquier lista.
        self._datos = []

    def push(self, valor):
        # append() agrega al final == agregar a la cima. Es O(1) porque
        # Python reserva espacio de sobra al final del arreglo dinamico;
        # no hay que recorrer ni mover nada de lo que ya estaba.
        self._datos.append(valor)

    def pop(self):
        if self.esta_vacia():
            # No hay un "elemento vacio" razonable que devolver en su
            # lugar: lanzar un error es preferible a devolver None o 0
            # en silencio (mismo criterio que ArregloFijo con un indice
            # fuera de rango).
            raise IndexError("No se puede hacer pop de una pila vacia")
        # pop() sin argumentos quita y devuelve el ULTIMO elemento, O(1)
        # porque tampoco aqui hay que recorrer ni mover nada.
        return self._datos.pop()

    def peek(self):
        if self.esta_vacia():
            raise IndexError("Pila vacia")
        # Solo LEE la cima (indice -1), sin quitarla de la lista.
        return self._datos[-1]

    def esta_vacia(self):
        return len(self._datos) == 0


p = Pila()
p.push(1)
p.push(2)
p.push(3)
print(p.pop())   # 3
print(p.peek())  # 2
```

Nota: **no** usen `insert(0, x)` / `pop(0)` para simular una pila con `list` — eso mueve todos los elementos y convierte cada operación en `O(n)`. La cima de la pila siempre debe ser el **final** de la lista.

### Aplicación: paréntesis balanceados

```python
def parentesis_balanceados(texto):
    pila = Pila()
    # A cada simbolo de CIERRE le corresponde exactamente un simbolo de
    # APERTURA. El diccionario permite, al ver un cierre, preguntar: "lo
    # que acabo de sacar de la pila, es justo la apertura que le toca a
    # este cierre?".
    pares = {')': '(', ']': '[', '}': '{'}

    for caracter in texto:
        if caracter in "([{":
            # Toda apertura se apila: es una promesa pendiente de cierre.
            pila.push(caracter)
        elif caracter in ")]}":
            # Un cierre debe hacer pareja con la apertura MAS RECIENTE
            # que sigue sin cerrarse (la de hasta arriba de la pila) —
            # por eso una pila, y no una lista cualquiera, es la
            # estructura correcta para este problema.
            #
            # Dos formas distintas de fallar aqui:
            #   1) la pila ya esta vacia: sobra un cierre sin apertura
            #      que le corresponda (ej. el primer caracter de ")(" );
            #   2) pila.pop() saca una apertura que NO hace pareja con
            #      este cierre (ej. "(]" — sale "(" pero se esperaba "[").
            if pila.esta_vacia() or pila.pop() != pares[caracter]:
                return False

    # Al final, la pila debe quedar vacia: toda apertura que se metio
    # debe haber encontrado su cierre. Si sobra algo en la pila, es una
    # apertura que nunca se cerro (ej. "((").
    return pila.esta_vacia()


print(parentesis_balanceados("(a[b]{c})"))  # True
print(parentesis_balanceados("(a[b)c]"))    # False
print(parentesis_balanceados("(("))          # False, sobra un '('
```

### Práctica: verificador de expresiones + deshacer

1. Prueben `parentesis_balanceados` con 5 cadenas propias (mezclen casos válidos e inválidos).
2. Implementen una función `evaluar_postfix(expresión)` que reciba una expresión en notación postfija separada por espacios, por ejemplo `"3 4 + 2 *"` (equivale a `(3 + 4) * 2 = 14`), y la evalue usando una `Pila`. Pista: al recorrer token por token, si es número hacen `push`; si es operador, hacen `pop` dos veces, operan, y el resultado vuelve con `push`.
3. Simulen un "deshacer" de editor de texto: mantengan una `Pila` de estados (strings) cada vez que el usuario escribe algo nuevo, y un método `deshacer()` que regrese al estado anterior con `pop()`.

---

## Colas (Queue)

### Qué problema resuelve

Procesar cosas en orden **FIFO** (First In, First Out — el primero que entra es el primero que sale). Aparece en: fila de impresión, atención de tickets, y es la base del recorrido BFS que van a usar en grafos (sección Grafos).

### Cómo se ve por dentro

![Clientes esperando en fila para pagar en un supermercado de Nueva York](img/colas_fila.jpg)

*Fila para pagar, supermercado en Nueva York. Foto: David Shankbone, CC BY-SA 3.0 — Wikimedia Commons.*

El primero que se formo es el primero que paga. Nadie se salta la fila (idealmente) — eso es FIFO.

```
enqueue(10) -> |10|
enqueue(20) -> |10|20|
enqueue(30) -> |10|20|30|
dequeue()   -> devuelve 10, queda |20|30|
```

### Por que `list` es una mala cola

```python
cola = []
cola.append(10)
cola.append(20)
cola.pop(0)   # OK, pero O(n): mueve todos los elementos restantes
```

`pop(0)` es `O(n)` porque **todos** los elementos siguientes se recorren una posición. Para una cola de verdad se necesita una estructura donde quitar del frente sea `O(1)`.

### Operaciones y su costo (con la estructura correcta)

| Operación | Complejidad |
|---|---:|
| `enqueue(x)` | O(1) |
| `dequeue()` | O(1) |
| `frente()` | O(1) |

### Dónde se usa en la vida real

- **Colas de impresión:** si mandan a imprimir 3 documentos, el sistema operativo los guarda en una cola y los imprime en el orden en que llegaron, sin importar cuál terminó de "cargar" primero.
- **Sistemas de mensajería entre servidores:** RabbitMQ, Kafka o Amazon SQS son, en esencia, colas gigantes: un servicio mete tareas (`enqueue`) y otro las va procesando en orden (`dequeue`) — así funcionan, por ejemplo, los pagos o notificaciones que se procesan "en segundo plano" en una app.
- **Atención a clientes:** sistemas de tickets de soporte técnico procesan las solicitudes en el orden en que entraron.

Se elige una cola cuando el **orden de llegada debe respetarse** — lo contrario de una pila.

### Implementación en Python

Python trae `collections.deque` (doble cola), pensada exactamente para esto:

```python
from collections import deque

class Cola:
    def __init__(self):
        self._datos = deque()

    def enqueue(self, valor):
        self._datos.append(valor)

    def dequeue(self):
        if self.esta_vacia():
            raise IndexError("No se puede hacer dequeue de una cola vacia")
        return self._datos.popleft()

    def frente(self):
        if self.esta_vacia():
            raise IndexError("Cola vacia")
        return self._datos[0]

    def esta_vacia(self):
        return len(self._datos) == 0


c = Cola()
c.enqueue("A")
c.enqueue("B")
c.enqueue("C")
print(c.dequeue())  # A
print(c.frente())   # B
```

### Práctica: simulador de fila de atención

1. Simulen una fila del banco: `Cola` de nombres. Metan 6 nombres.
2. Atiendan (con `dequeue`) a 3 personas y muestren en pantalla quién fue atendido y en qué orden.
3. Implementen una **cola circular de tamaño fijo** usando una `list` de tamaño `n` y dos índices (`frente` y `final`) que avanzan con `% n` (el operador módulo). Debe lanzar un error si intentan meter un elemento cuando ya está llena.

---

## Colas de prioridad (heaps)

### Qué problema resuelve

A veces no importa quién llegó primero, sino quién es **más urgente**. Una cola de prioridad siempre entrega el elemento de mayor (o menor) prioridad, sin importar el orden de llegada.

### Cómo se ve por dentro

Se implementa con un **heap**: un árbol binario casi-completo donde cada nodo es menor o igual que sus hijos (heap mínimo) o mayor o igual que sus hijos (heap máximo). Guardado en un arreglo, sin necesitar nodos ni referencias explícitas.

![Heap máximo representado como árbol y como arreglo](img/heap_maxheap.svg)

*Heap máximo: arriba, como árbol; abajo, la misma información guardada como arreglo (así se implementa de verdad). Autor: Ermishin, CC BY-SA 3.0 — Wikimedia Commons.*

Piensen en una fila de urgencias: no importa el orden en que llegaron los pacientes, siempre se atiende primero al más grave. Eso es un heap mínimo por gravedad — o, visto al reves, un heap máximo por urgencia.

### Operaciones y su costo

| Operación | Complejidad |
|---|---:|
| Insertar | O(log n) |
| Extraer el mínimo (o máximo) | O(log n) |
| Ver el mínimo (o máximo) | O(1) |

Comparen esto contra "ordenar la lista completa cada vez que se agrega algo" (`O(n log n)` por inserción): el heap es mucho más barato porque no ordena todo, solo mantiene la propiedad mínima (o máxima) de arriba.

### Dónde se usa en la vida real

- **Planificador de procesos de un sistema operativo:** cuando varios programas compiten por el procesador, el sistema no los atiende por orden de llegada (eso sería una cola) sino por prioridad — un heap.
- **GPS y mapas (Google Maps, Waze):** el algoritmo de Dijkstra para encontrar la ruta más corta usa un heap para siempre expandir, de entre todos los caminos posibles a medio explorar, el más corto hasta ahora.
- **Compresión de archivos:** el algoritmo de Huffman (usado dentro de ZIP y JPEG) arma su árbol de compresión sacando repetidamente, con un heap, los dos símbolos menos frecuentes.

Se elige un heap cuando se necesita repetidamente **"dame el más urgente/pequeño/grande de todos"**, sin necesitar la lista completa ordenada.

### Implementación en Python

Python trae `heapq`, que convierte una lista común en un heap mínimo:

```python
import heapq

tareas = []
heapq.heappush(tareas, (2, "revisar correos"))
heapq.heappush(tareas, (1, "atender incendio"))
heapq.heappush(tareas, (3, "planear la siguiente semana"))

while tareas:
    prioridad, descripcion = heapq.heappop(tareas)
    print(prioridad, descripcion)

# 1 atender incendio
# 2 revisar correos
# 3 planear la siguiente semana
```

La tupla `(prioridad, descripción)` funciona porque Python compara tuplas elemento por elemento: primero por prioridad.

### Práctica: sala de urgencias

1. Modelen una sala de urgencias con `heapq`: cada paciente entra como `(nivel_gravedad, nombre)`, donde `1` es lo más grave.
2. Inserten 6 pacientes en un orden de llegada que **no** coincida con su gravedad.
3. Atiendan (extraigan) a todos e impriman el orden real de atención.
4. Respondan por escrito: si hubieran usado una `Cola` normal (FIFO) en vez de un heap, ¿qué hubiera pasado con el paciente más grave si llegó de último?

---

## Árboles

### Qué problema resuelve

Organizar datos con una relación **jerárquica** (no lineal como listas/pilas/colas), y en particular, el **árbol binario de búsqueda (BST)** permite buscar, insertar y eliminar en `O(log n)` en promedio — mucho mejor que el `O(n)` de una lista, siempre que el árbol este razonablemente balanceado.

### Cómo se ve por dentro

![Árbol genealógico simple de la familia Grey](img/arboles_familia.svg)

*Árbol genealógico de ejemplo. Autores: Josef Sábl cz y Mysid, CC BY-SA 3.0 — Wikimedia Commons.*

Un árbol genealógico es la analogía más directa: Lucas Grey (la raíz) tiene hijos, esos hijos tienen sus propios hijos, y así sucesivamente — nadie tiene más de un padre, y no hay ciclos. Un árbol binario de búsqueda es un árbol genealógico con una regla extra de orden.

```
        8
      /   \
     3     10
    / \      \
   1   6      14
      / \    /
     4   7  13
```

Regla del BST: para cualquier nodo, todo lo de su **subárbol izquierdo es menor**, todo lo de su **subárbol derecho es mayor**.

### Operaciones y su costo

| Operación | Complejidad (árbol balanceado) | Complejidad (peor caso) |
|---|---:|---:|
| Buscar | O(log n) | O(n) |
| Insertar | O(log n) | O(n) |
| Eliminar | O(log n) | O(n) |

El peor caso ocurre cuando el árbol degenera en una lista (por ejemplo, si insertan datos ya ordenados uno tras otro). Esto es exactamente por lo que existen los árboles auto-balanceados (AVL, rojo-negro) — mención para un curso más avanzado, no lo construimos aquí.

### Dónde se usa en la vida real

- **El sistema de archivos de su computadora:** carpetas dentro de carpetas dentro de carpetas es, literalmente, un árbol. `C:\Usuarios\ana\Documentos\tarea.docx` es una ruta desde la raíz hasta una hoja.
- **El HTML de cualquier página web:** el navegador construye un árbol (el DOM) donde `<html>` es la raíz, `<body>` es su hijo, y cada etiqueta dentro es hija de la que la contiene. Cuando JavaScript "recorre el DOM", está recorriendo un árbol.
- **Bases de datos reales:** MySQL, PostgreSQL y SQLite indexan sus tablas con variantes de árboles (B-tree, B+tree) precisamente para que un `WHERE id = 42` sea O(log n) en vez de tener que revisar cada fila.

Se elige un árbol cuando los datos tienen una **relación jerárquica natural** y se necesita buscar rápido dentro de esa jerarquía.

### Implementación en Python

```python
class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        self.raiz = self._insertar(self.raiz, valor)

    def _insertar(self, nodo, valor):
        if nodo is None:
            return NodoArbol(valor)
        if valor < nodo.valor:
            nodo.izquierdo = self._insertar(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            nodo.derecho = self._insertar(nodo.derecho, valor)
        return nodo  # valores iguales no se duplican

    def buscar(self, valor):
        return self._buscar(self.raiz, valor)

    def _buscar(self, nodo, valor):
        if nodo is None:
            return False
        if valor == nodo.valor:
            return True
        if valor < nodo.valor:
            return self._buscar(nodo.izquierdo, valor)
        return self._buscar(nodo.derecho, valor)

    def in_orden(self):
        resultado = []
        self._in_orden(self.raiz, resultado)
        return resultado

    def _in_orden(self, nodo, resultado):
        if nodo is None:
            return
        self._in_orden(nodo.izquierdo, resultado)
        resultado.append(nodo.valor)
        self._in_orden(nodo.derecho, resultado)


arbol = ArbolBinarioBusqueda()
for v in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
    arbol.insertar(v)

print(arbol.buscar(6))     # True
print(arbol.buscar(100))   # False
print(arbol.in_orden())    # [1, 3, 4, 6, 7, 8, 10, 13, 14] -- ¡ordenado!
```

El recorrido `in_orden` (izquierda, nodo, derecha) siempre entrega los valores de un BST ya ordenados — esa es la razón de ser de la regla "menor a la izquierda, mayor a la derecha".

Los otros dos recorridos clasicos:

```python
def pre_orden(nodo, resultado):
    """nodo, izquierda, derecha -- util para copiar la forma del arbol"""
    if nodo is None:
        return
    resultado.append(nodo.valor)
    pre_orden(nodo.izquierdo, resultado)
    pre_orden(nodo.derecho, resultado)


def post_orden(nodo, resultado):
    """izquierda, derecha, nodo -- util para borrar el arbol de forma segura"""
    if nodo is None:
        return
    post_orden(nodo.izquierdo, resultado)
    post_orden(nodo.derecho, resultado)
    resultado.append(nodo.valor)
```

### Práctica: agenda de contactos ordenada

1. Construyan un `ArbolBinarioBusqueda` e inserten 10 nombres (strings — Python compara strings alfabéticamente, así que el BST funciona igual).
2. Agreguen un método `altura(self)` que calcule la altura del árbol (número de niveles) usando recursión: altura de un nodo vacío es 0; altura de un nodo es `1 + max(altura(izq), altura(der))`.
3. Inserten los mismos 10 nombres pero ya ordenados alfabéticamente en un árbol nuevo, y comparen la altura contra el árbol del paso 1.
4. Expliquen en una línea por qué la altura cambió tanto, conectándolo con la fila "peor caso" de la tabla de arriba.

---

## Grafos

### Qué problema resuelve

Modelar relaciones que **no son jerárquicas**: redes sociales, mapas de ciudades, dependencias entre tareas, páginas web enlazadas entre si. Un árbol es, de hecho, un caso particular de grafo (sin ciclos, con una raíz).

### Cómo se ve por dentro

Un grafo tiene **nodos (vértices)** y **conexiones (aristas)** entre ellos. Pueden tener dirección (A -> B distinto de B -> A) o no, y pueden tener peso (costo de la conexión) o no.

![Grafo simple de 6 nodos numerados conectados por aristas](img/grafos_6n.svg)

*Grafo no dirigido de ejemplo, 6 vértices. Autor: AzaToth, dominio público — Wikimedia Commons.*

Piensen en el mapa del metro: cada estación es un nodo, cada tramo de vía entre dos estaciones es una arista. No hay una sola "raíz" ni una jerarquía — cualquier estación puede conectar con cualquier otra, y puede haber más de un camino entre dos puntos. Eso es lo que distingue a un grafo de un árbol.

```
   A --- B
   |     |
   C --- D --- E
```

### Representaciones

**Lista de adyacencia** (la más común, eficiente cuando hay pocas conexiones respecto al total posible):

```python
grafo = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C", "E"],
    "E": ["D"],
}
```

Un grafo **es** ese diccionario, con una definición formal encima.

**Matriz de adyacencia** (más simple de razonar, pero gasta memoria `O(n^2)` sin importar cuántas conexiones haya realmente):

```python
#      A  B  C  D  E
matriz = [
    [0, 1, 1, 0, 0],  # A
    [1, 0, 0, 1, 0],  # B
    [1, 0, 0, 1, 0],  # C
    [0, 1, 1, 0, 1],  # D
    [0, 0, 0, 1, 0],  # E
]
```

### Recorridos: BFS y DFS

**BFS (Breadth-First Search, recorrido por niveles)** usa una **Cola** (sección Colas) — explora todos los vecinos directos antes de avanzar más lejos. Sirve para encontrar el camino **más corto** en número de saltos.

```python
from collections import deque

def bfs(grafo, inicio):
    visitados = {inicio}
    cola = deque([inicio])
    orden = []

    while cola:
        actual = cola.popleft()
        orden.append(actual)
        for vecino in grafo[actual]:
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append(vecino)

    return orden


print(bfs(grafo, "A"))  # ['A', 'B', 'C', 'D', 'E']
```

**DFS (Depth-First Search, recorrido en profundidad)** usa una **Pila** (sección Pilas) — o recursión, que internamente usa la pila de llamadas — se mete lo más lejos posible antes de retroceder.

```python
def dfs(grafo, inicio, visitados=None, orden=None):
    if visitados is None:
        visitados = set()
        orden = []

    visitados.add(inicio)
    orden.append(inicio)

    for vecino in grafo[inicio]:
        if vecino not in visitados:
            dfs(grafo, vecino, visitados, orden)

    return orden


print(dfs(grafo, "A"))  # ['A', 'B', 'D', 'C', 'E']
```

Noten que **la única diferencia estructural entre BFS y DFS es Cola vs. Pila** — es la razón por la que estas dos secciones se vieron antes que esta.

### Operaciones y su costo

| Operación | Lista de adyacencia | Matriz de adyacencia |
|---|---:|---:|
| ¿Existe arista A-B? | O(grado de A) | O(1) |
| Recorrer todos los vecinos de A | O(grado de A) | O(n) |
| Memoria total | O(n + aristas) | O(n^2) |

### Dónde se usa en la vida real

- **Google Maps / Waze:** calles y cruces son nodos y aristas (con peso: la distancia o el tiempo estimado). Cuando piden una ruta, el sistema corre un algoritmo de camino más corto (una versión mejorada de BFS con pesos) sobre ese grafo.
- **Redes sociales:** en Facebook o LinkedIn cada persona es un nodo y cada amistad/conexión es una arista. Sugerencias como "personas que quizá conozcas" se calculan buscando nodos a poca distancia en el grafo (amigos de amigos).
- **Internet mismo:** cada router es un nodo, cada cable o enlace es una arista; los paquetes de datos viajan buscando el camino más corto disponible en ese momento.
- **Sistemas de recomendación:** Netflix o Spotify modelan usuarios y contenidos como un grafo para encontrar patrones ("a quienes les gusto X también les gusto Y").

Se elige un grafo cuando las relaciones entre los datos **no son jerárquicas** — cualquier elemento puede conectarse con cualquier otro, sin una raíz única.

### Práctica: red de amistades

1. Modelen una red de 8 personas (nodos) con al menos 10 amistades (aristas) usando lista de adyacencia, asumiendo que la amistad es mutua (si A es amigo de B, agreguen la conexión en ambos sentidos).
2. Usen `bfs` para encontrar el orden en que la información de un rumor llegaría a todos desde una persona inicial.
3. Escriban una función `estan_conectados(grafo, origen, destino)` que devuelva `True`/`False` usando BFS o DFS (reutilicen el código de arriba, no necesitan reinventar el recorrido).
4. Agreguen una persona que no tenga ninguna amistad con el resto y comprueben que `estan_conectados` devuelve `False` hacia ella.

---

## Tablas hash

### Qué problema resuelve

Buscar, insertar y eliminar en **O(1) en promedio**, sin importar cuántos elementos haya — el salto respecto al `O(n)` de listas y `O(log n)` de árboles balanceados. Es la estructura detras de `dict` y `set` de Python.

Con esto ya pueden responder la práctica de "medir antes de razonar" (sección Complejidad) con precisión.

### Cómo se ve por dentro

Una **función hash** convierte una llave (string, número, lo que sea) en un índice de un arreglo interno. Guardar `"Ana": 20` es, en el fondo: calcular `hash("Ana") % tamano_del_arreglo` y poner el par ahí.

![Diagrama de una tabla hash: nombres como llaves, números de teléfono como valores](img/hash_tabla.svg)

*Tabla hash de ejemplo: cada nombre (llave) se convierte en un índice mediante la función hash, y ahí se guarda su valor asociado. Autor: Jorge Stolfi, CC BY-SA 3.0 — Wikimedia Commons.*

Es exactamente como una guía telefónica hecha al revés: en vez de ordenar los nombres alfabéticamente y buscar hoja por hoja (eso sería O(log n) si está bien ordenada, O(n) si no), la función hash calcula de una sola vez en qué "página" debería estar cada nombre.

```
hash("Ana")  % 8  ->  posicion 3
hash("Luis") % 8  ->  posicion 6

arreglo interno:
[None, None, None, ("Ana", 20), None, None, ("Luis", 21), None]
```

### El problema de las colisiones

Dos llaves distintas pueden caer en la misma posición (`hash("Ana") % 8 == hash("Eva") % 8`, por ejemplo). La solución más común es **encadenamiento**: cada posición del arreglo guarda una lista de pares, no un solo par.

```
posicion 3: [("Ana", 20), ("Eva", 19)]
```

Si la función hash reparte bien las llaves y el arreglo no está demasiado lleno, cada posición tiene en promedio 0 o 1 elementos — por eso el costo promedio sigue siendo `O(1)`. Si la función hash es mala (todo cae en la misma posición), degenera a `O(n)`: una lista enlazada disfrazada.

### Operaciones y su costo

| Operación | Promedio | Peor caso |
|---|---:|---:|
| Insertar | O(1) | O(n) |
| Buscar | O(1) | O(n) |
| Eliminar | O(1) | O(n) |

### Dónde se usa en la vida real

- **Diccionarios de casi cualquier lenguaje:** el `dict` de Python, el `HashMap` de Java, los objetos `{}` de JavaScript — todos son tablas hash por dentro. Cuando escriben `edades["Ana"]` están usando exactamente esta estructura.
- **Cachés de alta velocidad:** Redis y Memcached guardan resultados ya calculados (por ejemplo, la respuesta de una consulta cara a una base de datos) indexados por una llave, para responder en O(1) la siguiente vez que se pida lo mismo.
- **Verificación de contraseñas:** los sistemas no guardan la contraseña, guardan su hash. Al iniciar sesión, se calcula el hash de lo que escribieron y se compara — nunca se guarda ni compara el texto original.
- **Compiladores:** la "tabla de símbolos" que relaciona cada nombre de variable con su tipo y dirección de memoria es una tabla hash.

Se elige una tabla hash cuando la operación más frecuente es **buscar por una llave exacta** (no por rango, no ordenado) y se necesita que ese costo no crezca aunque crezcan muchísimo los datos.

### Implementación en Python

```python
class TablaHash:
    def __init__(self, capacidad=8):
        self.capacidad = capacidad
        self.cubetas = [[] for _ in range(capacidad)]

    def _indice(self, llave):
        return hash(llave) % self.capacidad

    def insertar(self, llave, valor):
        cubeta = self.cubetas[self._indice(llave)]
        for i, (k, _) in enumerate(cubeta):
            if k == llave:
                cubeta[i] = (llave, valor)  # ya existia, se reemplaza
                return
        cubeta.append((llave, valor))

    def buscar(self, llave):
        cubeta = self.cubetas[self._indice(llave)]
        for k, v in cubeta:
            if k == llave:
                return v
        raise KeyError(llave)

    def eliminar(self, llave):
        cubeta = self.cubetas[self._indice(llave)]
        for i, (k, _) in enumerate(cubeta):
            if k == llave:
                del cubeta[i]
                return
        raise KeyError(llave)


tabla = TablaHash()
tabla.insertar("Ana", 20)
tabla.insertar("Luis", 21)
print(tabla.buscar("Ana"))    # 20
tabla.eliminar("Ana")
tabla.buscar("Ana")           # KeyError
```

Esto es, a grandes rasgos, lo que hace `dict` por dentro (con muchas optimizaciones adicionales que Python ya trae resueltas).

### Práctica: contador de votos

1. Usen `TablaHash` (la de arriba, no `dict`) para contar votos de una elección: cada voto es un string con el nombre del candidato.
2. Simulen 20 votos repartidos entre 4 candidatos (pueden generarlos con `random.choice`).
3. Cuando un candidato ya tiene votos registrados, su conteo debe **incrementarse**, no reemplazarse — van a necesitar leer el valor actual con `buscar` antes de volver a `insertar`, o modificar el método `insertar` para que sepa sumar.
4. Al final, recorran las `cubetas` de la tabla e impriman cuántas de las 8 posiciones quedaron vacías y cuántas tienen más de un candidato (colisión). Conecten el resultado con la sección "El problema de las colisiones".

---

## Ordenamiento y búsqueda

### Por que van aquí, al final

Los algoritmos de ordenamiento y búsqueda **usan** las estructuras anteriores como caja de herramientas (arreglos, y en el caso de mergesort, listas divididas recursivamente). Verlos ahora conecta todo lo anterior.

### Busqueda

**Lineal** — funciona en cualquier lista, ordenada o no:

```python
def busqueda_lineal(valores, objetivo):
    for i, v in enumerate(valores):
        if v == objetivo:
            return i
    return -1
```

**Binaria** — requiere la lista **ya ordenada**, pero a cambio pasa de `O(n)` a `O(log n)`:

```python
def busqueda_binaria(valores, objetivo):
    izquierda, derecha = 0, len(valores) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if valores[medio] == objetivo:
            return medio
        elif valores[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1


valores = [1, 3, 4, 6, 7, 8, 10, 13, 14]
print(busqueda_binaria(valores, 7))   # 4
print(busqueda_binaria(valores, 100)) # -1
```

Esto es exactamente la misma idea que bajar por un BST (sección Árboles): descartar la mitad de las opciones en cada paso.

### Ordenamiento: uno simple, uno eficiente

**Insertion sort** — simple de razonar, `O(n^2)`, útil para entender el concepto:

```python
def insertion_sort(valores):
    for i in range(1, len(valores)):
        actual = valores[i]
        j = i - 1
        while j >= 0 and valores[j] > actual:
            valores[j + 1] = valores[j]
            j -= 1
        valores[j + 1] = actual
    return valores


print(insertion_sort([5, 2, 9, 1, 5, 6]))  # [1, 2, 5, 5, 6, 9]
```

**Merge sort** — `O(n log n)`, divide y vencerás

```python
def merge_sort(valores):
    if len(valores) <= 1:
        return valores

    medio = len(valores) // 2
    izquierda = merge_sort(valores[:medio])
    derecha = merge_sort(valores[medio:])

    return _combinar(izquierda, derecha)


def _combinar(izquierda, derecha):
    resultado = []
    i = j = 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado


print(merge_sort([5, 2, 9, 1, 5, 6]))  # [1, 2, 5, 5, 6, 9]
```

### Práctica: comparar en la práctica

1. Generen una lista de 5,000 números aleatorios (`random.sample` o `random.randint` en un ciclo).
2. Ordenen una copia con `insertion_sort` y otra copia con `merge_sort`, cronometrando cada una con `time.perf_counter()` (mismo patrón de la sección Complejidad).
3. Comparen los tiempos y expliquen la diferencia en términos de `O(n^2)` vs `O(n log n)`.
4. Sobre la lista ya ordenada, usen `busqueda_binaria` para buscar 3 valores que sepan que existen y 1 que sepan que no existe. Confirmen que los índices devueltos son correctos revisando `valores[índice]`.

---

## Cómo seguir

El orden de este documento no es casualidad: cada estructura resuelve una limitación concreta de la anterior.

```
Arreglo (acceso O(1), insertar al inicio O(n))
   -> Lista enlazada (insertar al inicio O(1), pierde acceso directo)
        -> Pila / Cola (casos de uso concretos de listas enlazadas/arreglos)
             -> Heap (cola, pero por prioridad en vez de orden de llegada)
                  -> Árbol (jerarquía, búsqueda O(log n))
                       -> Grafo (relaciones generales, no solo jerárquicas)
                            -> Tabla hash (búsqueda O(1), el techo práctico)
```

Con esto ya tienen las piezas para leer implementaciones reales (por ejemplo, por qué `dict` de Python es una tabla hash, o por qué `sorted()` usa una variante de merge sort llamada Timsort) y para elegir con criterio, en un problema nuevo, cuál estructura conviene según qué operación van a hacer **más seguido**.
