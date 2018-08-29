# Pauta correción  Control 1 IIC2233-2018-2 

## 1. Verdadero y Falso (1,5 puntos)
1. En Python, las tuplas suelen almacenar datos heterogéneos.
	
	**Respuesta**: **Verdadero**.	 
2. La respuesta de `reduce(lambda x, y: (x + y) / 2, [1, 1, 3, 6])`  es 5.5.
	
	**Respuesta**: **Falso**, el resultado es 4.0 (puede ser escrito como **int** o **float**).
3. Un *deque* sirve para simular un *stack* y una cola, al mismo tiempo.
	
	**Respuesta**: **Verdadero**.

4. Los diccionarios son eficientes para revisar si un elemento está entre los valores.
	
	**Respuesta**: **Falso**, es eficiente sólo para verificar las llaves. 
6. Asumiendo que dicci es un diccionario, la expresión *'foo' in dicci* devolverá _True_ si 'foo' se encuentra entre las llaves de dicci, o bien, entre sus valores.
	
	**Respuesta**: **Falso**, la expresión devuelve _True_ si y sólo si está entre las llaves. Los valores no tienen ninguna incidencia.
## Distribución de puntaje
* 0.3 ptos por cada aseveración correcta.
* Si la aserveración es **falsa** el puntaje se distribuye de la siguiente manera:
	* 0.1 puntos si no está justificada.
	* 0.2 puntos  si está justificada pero no correcta completamente.
	*  0.3 puntos si está justificada correctamente.
## 2. Sobre la actividad AC02 (1,5 puntos)
1. Explique el propósito de la función *foreach* de la actividad.

	**Respuesta**: la función `foreach(función, iterable)` aplicaba una *función* a cada elemento del *iterable*.
3. Escriba una función llamada *print_each* que, dado un iterable, imprima sus elementos usando el foreach visto en la actividad.
	
	**Respuesta**: 
	
	**Opción 1**: utilizando directamente la función print en *foreach*
		
	
		def print_each(iterable): 
		    foreach(print, iterable)
		
	**Opción 2**: utilizando una función *lambda*  para realizar *print* sobre cada elemento del iterable.
	
		def print_each(iterable): 
		    foreach(lambda x: print(x), iterable)
		  
	**Respuesta alternativa**: aparte de las dos opciones entregadas, si se entregaba una función que realizara el *print* solicitado, la respuesta también está correcta. 

4. Suponga que *paises* es un iterable que contiene objetos con los atributos **sigla** y **nombre**. Escriba una función que reciba dos argumentos: un iterable de países y un nombre de un país. Esta función deberá retornar un generador que contenga únicamente la sigla de todos los países que calzan con ese nombre.

	**Respuesta**:
	
	**Opción 1**: una forma de hacerlo era por medio de un generador por comprensión:
	
		def siglas_de_pais(nombre_pais, paises): 
		    return (p.sigla for p in paises if p.nombre == nombre_pais)
		
	**Opción 2**: otra forma posible era utilizando un *map* y un *filter*:
	
		def siglas_de_pais(nombre_pais, paises): 
		    return map(lambda p1: p1.sigla, filter(lambda p2: p2.nombre == nombre_pais, paises))
	**Respuesta alternativa**: aparte de las dos opciones entregadas, si se entregaba una función que retornara el generador pedido, la respuesta también está correcta.
##  Distribución de puntaje
* 0.5 puntos por cada pregunta.
##  3. Desarrollo rápido (1 punto)

1. ¿Para qué sirve el *statement* `yield`en Python?

	**Respuesta**: para devolver un generador, a través de una función generadora.
		
2.  Suponga que cuenta con un generador con números enteros en su interior. ¿Qué ocurrirá con este generador si quisiéramos calcular el promedio de estos números?

	**Respuesta**: para calcular el promedio, es necesario conocer todos los números. Por lo mismo, tendremos que agotar el generador. 
	**Respuesta alternativa**:  también se podía responder con alguna función que permitiese calcular el promedio con uso del generador.
##  Distribución de puntaje
* 0.5 puntos por cada pregunta.

## 4. Lectura de código (2 puntos)

