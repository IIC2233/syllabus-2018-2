# Guía de Corrección de Pares 

Esta guía está diseñada para ayudar a guiar en el proceso de corrección de una Actividad del curso IIC2233.

## Importante: Protege tu computador

El código que corregirás es ajeno, por lo que primero revisa si es seguro ejecutarlo. Utilizando un editor de texto (VSCode, Atom, Pycharm, etc), busca en el código las _keyword_ `eval`, `exec` y `pickle` (:skull:). Si las encuentras, evita ejecutar el código y reporta la situación al mail iic2233@ing.puc.cl.

**Ojo**, en los contenidos y la ayudantía se puede ver la utilización del método `exec_()` perteneciente a una instancia de `QApplication`. En este caso **no corresponde descuento**.

Si no están estas funciones en el código, entonces continúa :).

## Prueba el código

Para tener un primer _approach_ al código a corregir, córrelo para ver qué tal funciona. De esta manera, puedes tener una primera impresión de qué cosas alcanzó a realizar.

Si el código no corre (levanta alguna excepción), revisa el mensaje de error para ver la magnitud del error. 

## Se perdonan errores pequeños

A veces la gente se equivoca en cosas pequeñas, y si estas no están relacionadas con la materia de la semana, entonces se les perdona. Simplemente edita el código para que funcione :smile:.

Por ejemplo, es típico el `IdentationError` ya que el alumno dejó una función sin realizar y sin la sentencia `pass`. Un ejemplo:

```
# Hay mucho código..
def funcion_incompleta():
    
    
# Continúa el código..
```

Si los errores son del tipo `IdentationError`, `SyntaxError`, probablemente son fáciles de arreglar y debes hacerlo, para poder continuar con la corrección. 

Lo importante es que si la Actividad no corre por sí sola, ¡no merece necesariamente un 1.0 inmediato! La idea es buscar corregir lo más que se pueda para no perjudicar al alumno. Si tienen dudas, pueden hacer una _Issue_ :wink:. 

### Acerca de los Sprites

En la actividad se les dio la carpeta `sprites` con los diferentes archivos de imagen para hacer la actividad. Si sus compañeros no subieron las imágenes u ocuparon otra ruta, **no merecen descuento**, sólo cambia la ruta o deja las imágenes donde la persona que están evaluando las está buscando.

Un tip sería dejar las imágenes tanto en la raíz como en la carpeta `sprites` para no tener problemas. :wink: 

## Repasa la Actividad

Es importante acordarse qué se pedía y cómo iba a ser evaluado en la Actividad para comenzar a corregir. Para esto es necesario releer la Actividad y el feedback entregado para saber qué buscar y cómo.

Probablemente se deba revisar más de una vez, así que tenlo abierto (o disponible) durante la corrección.

## Corregir

En este momento comienza la corrección de la Actividad, para lo cual se debe ir avanzando en los ítems a probar. La idea es desagregar la actividad en distintas metas pequeñas, para que se evalúe de forma independiente cada una. 

Por ejemplo, si se pedía realizar una clase con varios métodos, la idea es ver, de manera independiente, cada uno de ellos.

Para esto se busca evitar descontar dos veces por lo mismo. Por ejemplo, si un alumno se equivocó en  implementar una función para mostrar una imagen en un label y utiliza esta función en dos requerimientos distintos, entonces sólo se le baja en uno. Si, por otro lado, lo implementa dos veces y de forma errónea, se le baja en ambos.

## Basarse en el feedback

Lean bien el feedback para saber cuántos puntos asignar en cada caso. Cada décima de nota equivale a un punto en el feedback, ¡así que ten ojo en esa conversión! Si tienen dudas sobre cuántos puntos asignar a una funcionalidad incompleta (y que no salga detallado), hagan una Issue :smile:.


## Descuento de formato


El archivo entregado debe ser un módulo de Python, por lo que si no posee la extensión **.py**, se descuenta 2 décimas.

En la Actividad no se imponían nombres específicos a las clases/funciones. Por lo tanto, no hay más descuentos específicos en esta sección.

Sin embargo, si el alumno en algún momento imprime algún mensaje obsceno o que insulta a algún ayudante/alumno/profesor, por ejemplo, porfavor reportar esto al mail iic2233@ing.puc.cl. Ahí el cuerpo docente discutirá cuánto descuento se merece.

## Ser un buen evaluador

La idea no sólo es evaluar a sus compañeros, sino que ayudarlo a mejorar por lo que lo mejor que puedes hacer es darle buen feedback. Si encuentras que pudo resolver el problema de una mejor manera, entonces déjalo como comentario para que el alumno no se equivoque en lo mismo en otra evaluación :smile:.

## Hagan issues!

Aunque tratemos, quizás no podamos ser todo lo específico que deberíamos en el feedback. Si consideran que este es poco claro en cualquier punto, hagan una issue pidiendo alguna aclaración. Así ayudan a otros a corregir si tuvieron las mismas dudas que ustedes :wink:.

## Tips generales

Por último, dejamos algunos tips generales para corregir mejor:

- Evita estar apurado.
- Tratar de entender qué intentó hacer el alumno.
- Trata de siempre ser explícito en decir en qué se equivocó tu compañero.
- En los comentarios, decir dónde está el error es muy útil! (No está de más señalar la línea del error) :+1:
- En esa misma línea, dar un consejo si es que se te ocurre es dar el mejor feedback a tu compañero :smile: 
- En cada paso del feedback que vayas completando, anota inmediatamente tus observaciones! :cop: Es fácil olvidarlas.

## Ética

Recuerden que esta es una evaluación de un curso de la universidad. Por lo que les pedimos que respeten las normas y no favorezcan a nadie por motivos personales. Sean siempre objetivos y, si tienen dudas, no duden en preguntar :wink:.