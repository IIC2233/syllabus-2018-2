# Pauta C05
## Verdadero o falso (1,8 puntos)
### Rúbrica:
+ 0.15 por cada V o F correcto
+ 0.15 por buena justificación en caso de que la respuesta correcta sea “F”.
------------
1. Si se cambia la extensión de un archivo, entonces su contenido cambia.
   **R: Falso**.
   ***Justificación***: La extensión de un archivo es parte de su nombre y constituye simplemente una convención para informar acerca de su contenido, pero no para determinarlo.
2. Todo archivo de texto puede ser leído como un archivo binario.
   **R: Verdadero**.
3. Todos los caracteres usados en el idioma español se pueden codificar usando 
   `utf-8`, pero no `ascii`.
   **R: Verdadero**.
4. La función `bin` recibe un `bytearray` y devuelve un string.
   **R: Falso**.
   ***Justificación***: recibe cualquier tipo de objeto que pueda ser interpretado como `int` o bien implemente el método `__index__`
5. Un objeto del tipo `bytes` puede tener un largo mayor a 256 elementos.
   **R: Verdadero**
7. Al crear una subclase de `threading.Thread`, se debe implementar lo que se ejecutará en el método `start`.
   **R: Falso** 
   ***Justificación***: Se debe implementar el método `run`.
9. Un _thread_ _daemon_ se deja de ejecutar cuando el _thread_ principal termina.
   **R: Verdadero**
9. Un _deadlock_ se produce solamente cuando se usan _locks_.
   **R: Falso**
   ***Justificación***: Puede producirse usando cualquier primitiva de sincronización, incluyendo _Events_.

  
## Desarrollo rápido (1,2 puntos)
1. En el contexto del uso de interfaces gráficas, explique en qué consiste el modelo *backend-frontend* y mencione dos ventajas.

### Rúbrica:
+ **0.6 por explicar en qué consiste**
    + 0.6 por explicar en qué consiste mencionando separación.
    + 0.3 si se aproxima pero **no menciona separación**.
