# Pauta C04
## Verdadero y Falso

**Rúbrica:**

- **0,15 ptos.** por cada Verdadera o Falsa correcta.
- **0,15 ptos.** por cada justificación bien hecha
    - **0,05 ptos.** si la justificación tiene errores importantes.
    - **0,15 ptos.** en caso de que la justificación sea la correcta.

**1. El uso de un conjunto de tests permite determinar que no habrá errores en el programa.**

**R: Falso.** Los tests son sólo casos particulares de una _infinidad_ de posibles casos a probar. De todas formas, sí nos permiten obtener mayor seguridad acerca del correcto funcionamiento de nuestro código.
Quienes respondan que _podría_ ser verdadero se considera erróneo dado que no se puede tener certeza de cubrir todos los casos, según la justificación puede tener hasta 0.05 siguiendo la lógica.

**2. Al buscar un camino entre dos vértices distintos de un grafo, el algoritmo DFS nos asegurará que, si existiese uno, entonces retornará el camino más corto.**

**R: Falso.** El algoritmo no asegura el camino más corto al contrario de BFS.
En caso de dar un contraejemplo, decir que no lo asegura o nombrar BFS se considera como correcto.

**3. En una matriz de adyacencia, el grado de un vértice en particular se puede obtener al sumar los valores de la fila o de la columna de ese vértice.**

**R: Verdadero.**

**4. En un grafo dirigido, una _lista de adyacencia_ es una lista con pares de elementos que representan una arista de la siguiente forma: `(inicial, final)`.**

**R: Falsa.** Esta representación se conoce como “lista de aristas”. La lista de adyacencia es una lista con elementos escritos de la siguiente forma:
`nodo: [vecino1, vecino2, vecino3... vecinoN]`
Se da puntaje completo con tan sólo explicar una de las dos justificaciones dadas en este punto.

**5. Los tests unitarios sirven para probar funciones que reciben sólo un argumento.**

**R: Falsa.** Los tests unitarios son llamados dado que permiten probar unidades de código (_e.g._ una función), que son idealmente individuales e independientes.
Ideas como que reciben muchos argumentos, se considera como una justificación insuficiente, porque pueden haber funciones que no reciben argumentos.

**6. En el contexto de un `try/except`, las sentencias dentro del bloque `else` se ejecutarán sólo si es que no hubo una excepción.**

**R: Verdadero.**

## Desarrollo Rápido

**1.¿Cuál es la cantidad máxima de aristas que podría tener un grafo no dirigido sin _loops_ que tiene _n_ vértices? Justifique su respuesta**.

**Respuesta: n × (n - 1) / 2**.
Hay muchas justificaciones para este desarrollo. Utilizar la combinatoria sin repetición C(n,2), contar los 1 en una matriz de adyacencia de un grafo nxn, por inducción, etc.

Las personas que pusieron n x (n - 1) no consideraron quitar las repeticiones que se generan al ser un grafo no dirigido, por lo que no se considera como correcto.

**Rúbrica:**

- **0,2 ptos.** por la fórmula.
- **0,3 ptos.** por la justificación.

**2. Suponga que una función llamada `mifunc`, al ser llamada sin argumentos, levanta la excepción `RuntimeError`. Explique por qué el siguiente test falla. Asuma que `mifunc` está importada correctamente y que, además, el método `test_algo` está definido dentro de un caso de test creado con el módulo `unittest`.**

```python
def test_algo(self):
    self.assertRaises(RuntimeError, mifunc())
```

**Respuesta:** Este test falla porque al llamar a la función `mifunc` directamente en el caso de prueba, entonces esta se ejecuta y lanza la excepción. Esto no permite que el test haga realmente la comparación para saber si efectivamente ocurrió un `RuntimeError`.

Lo correcto hubiese sido sacarle los paréntesis a `mifunc()`, entregando sólo el _callable_.

Decir que `assertRaises` es quien tira el error no recibe puntaje, puesto que no es la verdadera razón.

## Sobre la actividad

**Rúbrica:**

- **0,75 ptos.** por cada una.

**1. ¿Bajo qué condición aparecía un `InconsistencyError`?**

**Respuesta:** Este error ocurría cuando se intentaba sumar dos carros de compra de supermercados distintos.

**2. ¿Qué método estaba incorrectamente implementado según los tests efectuados?**

**Respuesta:** El método que estaba implementado de manera incorrecta era el que permitía verificar la existencia de un producto o un código, en el catálogo de un supermercado, al utilizar el _keyword_ `in`.

## Pregunta de código

```python
class Nodo:

    def __init__(self, id_):
        self.id_ = id_
        self.vecinos = set()

    def __len__(self):
        return len(self.vecinos)


class Grafo:

    def __init__(self):
        self.aristas = {}

    @property
    def nodos(self):
        return {n.id_ : n for arista in self.aristas.values() for n in arista}

    def agregar_arista(self, x, y):
        if (x, y) in self:
            return

        nx = self.nodos.get(x, Nodo(x))
        ny = self.nodos.get(y, Nodo(y))
        nx.vecinos.add(ny)
        ny.vecinos.add(nx)
        self.aristas[(x, y)] = nx, ny

    def _tejas(self):
        return sum(map(len, self.nodos.values()))

    def lentejas(self):
        print(f"{len(self)} # {self._tejas()}")

    def __contains__(self, arista):
        return arista in self.aristas or arista[::-1] in self.aristas

    def __len__(self):
        return len(self.aristas)

    def __repr__(self):
        return f"{list(self.aristas)}"
```

