# Descuentos :chart_with_downwards_trend: 

A pesar de que se pueden acumular más de 10 décimas entre todos los descuentos, el descuento final que aplica es el siguiente si no se entrega la tarea atrasada:

#### <center>mín(total descuentos aplicados, 10)</center>

Si la tarea se entrega atrasada, entonces la fórmula es

#### <center>mín(10 + descuentos atrasos, descuentos totales)</center>

## PEP8 (3 décimas) :pencil2: 
PEP8 es el estándar que se utiliza para programar en `Python` :snake:, por lo que es importante que se sigan las convenciones. Todo tipo de detalle sobre estas convenciones se encuentran [aquí](https://www.python.org/dev/peps/pep-0008/).

Solo se verificarán:
1. No se exceda el máximo de **80** carácteres **por línea**.
2. Que no haya variables no declarativas ni aclarativas.
3. Uso adecuado de CamelCase y snake_case.
4. Espacio después de la coma (",").
5. Uso de espacios para indentación y **no** de tabulaciones. 

La cantidad de décimas a descontar será la siguiente (acorde a lo establecido arriba):
- **1 décima** si no se cumple _solo_ 1
- **2 décimas** si no se cumplen 2
- **3 décimas** si no se cumplen 3 _o más_

La búsqueda de estos tipos de errores tampoco debe ser una búsqueda exhaustiva, pero es altamente probable que los _linters_ se los muestren. Si solo ven _un_ error de algún tipo siendo que en el resto de los casos no ocurre, entonces se puede perdonar.

## README (1 décima) :page_facing_up: 

Si no se indica(n) los archivos principales que son necesarios para ejecutar la tarea o su ubicación dentro de su carpeta se hará este descuento.


## Modularización (5 décimas) :package: 

* **5 décimas** si uno o más archivos exceden las 800 líneas de código.

* **3 décimas** si 3 o más archivos **exceden 600 líneas** y es posible haberlo segmentado en otros archivos


## Formato de entrega (5 décimas) :inbox_tray: 
 1. Lenguaje vulgar (groserías) o inapropiado para el curso
 2. Nombres de archivos no explícitos ni declarativos

## Entrega atrasada (5-20 décimas) :watch: 

Si se entrega la tarea atrasada se tendrá un descuento **inicial** de 5 décimas hasta un descuento de 20 décimas a las 24hrs de atraso del plazo establecido de manera lineal, con la fórmula:

### <center>5+15t/24</center>

Donde `t` está en horas (es una función **continua** y no discreta) y no se permiten entregas pasadas las 24 hrs de la hora inicial de entrega.


## Uso de `.gitignore` (5 décimas) :hand: 

Uno de los 3 siguientes casos:
- **5 décimas** si no está el `.gitignore` y sube las cosas de todos modos (y es pedido en el enunciado).
- **2 decimas** si no está el gitignore pero no están subidas las cosas (no se puede evaluar el uso de `.gitignore`)
- **2 décimas** si sube igual la `gui` a pesar de tener el arhivo `.gitignore` (no cumple con el objetivo del gitignore)

## Adicionales (5 décimas) :information_source:
Dependiendo de cómo esté hecha la tarea, el ayudante se puede topar con múltiples inconvenientes que impidan la corrección de la tarea o le dificulten en gran medida la revisión de esta. Es por esto que puede aplicar el descuento que considere apropiado para la situación en la que se encuentre de ser justificado.