----
Respuestas tipo:
+ “Es la separación entre la lógica y lo visual del programa”
+ “Separación que existe entre la capa de presentación y la capa de acceso a los datos.”
+ “Un modelo para separar la lógica del programa y lo que se muestra del programa”
----
+ **0.3 por cada ventaja mencionada (hasta 2 ventajas).** [En el material se mencionan 6](https://github.com/IIC2233/contenidos/blob/master/semana-10/5-dise%C3%B1o-front-back.ipynb), pero pueden haber otras a criterio del corrector.
-------


## Sobre la actividad (1,5 puntos)
Dada la palabra 01011000110, indique cuáles son los bits de paridad siguiendo el algoritmo de detección de errores basado en el código de *Hamming*.

### Rúbrica:
Aquí existen varios tipos de respuesta:

----
**Si simplemente indica 4 posiciones de la palabra:**
- 0 bits correctos → 0p
- 1 bit correcto → 0,3p
- 2 bits correctos → 0,6p
- 3 bits correctos → 1,0p
- 4 bits correctos → 1,5p

Además, se resta un bit correcto por cada bit extra usado.

----
**Si el alumno dio la definición (2^k - 1), 1,5 si esta definición es correcta, 0,75 si tiene algún fallo menor, y 0 en otro caso.**

----

**Si el alumno dio los bits juntos (por ejemplo, en este caso la secuencia correcta sería “0110”) dar 1,5 si dio exactamente esta secuencia**

----
**R**: **01**0**1**100**0**110
## Lectura de código(1,5 + 0,5(bonus) puntos)
## Resumen Formas

+ [Forma A: “El papá de los helados”](#codA)
+ [Forma B: “La tía de los helados”](#codB)
+ [Forma C: “La mamá de los helados”](#codA)


### <a name="codA"></a> Forma A
```python=
from os.path import basename


def leer(nombre_archivo):
    try:
        with open(nombre_archivo, 'rb') as binario:
            print(f'Leyendo {basename(nombre_archivo)}')
            return binario.read()
    except FileNotFoundError:
        print('No se encontró el archivo')
        return b'\x4f\x74\x72\x6f\x73\xe5\x8d\x8e\xe4\xb8\xba'


leer('../A/B/E/J')
leer('/A/C/G')
leer('./F/K')

contenido = leer('K')
decodificado = contenido.decode('ascii', errors='ignore')

print(type(contenido))
print(type(decodificado))  
print(decodificado) # 0,5 pts de bonus
```
#### Output
```bash=
'No se encontró el archivo'     => 0.2 (correcto/incorrecto)
'Leyendo G'     => 0.3 si está correcta. 0.2 si en vez de ‘G’ da el path completo.
'No se encontró el archivo'    => 0.2  (correcto/incorrecto)
'Leyendo K'     => 0.3 si está correcta. 0.2 si en vez de ‘K’ da el path completo.
<class ‘bytes’>    => 0.25 si da a entender que es de tipo bytes.
<class ‘str’>    => 0.25 si da a entender que es de tipo string.
El pap de los helados    => 0.5 bonus: correcto / incorrecto
```

### <a name="codB"></a> Forma B 
```python=
from os.path import basename


def leer(nombre_archivo):
    try:
        with open(nombre_archivo, 'rb') as binario:
            print(f'Leyendo {basename(nombre_archivo)}')
            return binario.read()
    except FileNotFoundError:
        print('No se encontró el archivo')
        return b'\x50\x75\x6e\x74\x6f\xe5\x8d\x8e\xe4\xb8\xba'


leer('/A/B/F/K')
leer('../A/C/G')
leer('./D/I')

contenido = leer('I')
decodificado = contenido.decode('ascii', errors='ignore')

print(type(contenido))
print(type(decodificado))  
print(decodificado) # 0,5 pts de bonus
```
#### Output
```bash=
'Leyendo K'    => 0.3 si está correcta. 0.2 si en vez de ‘K’ da el path completo.
'No se encontró el archivo'    => 0.2 (correcto/incorrecto)
'No se encontró el archivo'    => 0.2 (correcto/incorrecto)
'Leyendo I'    => 0.3 si está correcta. 0.2 si en vez de ‘I’ da el path completo.
<class ‘bytes’>    => 0.25 si da a entender que es de tipo bytes.
<class ‘str’>    => 0.25 si da a entender que es de tipo string.
La ta de los helados    => 0.5 bonus: correcto / incorrecto

```
### <a name="codC"></a> Forma C
```python=
from os.path import basename


def leer(nombre_archivo):
    try:
        with open(nombre_archivo, 'rb') as binario:
            print(f'Leyendo {basename(nombre_archivo)}')
            return binario.read()
    except FileNotFoundError:
        print('No se encontró el archivo')
        return b'\x4f\x74\x72\x6f\x73\xe5\x8d\x8e\xe4\xb8\xba'


leer('../A/B/E/J')
leer('/A/C/G')
leer('./F/K')

contenido = leer('K')
decodificado = contenido.decode('ascii', errors='ignore')

print(type(contenido))
print(type(decodificado))  
print(decodificado) # 0,5 pts de bonus
```
#### Output
```bash=
'No se encontró el archivo'     => 0.2 (correcto/incorrecto)
'Leyendo G'     => 0.3 si está correcta. 0.2 si en vez de ‘G’ da el path completo.
'No se encontró el archivo'    => 0.2  (correcto/incorrecto)
'Leyendo K'     => 0.3 si está correcta. 0.2 si en vez de ‘K’ da el path completo.
<class ‘bytes’>    => 0.25 si da a entender que es de tipo bytes.
<class ‘str’>    => 0.25 si da a entender que es de tipo string.
La mam de los helados    => 0.5 bonus: correcto / incorrecto

```