**1. ¿El grafo de la clase `Grafo` es dirigido o no dirigido? Justifique su respuesta**.

**Respuesta:** El grafo es **no dirigido**. Al llamar al método `agregar_arista`, lo primero que este hacía era verificar si la tupla `(x, y)` o `(y, x)` estaba entre las aristas, vía el _dunder method_ `__contains__`. Por lo tanto, al no distinguir el orden de los elementos de la tupla, es posible inferir que no este no tenía importancia. Luego, el grafo era no dirigido.

Otra forma de verlo era que al agregar los vecinos, se añadían en ambos nodos, por lo que implicaba una bidireccionalidad.

**Rúbrica:**

- **0,1 ptos.** por decir que era un grafo no dirigido.
- **0,4 ptos.** por la justificación.

**2. Indique el `output` del código.**

**Rúbrica:**

Para _output_ de `g.lentejas()` :

- **0 ptos.** si hay dos errores.
- **0,1 ptos.** si hay un error.
- **0,3 ptos.** si no hay errores.

Para el _output_ de `print(g)`:

- **0 ptos.** si hay dos o más errores
- **0,3 ptos.** si hay un error (orden incorrecto de aristas cuenta como error)
- **0,6 ptos.** si no hay errores.


### Forma A
```python
g = Grafo()
g.agregar_arista(1, 2)
g.agregar_arista(1, 3)
g.agregar_arista(3, 1)
g.lentejas()
g.agregar_arista(2, 3)
g.agregar_arista(4, 3)
g.agregar_arista(3, 5)
g.lentejas()
g.agregar_arista(3, 5)
g.agregar_arista(4, 5)
g.agregar_arista(4, 6)
g.agregar_arista(4, 1)
g.lentejas()
print(g)
```

**Respuesta:**

```
2 # 4
5 # 10
8 # 16
[(1, 2), (1, 3), (2, 3), (4, 3), (3, 5), (4, 5), (4, 6), (4, 1)]
```

### Forma B
```python
g = Grafo()
g.agregar_arista(1, 2)
g.agregar_arista(2, 3)
g.agregar_arista(1, 3)
g.lentejas()
g.agregar_arista(3, 1)
g.agregar_arista(2, 4)
g.agregar_arista(5, 1)
g.agregar_arista(1, 4)
g.lentejas()
g.agregar_arista(1, 4)
g.agregar_arista(4, 5)
g.agregar_arista(3, 4)
g.lentejas()
print(g)
```

**Respuesta:**

```
3 # 6
6 # 12
8 # 16
[(1, 2), (2, 3), (1, 3), (2, 4), (5, 1), (1, 4), (4, 5), (3, 4)]
```

### Forma C
```python
g = Grafo()
g.agregar_arista(1, 2)
g.agregar_arista(2, 3)
g.agregar_arista(1, 3)
g.agregar_arista(1, 4)
g.lentejas()
g.agregar_arista(3, 4)
g.agregar_arista(2, 4)
g.agregar_arista(1, 5)
g.lentejas()
g.agregar_arista(1, 4)
g.agregar_arista(4, 2)
g.agregar_arista(5, 2)
g.lentejas()
print(g)
```

**Respuesta:**
```
4 # 8
7 # 14
8 # 16
[(1, 2), (2, 3), (1, 3), (1, 4), (3, 4), (2, 4), (1, 5), (5, 2)]
```
**3. Responda con palabras: ¿qué _diantres_ está calculando la función `_tejas`?**

**Respuesta:** Este método está calculando la suma de los **grados** de todos los vértices.
Si dicen que es el grado del grafo, dando a entender que eso sería la suma de los grados de los vértices, entonces corresponde el puntaje completo.

**Rúbrica:**
- **0 ptos.** por no decir nada o algo incorrecto.
- **0,3 ptos.** por decir que es la suma de los vecinos de todos los vértices.
- **0,5 ptos.** por utilizar la definición de grado.

**4. ¿Nota algo distintivo en cada resultado de `g.lentejas()`? ¿Cómo se podría explicar esto?**

**Respuesta:** El valor de la izquierda es la mitad que el de la derecha. Esto se puede explicar ya que cada vez que agrego una arista en un grafo no dirigido, esta incide exactamente en dos nodos, aumentando la suma total de los grados en 2.
En este punto se aceptan razonamientos que logren llevar a la conclusión esperada, mientras estos contengan la razón de que es un grafo no dirigido y que eso implica esta duplicación en el grado.


**Rúbrica:**
- **0,2 ptos** por decir que uno es el doble del otro.
- **0,3 ptos** por la explicación correspondiente.