Escriba el *output* del programa. Escriba, además, el valor de los iteradores instanciados(asumiendo que se transforman, por ejemplo, en una lista, en donde sería posible ver los elementos de los iteradores, como si se le aplicara `print(list(generador))`) como **pasos intermedios**, anres de la impresión del resultado. Indique a qué paso intermedio coresponde cada secuencia de valores.
### Forma 1
	a = [3, 1, 4, 1, 5, 9, 2, 6] # pi
	b = [2, 7, 1, 8, 2, 8, 2] # e
	c = [1, 4, 1, 4, 2, 1] # raíz de 2
	resultado = {x[1] // x[2] for x in filter(lambda x: (x[0] + 1) % 3, zip(a, b, c))}
	print(resultado)
	
#### Respuesta
**Paso 1**: la función *zip* retornaba el siguiente generador:

	((3, 2, 1), (1, 7, 4), (4, 1, 1), (1, 8, 4), (5, 2, 2), (9, 8, 1))
 Debido a que *zip* forma tuplas hasta recorrer completamente el iterable con menos elementos, que en este caso sería la lista *c*.
 
 **Paso 2**: *filter* retornaba el siguiente generador:
		 
	((3, 2, 1), (1, 7, 4), (4, 1, 1), (1, 8, 4), (9, 8, 1))
Debido a que la condición del *filter* era que el sucesor del primer elemento de cada tupla **no** fuera múltiplo de 3. El único elemento del iterable que no cumplía con eso era `(5, 2, 2)` .

**Paso 3**: resultado final, el *set* por comprensión resultante debía era:

	{8, 2, 1}
Debido  a que *set* no admite duplicados, sólo debían quedar los valores distintos después de la operáción realizada sobre cada tupla.

### Forma 2
	a = [3, 1, 4, 1, 5, 9, 2, 6] # pi
	b = [2, 7, 1, 8, 2, 8, 2] # e
	c = [1, 4, 1, 4, 2, 1] # raíz de 2
	resultado = {x[1] // x[0] for x in filter(lambda x: (x[2] + 1) % 3, zip(a, b, c))}
	print(resultado)
	
#### Respuesta
**Paso 1**: la función *zip* retornaba el siguiente generador:

	((3, 2, 1), (1, 7, 4), (4, 1, 1), (1, 8, 4), (5, 2, 2), (9, 8, 1))
 Debido a que *zip* forma tuplas hasta recorrer completamente el iterable con menos elementos, que en este caso sería la lista *c*.
 
**Paso 2**: *filter* retornaba el siguiente generador:
		 
	((3, 2, 1), (1, 7, 4), (4, 1, 1), (1, 8, 4), (9, 8, 1))
Debido a que la condición del *filter* era que el sucesor del tercer elemento de cada tupla **no** fuera múltiplo de 3. El único elemento del iterable que no cumplía con eso era `(5, 2, 2)` .

**Paso 3**: resultado final, el *set* por comprensión resultante debía era:

	{0, 8, 7}
Debido  a que *set* no admite duplicados, sólo debían quedar los valores distintos después de la operáción realizada sobre cada tupla.

### Forma 3
	a = [3, 1, 4, 1, 5, 9, 2, 6] # pi
	b = [2, 7, 1, 8, 2, 8, 2] # e
	c = [1, 4, 1, 4, 2, 1] # raíz de 2
	resultado = {x[0] // x[1] for x in filter(lambda x: (x[2] + 1) % 3, zip(a, b, c))}
	print(resultado)
	
#### Respuesta
**Paso 1**: la función *zip* retornaba el siguiente generador:

	((3, 2, 1), (1, 7, 4), (4, 1, 1), (1, 8, 4), (5, 2, 2), (9, 8, 1))
 Debido a que *zip* forma tuplas hasta recorrer completamente el iterable con menos elementos, que en este caso sería la lista *c*.
 
 **Paso 2**: *filter* retornaba el siguiente generador:
		 
	((3, 2, 1), (1, 7, 4), (4, 1, 1), (1, 8, 4), (9, 8, 1))
Debido a que la condición del *filter* era que el sucesor del tercer elemento de cada tupla **no** fuera múltiplo de 3. El único elemento del iterable que no cumplía con eso era `(5, 2, 2)` .

**Paso 3**: resultado final, el *set* por comprensión resultante debía era:

    {0, 1, 4}
Debido  a que *set* no admite duplicados, sólo debían quedar los valores distintos después de la operáción realizada sobre cada tupla.


## Distribución de puntaje
 * 0.5 puntos por escribir correctamente el *zip* resultante
 * 0.5 puntos por escribir correctamente el *filter* resultante.
 * 1 punto por escribir el resultado final.

