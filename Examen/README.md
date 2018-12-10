# Pauta Examen

## Pregunta 1: Contenido misceláneo

**1. (8 pts.)** Verdadero o Falso

**Rúbrica:**
- 1 pt por cada verdadera correcta
- 0.5 pts por cada falsa
- 0.5 pts por cada fundamentación de por qué es falsa.

a) Una clase derivada de una clase abstracta no puede ser instanciada, a menos que todos sus métodos abstractos estén implementados.

**Respuesta**: Verdadero.

b) Bajo el contexto de testing con unittest, el método setUp se ejecuta al principio de cada test.

**Respuesta:** Verdadero.

c) En OOP, el concepto de «interfaz» es el conjunto de atributos y métodos que expone un objeto.

**Respuesta:** Verdadero.

d) Para conectarse a un socket remoto, sólo es necesario definir la dirección IP de destino.

**Respuesta:** Falso, ya que también necesita el puerto.

e) Un servidor HTTP sólo puede responder con documentos en formato HTML o JSON.

**Respuesta:** Falso, ya que puede responder en cualquier formato: CSS, XML, imágenes, etcétera.

f) En Python, es posible definir atributos públicos y atributos privados para una clase.

**Respuesta:** Falso, ya que todos los atributos de un objeto en Python pueden ser accedidos desde afuera de una u otra forma. No existen los atributos privados; son sólo convenciones del lenguaje.

g) Los diccionarios son eficientes para revisar si un elemento está entre los valores.

**Respuesta:** Falso, ya que no son eficientes para los valores, pero sí para las llaves.

h) No es posible tener más de un daemon thread corriendo.

**Respuesta:** Falso, ya que… sí es posible.

**2. (2 pts.)** Dada la expresión `foo = logger('log.txt', 'verbose')(timer(foo))`, rellene el siguiente _snippet_ para que sea equivalente a dicha expresión. En otras palabras, utilice el azúcar sintáctico a su favor.

**Respuesta:**
```Python
@logger('log.txt', 'verbose')
@timer
def foo():
    pass
```

**Rúbrica**
- 2 pts, si tiene ambos decoradores en el orden correcto.
- 1 pt, si tiene ambos decoradores en el orden incorrecto o tiene errores de sintaxis pequeños.
- 0 pts, en cualquier otro caso.


**3. (2 pts.)** ¿Es posible implementar un `deque` usando una lista ligada con `nodos` de la clase A mostrada abajo? Si es así, justifique. Si no es así, explique por qué y proponga una modificación para que esto sea posible.

```Python
class A:
    def __init__(self, data, next_):
        self.data = data
        self.next_ = next_
```

**Respuesta:** No es posible, debido a que solo se puede extraer o sacar eficientemente elementos de un solo lado de la lista. Una solución es agregar una referencia o puntero adicional (un atributo `self.parent` por ejemplo), para disponer de operaciones eficientes en los dos lados de la lista.

**Rúbrica**
- 1 pt por decir que no se podía.
- 1 pt por entregar la solución de la lista doblemente ligada, de alguna manera: con código, palabras, etc.
    - 0.5 pts si la solución está mal implementada pero iba bien encaminada.

**4. (2 pts.)** Explique qué se debe hacer para capturar el teclado en una aplicación que tiene una interfaz gráfica. En su respuesta puede hacer referencia a `PyQt5`, pero no es obligatorio.

**Respuesta:** Implementar el método (por ejemplo, keyReleaseEvent) de interés en una clase que herede de Widget (QWidget).


**Rúbrica**
- 1 pt. Por señalar que se debe implementar un método que maneje el evento en cuestión.
- 1 pt. Por decir que este método se tiene que implementar en el objeto donde queremos capturar el evento. En el caso de PyQt es un Widget.


**5. (2 pts).** Describa un caso de uso en que preferiría utilizar UDP por sobre TCP. Justifique su decisión.

**Respuesta**: Puede ser un caso de streaming, por ejemplo, donde se necesita tener velocidad en la trasnmisión.

**Rúbrica**
- 1 pt. Si nombra un caso correcto.
- 1 pt. Por justificación correcta.
    - 0.5 pts. Si su justificación no es completa o convincente.

**6. (4 pts.)** Escriba el output para cada uno de los siguientes bloques de código. Asuma que existe un archivo para cada situación y que está en el formato sugerido por su extensión (.bin corresponde un archivo binario, mientras que .txt corresponde a un archivo de texto).

