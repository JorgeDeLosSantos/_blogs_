# Una introducción a SymPy

SymPy es una librería de Python desarrollada para resolver problemas de matemáticas simbólicas. Existen diversos software comerciales que realizan estas tareas: Maple, Mathematica, MATLAB, entre otros, pero requieren una licencia de uso que puede resultar poco accesible en algunos casos. En cambio, SymPy se distribuye bajo licencia BSD, que en resumen permite el uso libre de la misma.   

### Importando SymPy

Para importar SymPy y disponer de todos los módulos y funciones que le componen puede hacerse de diversas formas:

1. Forma tradicional

```python
>>> import sympy
```

Es la manera más habitual, se carga toda la librería y se accede a cada una de las funciones mediante la sintaxis:

```python
>>> r=sympy.funcion(args)
```

2. Importando funciones seleccionadas

```python
>>> from sympy import Symbol,integrate,sin,cos
```

De este modo se importan solamente las funciones que vayan a utilizarse, es recomendable cuando se utilizará un número reducido de las mismas. Proporciona cierta ventaja dado que para acceder a una función no es necesario anteponer el nombre de la librería (sympy), aunque esto mismo represente una desventaja en aquellos casos en los que existen funciones de diferentes librerías con el mismo nombre.

3. Utilizando un alias o seudónimo

```python
>>> import sympy as sp
```

Funciona del mismo modo que para el primer caso, con la diferencia que el usuario puede asignarle un nombre más corto o bien más representativo para hacer las llamadas a funciones.

Para los ejemplos que se mostrarán en esta entrada se utilizará la segunda forma.


### Declarando una variable simbólica

Para declarar una variable simbólica podemos utilizar la función Symbol, para ello primero importamos la función y posteriormente declaramos una variable simbólica "x":

```python
>>> from sympy import Symbol
>>> x=Symbol('x')
>>> x
x
>>> x+2
x + 2
```

Como puede verse, una vez se ha declarado la variable simbólica podemos utilizarle para formar expresiones algebraicas de todo tipo. Existe una forma más "simple" de declarar una variable simbólica, para ello habrá de importarse del módulo "abc" la letra correspondiente, por ejemplo:

```python
>>> from sympy.abc import x
```

O bien:

```python
>>> from sympy.abc import x,y,z
```

Lo anterior en el caso de que se requieran múltiples variables simbólicas.


### Manipulaciones algebraicas

#### Factorizar una expresión algebraica.

Para factorizar una expresión algebraica podemos utilizar la función factor, por ejemplo suponga que se quiere factorizar 
la expresión \(x^2+2x+1\):

```python
>>> from sympy import factor,Symbol
>>> x=Symbol('x')
>>> factor(x**2+2*x+1)
(x + 1)**2
```

#### Expandir una expresión algebraica

Enseguida se muestra un ejemplo de cómo "expandir" o multiplicar dos expresiones algebraicas.

```python
>>> from sympy import Symbol,expand
>>> x=Symbol('x')
>>> expand((x+2)*(x-3))
x**2 - x - 6
```