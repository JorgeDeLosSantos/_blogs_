!# Resolver ecuaciones e inecuaciones

Una ecuación es una igualdad matemática entre dos expresiones
algebraicas en las que aparecen valores conocidos y una variable
desconocida (incógnita), relacionados mediante operaciones matemáticas
básicas, ejemplos de ecuaciones se muestran a continuación:

$$ 3x^2+2x-2=0 $$

$$ x+\frac{3}{7}=2 $$

$$ \cos(x)+sin(\frac{\pi}{2})=0 $$

Las ecuaciones algebraicas sirven para modelar situaciones poco
complejas pero que requieren el uso de la herramienta matemática para
obtener una solución satisfactoria. Existen diversos métodos para
resolver ecuaciones, los cuales se aplican dependiendo del tipo de
ecuación, incluso hay fórmulas establecidas para algunos tipos de
ecuaciones que minimizan el esfuerzo de cálculo.

MATLAB dispone de la función solve perteneciente al Symbolic Math
Toolbox, la cual permite resolver ecuaciones, inecuaciones y sistemas de
ecuaciones; la sintaxis general de la función `solve` es:

    solve(ec, var);

Donde ec es una ecuación algebraica definida usando variables simbólicas
y var es la incógnita respecto a la cual se resuelve la ecuación dada.

A manera de ejemplo se resolverá la siguiente ecuación lineal {$$} x+3=2 {/$$}:

    >> x=sym('x');
    >> solve(x+3==2,x)
    ans =
    -1

Es importante hacer mención que para especificar una igualdad se
utilizan dos signos, dado que un sólo signo hace referencia a una
asignación.

Si no se especifica el segundo miembro de la igualdad, MATLAB asumirá
que la expresión estará igualada a cero, es decir, para resolver la
ecuación:

$$ x^2-2x-1=0 $$

Puede hacerlo de las diversas formas que enseguida se muestran:

    >> solve(x^2-2*x-1==0,x)
    ans =
     2^(1/2) + 1
     1 - 2^(1/2)
    >> solve(x^2-2*x-1,x)
    ans =
     2^(1/2) + 1
     1 - 2^(1/2)
    >> solve(x^2-2*x-1)
    ans =
     2^(1/2) + 1
     1 - 2^(1/2)

Para resolver desigualdades o inecuaciones la sintaxis es prácticamente
la misma, claro, sólo hay que utilizar los operadores relacionales mayor
que o menor que en lugar del signo de igualdad. Por ejemplo, resolviendo
la siguiente desigualdad {$$} x+2>10 {/$$}:

    >> solve(x+2>10,x)
    ans =
    Dom::Interval(8, Inf)

MATLAB devuelve el intervalo solución para la inecuación, en este caso
{$$} (8,\infty) {/$$}. Para el caso de un intervalo cerrado MATLAB devuelve entre
corchetes el valor del límite correspondiente, por ejemplo:

    >> solve(x+2>=10,x)
    ans =
    Dom::Interval([8], Inf)

Un sistema de ecuaciones se compone de dos o más ecuaciones y un número
equivalente de valores desconocidos, es posible resolver sistemas de
ecuaciones utilizando también la función solve con la sintaxis
siguiente:

    solve(ec1,ec2,ec3,…)

Un ejemplo, resolver el siguiente sistema de ecuaciones:

$$ x+y=4 $$
$$ x-y=3 $$

    >> syms x y
    >> sol=solve(x+y==4,x-y==3)
    sol = 
        x: [1x1 sym]
        y: [1x1 sym]

Para visualizar los resultados puede acceder a los campos de cada
variable como se muestra enseguida:

    >> sol.x 
    ans =
    7/2
    >> sol.y
    ans =
    1/2