a)
```Python
with open('archivo_de_texto.txt', 'r') as f:
    print(type(f.read()))
```
**Respuesta**: `str`

b)
```Python
with open('archivo_de_texto.txt', 'rb') as f:
    print(type(f.read()))
```
**Respuesta**: `bytes`.

c)
```Python
with open('archivo_binario.bin', 'rb') as f:
    print(type(f.read()))
```

**Respuesta** `bytes`.

d)
```Python
mi_variable = pickle.dumps(json.dumps('iic2233'))
print(type(mi_variable))
```

**Respuesta** `bytes`.

**Rúbrica**:
- 1 pt cada una.
    - 0.5 pts en caso de que escriba "texto" donde era `str` o `binary` o _binario_ en caso de que fuera `bytes`

**7. (2 pts.)** Dada la siguiente figura, indique cómo llegar desde los siguientes orígenes a los destinos indicados mediante **rutas relativas**. (**Nota**: ../ se devuelve al directorio padre.)
(foto)

a) B -> K:

**Respuesta** `./E/J/K`  o   `E/J/K `

b) J -> C:

**Respuesta:** `../../../C`

**Rúbrica**
- 1 pt por cada respuesta correcta
- 0 En cualquier otro caso.

**8. (2 pts.)** Explique la principal diferencia entre `re.match` y `re.search`.

**Respuesta:** `re.match` solo hace _match_ cuando el patrón está al inicio del _string_, mientras que en `re.search` el patrón puede estar en cualquier parte.

**Rúbrica**
- 2 puntos si define lo que hace ambos y logra mostrar la diferencia.
- 1 punto si se equivoca en alguno de ellos, o los intercambia.
- 0 puntos en cualquier otro caso.


**9. (3 pts.)** ¿Qué significa _serializar_ y cuál es su propósito? Además, entregue un ejemplo clarificador.

**Respuesta:** Es transformar la información a un medio de almacenamiento (bytes, JSON, XML, etc). El fin de esto es poder enviarlo a través de una red.

**Rubrica**
- 1pt por la definición
- 1pt por el propósito
- 1pt por ejemplo clarificador


**10. (3 pts.)** Y ahora, sobre las herramientas del curso...

a) (1 pt.) ¿Qué permite hacer el comando `ls` de Unix?

**Respuesta:** Permite listar los archivos de un directorio/carpeta en específico.

**Rúbrica**
- Sólo se puede tener bueno o malo :c

b) (2 pts.) ¿Cuál es la diferencia entre `git add` y `git commit`?

**Respuesta:** git add mueve los cambios (o archivos) al área de staging, mientras que git commit empaqueta los cambios (o archivos) en el área de staging junto con un mensaje y crea un commit.

**Rúbrica**
- 2 pts Si dice la diferencia a partir de explicar lo que hace cada uno
- 1 pt Si sólo indica lo que hace uno o explicó bien uno de los dos comandos.
- 0 En cualquier otro caso

**11. (3 pts.)** **Bonus**: _último semestre nadie se enoja_

a) (1 pt.) _Cultura chupística_: escriba cinco módulos que vienen built-in en Python, tales como... `math`.

**Respuesta:** random, collections, functools, itertools, threading, socket, csv, json, os, sys...

**Rúbrica**
- Sólo se puede dar este bonus en caso de tener los 5 módulos buenos.

b) (1 pt.) ¿Qué versión de Python estamos utilizando en el curso? Escríbala en formato **X.Y**

**Respuesta:** 3.6 (Única respuesta válida)

c) (1 pt.) ¿Cuál es el nombre del diseñador del lenguaje de programación Python?

**Respuesta:** Guido (Única respuesta válida)



## Pregunta 2: Modelación OOP

1. **(15 pts)** Diseñe el diagrama de clases (en UML) que modela este problema. indique claramente las clases y relaciones entre éstas (_e.g._ composición, agregación, herencia). En caso de que no fuese claro qué relación existe entre dos clases, justifique su respuesta --con una línea es suficiente. La cardinalidad entre relaciones no será necesaria. Realice los supuestos que considere necesarios en tanto no contradigan el enunciado.

