# Conceptos básicos de la POO

La programación orientada a objetos (POO) es un paradigma de
programación que utiliza objetos como parte esencial de sus
interacciones, para el desarrollo de aplicaciones y soluciones
tecnológicas. La POO está soportada por técnicas de programación tales
como la herencia, el polimorfismo, el encapsulamiento, entre otras, cada
una de ellas proporciona herramientas que han permitido la proliferación
de este modelo de programación en las últimas décadas. Actualmente
existen una variedad de lenguajes que soportan la POO, siendo los más
conocidos C++, Java y C#.

El soporte *moderno* de MATLAB para la POO es relativamente nuevo,
siendo introducido a partir de la versión 7.6 (R2008a) con notables
carencias respecto a los lenguajes de referencia en ese aspecto, pero
evidentemente la mejora desde entonces ha sido considerable.


> Con soporte *moderno* se hace alusión a la notación actual que se
utiliza en la definición de clases, por ejemplo `classdef` para crear
una clase. Puesto que antes de la implementación de esta notación,
existía la posibilidad de programar orientado a objetos haciendo uso
de algunos *artilugios*, como el colocar la clase (definida mediante
una función que hacía lo de un *constructor* de la clase) y sus
métodos dentro de una carpeta cuyo nombre debería ser el de la clase
misma anteponiéndole un arroba (@).

### Clases y objetos

Una clase es una definición de las propiedades y/o características de un
determinado tipo de objetos, es decir, un modelo particular que sirve
para crear objetos bajo esas mismas especificaciones.

Un objeto es la representación concreta derivada de una clase que está
provisto de atributos y métodos, o en términos más formales: un objeto
es la instancia de una clase.

A manera de ejemplo y un contexto más apegado a la realidad,
consideremos a los perros como una determinada clase, es sencillo
hacernos la idea de cómo es un perro y cuáles son sus características y
apariencia general; luego, el perro que tenemos en casa (en caso de que
así sea) es una instancia de esa clase o un objeto de la clase perro,
con características más particulares pero que no les excluyen de ser un
perro.

### Atributos

Los atributos son las propiedades asociadas a una clase de objetos.
Siguiendo con el ejemplo de los perros, estos tienen atributos como el
tamaño, color, raza, temperamento, etc. Es común en la POO diferenciar
entre dos tipos de atributos acorde a su accesibilidad: los privados y
los públicos. Los privados son atributos disponibles solo dentro de la
definición de la clase, en cambio los públicos son accesibles desde
cualquier otra clase o fichero de instrucciones.

### Métodos

Los métodos de una clase de objetos son algoritmos o bloques de
programación que determinan el comportamiento de un objeto. Por lo
general los métodos se usan para modificar los atributos de un objeto o
bien generar un nuevo evento. En MATLAB los métodos son definidos
mediante funciones.

### Eventos

Un evento es la *reacción* que tiene un objeto resultante de la
interacción con el usuario o bien mediante la ejecución de los métodos.
