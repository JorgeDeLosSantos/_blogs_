# SymPy, calculando la ecuación de un plano dados tres puntos

SymPy es una de esas librerías que lo mismo sirven para hacer grandes cosas, que para *desempolvar* recuerdos y 
aplicarlos en cuestiones más orientadas a la etapa académica. Y es que las cuestiones de algebra simbólica 
suelen ser muy divertidas y lo suficientemente interesantes para mantener a un individuo ocupado.

Bueno, sin más preámbulos, en este post vamos a ver cómo utilizar SymPy para calcular la ecuación de un plano 
dados tres puntos contenidos en este.

Primero un poco de geometría elemental. Sean los tres puntos contenidos en el plano los siguientes:

$$ P_1 = (x_1, y_1, z_1) $$
$$ P_2 = (x_2, y_2, z_2) $$
$$ P_3 = (x_3, y_3, z_3) $$

Luego, la ecuación implícita del plano podemos obtenerla resolviendo la ecuación dada por el determinante siguiente:

$$
\left|\begin{matrix}
x - x_1 & y - y_1 & z - z_1 \\
x_2 - x_1 & y_2 - y_2 & z_2 - z_1 \\
x_3 - x_1 & y_3 - y_1 & z_3 - z_1 \\
\end{matrix}\right| = 0
$$

La solución tradicional creo que, llegados a este punto, todos podemos obtenerla sin ningún tipo de sobresalto. Ahora, 
la idea es implementar una solución utilizando SymPy. 

SymPy dispone de una clase `Matrix`, que recibe como argumentos de entrada una lista de valores numéricos o bien 
de cualquier variable simbólica que haya sido definida previamente. Está claro que en este caso los valores 
de las coordenadas de los puntos son conocidos, pero las variables \\(x, y, z\\) serán variables de tipo simbólico. 
Para calcular el determinante de una matriz podemos utilizar la función `det`, que recibe como argumento de entrada 
un objeto de la clase Matrix. Una vez resuelto el determinante tendremos una ecuación de la forma:

$$ Ax + By + Cz - k = 0 $$

Veamos el código implementado en SymPy:

```python
from sympy import Matrix, det
from sympy.abc import x,y,z

P1 = (1,2,3)
P2 = (0,-1,1)
P3 = (-2,1,-2)

M = Matrix([[x-P1[0]     , y-P1[1]     , z-P1[2]]    ,
		    [P2[0]-P1[0] , P2[1]-P1[1] , P2[2]-P1[2]],
		    [P3[0]-P1[0] , P3[1]-P1[1] , P3[2]-P1[2]]])

print(u"Ecuación implícita: %s = 0"%det(M))
```

Lo cual nos devolverá en consola la ecuación implícita del plano:

```python
Ecuación implícita: 13*x + y - 8*z + 9 = 0
```

Ahora bien, si requerimos la ecuación anterior expresada de forma explícita como una función bivariable del tipo 
\\(z=f(x,y)\\), entonces, debemos utilizar la función `solve` y resolver la ecuación planteada respecto a  \\(z\\), por ejemplo:

```python
from sympy import Matrix, solve, det
from sympy.abc import x,y,z

P1 = (1,2,3)
P2 = (0,-1,1)
P3 = (-2,1,-2)

M = Matrix([[x-P1[0]     , y-P1[1]     , z-P1[2]]    ,
		    [P2[0]-P1[0] , P2[1]-P1[1] , P2[2]-P1[2]],
		    [P3[0]-P1[0] , P3[1]-P1[1] , P3[2]-P1[2]]])

sol = solve(det(M), z)
print(u"Ecuación implícita: %s = 0"%det(M))
print(u"Ecuación explícita: z=%s"%(sol[0]))
```

Resultando:

```python
Ecuación implícita: 13*x + y - 8*z + 9 = 0
Ecuación explícita: z=13*x/8 + y/8 + 9/8
```

Incluso podemos graficar nuestro plano utilizando la función `plot3d` del módulo `plotting`:

```python
from sympy.plotting import plot3d

plot3d(sol[0], (x,0,5), (y,0,5), title="$z = %s$"%(latex(sol[0])))
```

