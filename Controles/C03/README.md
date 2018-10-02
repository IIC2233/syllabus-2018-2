# Pauta C03

## Verdadero y Falso (1.5 pts)

* 0.25 pts cada uno.

1) Un nodo es una unidad básica de datos.

**R:** Verdadero.

2) Una clase abstracta no está pensada para ser instanciada directamente.

**R:** Verdadero.

3) La cantidad de pasos para obtener la posición de un nodo en una lista ligada, es proporcional a la posición en la que está dicho nodo.

**R:** Verdadero.

4) El nivel d de un árbol binario posee a lo más 2^d nodos, considerando que el nivel de la raíz es cero.

**R:** Verdadero.

5) La estrategia de recorrido BFS consiste en recorrer cada nivel del árbol, en orden de jerarquía, antes de pasar al siguiente.

**R:** Verdadero.

6) El problema del diamante en inglés a veces se le llama *deadly diamond of death*.

**R:** Verdadero.

## Desarrollo Rápido (1.0 pts)

1) Explica brevemente el problema del diamante. **(0.5 pts)**

**Ejemplo de respuesta:** Ambigüedad que surge cuando dos clases (por ej. B y C) heredan de A y a su vez otra clase (D) hereda de B y C a la vez, cuando se llama a un método en D que es de A.

**Distribución del puntaje:**

* **0.25 pts** por decir en qué estructura de clases se produce este problema.
* **0.25 pts** por decir que no es claro qué implementación se usa de un método, o que haciendo llamadas explícitas a los métodos en las clases madre en vez de usar super, puede llamar dos veces al método implementado en A.

2) Explique brevemente por qué un árbol es considerado una estructura recursiva. **(0.5 pts)**

**Respuestas aceptadas:**

-  Porque cada parte de un árbol es a su vez un árbol.
-  Porque cada nodo es, a su vez, la raíz de un sub-árbol formado por él y sus hijos.

## Sobre la Actividad (1.5 pts)

- ¿Cuáles son los elementos y el orden de la jerarquía presentada en la actividad? **(0.75 pts)**

**R:** Los elementos son las entidades (o guerreros) del ejército y el orden de la jerarquía es General, Teniente, Mayor, Capitán y Soldado (pueden escribirlo inverso).

**Distribución de puntajes:**

- Correcto: **0,75 pts**.
- Correctos con 1 swap:	**0,55 pts**.
- Correctos sin orden: **0,20 pts**.
- Entidad faltante (descuento): **-0,30 pts**.
- 3 entidades o menos o cualquier otra cosa: **0 pts**.

PS: El puntaje final no puede ser negativo.

- ¿Qué se está buscando maximizar al asignar un subalterno con su superior? **(0.75 pts)**

**R:** Puede decir la afinidad **y/o** los ítems que tienen en común.

## Lectura de código (2.0 pts)

**Forma 1:**

```python
class Nodo:

    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None


class EstructuraDieciochera:

    def __init__(self):
        self.inicio = self.fin = None
        self._len = 0

    def agregar(self, valor, pos=None):
        nodo = Nodo(valor)
        if not self._len:
            self.inicio = self.fin = nodo
            self._len += 1
            return

        fin = self.fin
        fin.siguiente = nodo
        self.fin = nodo
        self._len += 1

    def foo(self):
        primer_len = len(self.inicio.valor)
        actual = self.inicio
        while actual.siguiente:
            actual = actual.siguiente
            if primer_len <= len(actual.valor):
                yield actual.valor


bar = EstructuraDieciochera()
bar.agregar("le pegaron")
bar.agregar("su puñete")
bar.agregar("al guatón Loyola")
bar.agregar("por dársela")
bar.agregar("de encacha'o")
bar.agregar("comadre Lola")

for x in bar.foo():
    print(x)

```

**Forma 2:**

```python
class Nodo:

    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None


class EstructuraDieciochera:

    def __init__(self):
        self.inicio = self.fin = None
        self._len = 0

    def agregar(self, valor, pos=None):
        nodo = Nodo(valor)
        if not self._len:
            self.inicio = self.fin = nodo
            self._len += 1
            return

        fin = self.fin
        fin.siguiente = nodo
        self.fin = nodo
        self._len += 1

    def foo(self):
        primer_len = len(self.inicio.valor)
        actual = self.inicio
        while actual.siguiente:
            actual = actual.siguiente
            if primer_len >= len(actual.valor):
                yield actual.valor


bar = EstructuraDieciochera()
bar.agregar("comadre Lola")
bar.agregar("por dársela")
bar.agregar("su puñete")
bar.agregar("le pegaron")
bar.agregar("de encacha'o")
bar.agregar("al guatón Loyola")

for x in bar.foo():
    print(x)

```

**Forma 3:**

```python
class Nodo:

    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None


class EstructuraDieciochera:

    def __init__(self):
        self.inicio = self.fin = None
        self._len = 0

    def agregar(self, valor, pos=None):
        nodo = Nodo(valor)
        if not self._len:
            self.inicio = self.fin = nodo
            self._len += 1
            return

        fin = self.fin
        fin.siguiente = nodo
        self.fin = nodo
        self._len += 1

    def foo(self):
        primer_len = len(self.inicio.valor)
        actual = self.inicio
        while actual.siguiente:
            actual = actual.siguiente
            if primer_len <= len(actual.valor):
                yield actual.valor


bar = EstructuraDieciochera()
bar.agregar("por dársela")
bar.agregar("comadre Lola")
bar.agregar("su puñete")
bar.agregar("al guatón Loyola")
bar.agregar("le pegaron")
bar.agregar("de encacha'o")

for x in bar.foo():
    print(x)

```

- ¿Qué estructura de datos se está implementando (parcialmente) por la clase `EstructuraDieciochera`? **(0.5 pts)**

**R:** Lista **ligada**. (Árbol unario está bien. Doblemente ligada está mal.)

- Indique el output del código. **(1.5 pts)**

Algo importante que notar era que nunca se imprimía el primer elemento.

**Puntajes Forma 1:**

| Output | Puntaje | Comentario |
|:------:|:-----:|:----------:|
| | 0.2 | por no imprimir "le pegaron"|
| | 0.2 | por no imprimir "su puñete"|
| "al guatón Loyola" | 0.2 | |
| "por dársela" | 0.2 | |
| "de encacha'o" | 0.2 | |
| "comadre Lola" | 0.2 | |
| | 0.3 | por todo correcto |

**Puntajes Forma 2:**

| Output | Puntaje | Comentario |
|:------:|:-----:|:----------:|
| | 0.2 | por no imprimir "comadre Lola"|
| "por dársela" | 0.2 | |
| "su puñete" | 0.2 | |
| "le pegaron" | 0.2 | |
| "de encacha'o" | 0.2 | |
| | 0.2 | por no imprimir "al guatón Loyola"|
| | 0.3 | por todo correcto |

**Puntajes Forma 3:**

| Output | Puntaje | Comentario |
|:------:|:-----:|:----------:|
| | 0.2 | por no imprimir "por dársela"|
| "comadre Lola" | 0.2 | |
| | 0.2 | por no imprimir "su puñete"|
| "al guatón Loyola" | 0.2 | |
| | 0.2 | por no imprimir "le pegaron"|
| "de encacha'o" | 0.2 | |
| | 0.3 | por todo correcto |