**Respuesta:**
![](https://i.imgur.com/b0bbkky.png)


**Rúbrica:**
+ **Clases**:
    + 1 punto cada una.
    + 2 puntos por incluir la clase Persona.
+ **Relaciones**:
     + 1 punto por cada una.
     + 2 puntos por colores correctos agregación y composición.
     + -1 punto por cada color incorrecto.
     + -0.5 por posicion del diamante incorrecta.


4. **(15 pts)** Escriba la declaración de clases, con atributos y métodos (incluyendo los _properties_) según el diagrama realizado en la parte anterior. Los atributos de cada clase deben estar declarados en el método `def __init__` de la clase. Recuerde ser consistente con el diagrama de clases diseñado en la parte anterior.

**Respuesta:**
**0.5 puntos por cada ítem.**
Era necesario tener 30 de los siguientes items para obtener los 15 puntos:

    Partida: 6 ítems (3p)
        uno
        dos
        jugadas
        resultado
        finalizar
        __len__
    Ronda: 2 ítems (1p)
        partidas
        estadísticas (property)
    Torneo: al menos 10 ítems de 12 posibles (5p)
        nombre
        fechas
        ciudad
        ritmo_de_juego
        premios
        inscritos
        terminado
        rondas
        posiciones
        organizar_ronda
        campeón (property)
        mejor_jugador (property)
    Persona: 4 ítems (2p)
        nombre
        apellido
        nacionalidad
        fecha_de_nacimiento
    Jugador: 4 ítems (2p)
        super()
        rating
        título
        torneos
    Árbitro: 4 ítems (2p)
        super()
        torneo_actual
        supervisar
        imponer_sanción



**Rúbrica:**

## Pregunta 3: Estructura de Datos y Algoritmos

... Enunciado ...

Usted deberá implementar varios métodos en una clase llamada `Grafo`. No debe crear una clase para los nodos del grafo, sino que debe usar estructuras básicas (_i. e._ listas, diccionarios, _strings_, _sets_, tuplas o números) dentro de `Grafo` para representar nodos y aristas.

1. **(4 pts)** Implemente el método `def __init__(self)` de forma de inicializar un grafo vacío. En este método usted debería establecer variables para guardar la información del grafo.

**Respuesta:**

Hay muchas formas. Se debe tener una forma de guardar los nodos y las conexiones. Una de ellas es utilizando un `defaultdict`, que por defecto tiene diccionarios vacíos:

```python
def __init__(self):
    self.nodos = set()
    self.adyacencia = defaultdict(dict)
```

**Rúbrica:**

- 2 ptos Hay una estructura para guardar los nodos que hay (Una estructura **adecuada**).
- 2 ptos Hay una estructura para guardar las aristas con sus pesos (Puede ser la misma anterior).
(puede ser la misma estructura para ambos)
**Importante:** Si se utilizó una clase `Nodo`, se descuenta 2 puntos.


2. **(6 pts)** Implemente el método `def agregar_nodo(self, pagina)` (donde `pagina` es de tipo `str`) para agregar un nuevo nodo al grafo. Si ya existe un nodo para esta página, no deberá hacer nada.

**Respuesta:**

```python
def agregar_nodo(self, pagina):
    self.nodos.add(pagina)
```

**Rúbrica:**

- 4 ptos Agrega nodo a su estructura
- 2 ptos Si es que nodo ya existe en el grafo, no pasa nada.

3. **(4 pts)** Implemente el método `def agregar_arista(self, pagina_a, pagina_b, peso)` que agrega una arista desde el nodo `pagina_a` hacia el de la `pagina_b` con el respectivo peso. Si alguno de los nodos no existe en el grafo, o si la arista ya existe, no deberá hacer nada.

**Respuesta:**

```python
def agregar_arista(self, pagina_a, pagina_b, peso):
    if pagina_a not in self.nodos or pagina_b not in self.nodos:
        return
    if pagina_b in self.adyacencia[pagina_a]:
        return
    self.adyacencia[pagina_a][pagina_b] = peso
```

**Rúbrica:**

- 2 ptos Se guarda una arista desde el nodo de la página hacia el de la página b con el respectivo peso. (1 si guarda bidireccionalmente).
- 1 pto   Revisa que los nodos existan y no hace nada si no existen.
- 1 pto   Revisa que la arista ya exista y no hace nada en ese caso.


Teniendo la estructura básica del grafo, el DCC quiere modelar cómo las personas navegan por las páginas. El supuesto es que cada persona que está en una página elige la siguiente haciendo clic en uno de los _links_ al azar. Tomando el ejemplo anterior, la probabilidad de llegar a Emol estando en Gamba con un clic es 1, puesto que todos los _links_ van hacia allá; en cambio, la probabilidad de ir hacia el perfil de Piñera estando en CNN es 3/8, ya que sólo 3 de los 8 _links_ en la página van hacia allá.

4. **(4 pts)** Implemente el método `def probabilidad_siguiente(self, pagina_a, pagina_b)` que devuelve la probabilidad de que un usuario pase desde la página _a_ hasta la página _b_ con un solo clic. Puede asumir que `pagina_a` y `pagina_b` siempre existen.

**Respuesta:**

```python
def probabilidad_siguiente(self, pagina_a, pagina_b):
        sum_out_nodo = sum(v for k, v in self.adyacencia[pagina_a].items())
        return self.adyacencia[pagina_a].get(pagina_b, 0) / sum_out_nodo
```

**Rúbrica:**

- 1 pto   Encuentra el peso de la arista entre a y b = w.
- 2 ptos Calcula la suma de los pesos de todas las aristas que salen de a = Z.
- 1 pto   Divide w en Z.


Por otra parte, la probabilidad de elegir un camino de _links_ [_v<sub>1</sub>_, _v<sub>2</sub>_, ..., _v<sub>n</sub>_] es el producto de las probabilidades de ir desde _v<sub>i</sub>_ hasta _v<sub>i + 1</sub>_ para 1 < _i_ < _n - 1_.

5. **(6 pts)** Implemente el método `def probabilidad_camino(self, camino)` que devuelve la probabilidad de que un usuario tome el camino indicado.

**Respuesta:**

```python
def probabilidad_camino(self, camino):
    if len(camino) <= 1:
        return 1
    return self.probabilidad_siguiente(camino[0], camino[1]) * self.probabilidad_camino(camino[1:])
```

**Rúbrica:**

- 4 ptos Recorre correctamente el camino.
- 2 ptos Multiplica correctamente las probabilidades de pasar a_i a a_{i+1} para todos los nodos del camino. (En caso de que inicialice en 0, se pone 0)


Por último, el DCC quiere simular cómo se podría comportar un usuario que parte en cierta página y obtener el camino que sigue si hace click en _k_ _links_.

6. **(6 pts)** Implemente el método `def camino_aleatorio(self, pagina, k)` que devuelve un camino de largo _k_, generado al azar simulando ser un usuario que parte del nodo `pagina`.

**Respuesta:** Se puede asumir que siempre van a haber conexiones mínimas.

```python
def camino_aleatorio(self, pagina_a, largo):
        # Iterativo
        path = [pagina_a]
        for _ in range(largo):
            nodo_actual = path[-1]
            vecinos = list(self.adyacencia[nodo_actual])
            pesos = [self.probabilidad_camino(nodo_actual, x) for x in vecinos]
            elegido = random.choices(vecinos, pesos, k=1)
            path.append(elegido)
        return path
```

**Rúbrica:**

- 2 ptos Devuelve un camino aleatorio de largo k (0 ó 1 para sólo el nodo entrada).
- 4 ptos El camino utiliza las probabilidades del paso anterior.

7. **(4 pts, bonus)** Implemente el método `def caminos_tamano_k(self, pagina, k)` que devuelve todos los caminos de largo _k_ que parten desde la respectiva página, junto con la probabilidad de que cada uno de estos sea tomado por el usuario.

**Respuesta:**

```python
def caminos_tamano_k(self, pagina_a, k):
    # Se subirá en breves instantes.
```

**Rúbrica:**

- Todo o nada.
- Realiza DFS o BFS para recorrer los distintos caminos. Además, Retorna los que son de tamaño k, sin repetidos en el formato correcto.

## Pregunta 4: Lectura de código

1. **(12 pts)** Escriba el _output_ del siguiente programa.

```python
# Los outputs vertidos por este programa no representan,
# necesariamente, el pensamiento del curso IIC2233.

class Estadio:
    def bengala(self, func):
        print("TBD")

class Monumental(Estadio):
    def bengala(self, func):
        try:
            print("Jugando en el Monumental de Núñez.")
            func()
        except:
            print("El Monumental de Núñez está inhabilitado.")
        else:
            print("¡River campeón!")
        finally:
            super().bengala(lambda: "La redonda emoción.")

class Bombonera(Estadio):
    def bengala(self, func):
        try:
            print("Jugando en la Bombonera.")
            func()
        except TypeError as error:
            print("La Bombonera está inhabilitada.")
        else:
            print("¡Boca campeón!")

class EstadioUCH(Monumental, Bombonera):
    def bengala(self, func):
        try:
            print("Jugando en el estadio de la Universidad de Chile.")
            func()
        except SyntaxError as error:
            print("No existe este estadio.")
        finally:
            super().bengala(func)

lista, estadio = [], EstadioUCH()
try:
    estadio.bengala(lambda: lista[0])
except IndexError:
    print("Jugando en el Santiago Bernabéu.")
```

**Respuesta:**

El _output_ es:
```
Jugando en el estadio de la Universidad de Chile.
Jugando en el Monumental de Núñez.
El Monumental de Núñez está inhabilitado.
Jugando en la Bombonera.
¡Boca campeón!
Jugando en el Santiago Bernabéu.
```

**Rúbrica:**

- 12 puntos por el output correcto perfecto.
- Descontar 1 punto por cada print que no esté, o esté y no debiese estar.
- Descontar 4 puntos si está correcto y hay 1 swap.
- Descontar 8 puntos si está correcto pero sin orden.




2. **(18 pts)** Lea **atentamente** el siguiente bloque de código.

```python
def foo(n):
    return sum(n % x == 0 for x in range(1, n + 1))

def bar(n):
    return lambda x: foo(x) == n
```

_a)_
**(3 pts)** Describa con sus propias palabras lo que hace la función `foo`. [**Pista**: En Python, recuerde que `True + False + True` devuelve 2. Y si no recuerda, apréndalo

**Respuesta:**

Dado un _n_ (un número natural), esta función `foo` te entrega la cantidad de divisores de _n_.

**Rúbrica:**

- 3 puntos por respuesta correcta.
- 2 puntos por escribir algo medianamente correcto (no divisores).
- 0 puntos en cualquier otro caso.

**(2 pts)** Además, escriba el resultado de `foo(12)`.

**Respuesta:**

El _output_ es 6, ya que 12 tiene seis divisores: 1, 2, 3, 4, 6 y 12.

**Rúbrica:**
- 2 puntos por escribir 6.
- 1 punto por **mostrar los divisores**, pero por alguna razón no llegar a 6.
- 0 puntos en cualquier otro caso.

_b)_
**(3 pts)** Describa con sus propias palabras lo que hace la función `bar`.

**Respuesta:**

Dado un _n_, te devuelve una función que dice si un número natural _x_ tiene (o no) _n_ divisores.

**Rúbrica:**

- 3 puntos por respuesta correcta.
- 2 puntos por escribir algo medianamente correcto.
- 0 puntos en cualquier otro caso.

**(2 pts)** Además, escriba el resultado de `bar(2)(23)`. ¿Para qué diantres podría servir `bar(2)`?

**Respuesta:**

El resultado es `True`, ya que 23 tiene exactamente dos divisores: 1 y 23.

**Rúbrica:**
- Asigna 1 punto por decir bar(2)(23) es True.
- Asigna 1 punto decir que bar(2) sirve para ver si un número es primo o no.

_c)_ **(3 pts)** Escriba el _output_ del siguiente código.

```python
uno = [n * n for n in filter(bar(2), range(5, 18))]
print(uno)
````

**Respuesta:**

El _output_ es:

```
[25, 49, 121, 169, 289]
```

**Rúbrica:**

- 3 si el _output_ es el correcto.
- 1 si el _output_ es incorrecto pero se tienen resultados parciales que muestren que entendió la lógica.
- 0 en otro caso.

_d)_ **(3 pts)** Escriba el _output_ del siguiente código.

```python
from functools import reduce

def qux(n):
    return reduce(
        lambda a, b: a + b,
        map(lambda x: x - foo(x), range(1, n + 1))
    )

dos = [qux(n + 3) for n in range(5)]
print(dos)
```

**Respuesta:**

El _output_ es:

```
[1, 2, 5, 7, 12]
```

**Rúbrica:**

- 3 si el _output_ es el correcto.
- 1 si el _output_ es incorrecto pero se tienen resultados parciales que muestren que entendió la lógica.
- 0 en otro caso.

_e)_ **(2 pts)** Escriba el _output_ del siguiente código.

```python
tres = set((p - 1) // q for p, q in zip(uno, dos))
print(tres)
```

**Respuesta:**

El _output_ es:

```
{24}
```

**Rúbrica:**

- 2 si el _output_ es el correcto.
- 1 si el _output_ es incorrecto pero se tienen resultados parciales que muestren que entendió la lógica.
- 0 en otro caso.

**Por definir**

_f)_ **(3 pts, bonus)** ¿Qué patrón (medianamente interesante) podría enunciar según los resultados obtenidos?

**Respuesta:**

Todo número primo mayor a 3 al cuadrado menos 1 es múltiplo de 24.

**Rubrica:**

Todo o nada.
