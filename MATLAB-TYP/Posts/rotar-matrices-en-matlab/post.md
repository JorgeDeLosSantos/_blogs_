!# Resolver ecuaciones e inecuaciones 

La rotación de matrices consiste en redefinir la posición de sus
elementos mediante una modificación que no afecta el valor de sus
elementos. Para comenzar, suponga que se tiene un vector v definido como
sigue:

$$ v = [ v_1 , v_2 , v_3, \cdots , v_{n-1} ,v_n ] $$

Y sea vea v' el vector cuyas componentes son las mismas que v pero
dispuestas en un orden inverso, es decir:

$$ v\prime = [v_n , v_{n-1} ,\cdots , v_3 ,v_2 ,v_1 ] $$

En MATLAB invertir el orden de los elementos de un vector resulta una
tarea muy sencilla, esto puede lograrse indexando los elementos de la
forma que a continuación se muestra:

    >> v=[-2 5 8 7 3 0] % Vector original
    v =
        -2     5     8     7     3     0
    >> vp=v(end:-1:1) % Vector con elementos invertidos
    vp =
         0     3     7     8     5    -2

La anterior es una forma muy simple de realizar dicha tarea, pero si
usted prefiere el uso de funciones existe para tal fin la función fliplr
cuya tarea es exactamente esa, extendiéndose su uso también a matrices,
véase el ejemplo utilizando el mismo vector definido anteriormente:

    >> vp=fliplr(v)
    vp =
         0     3     7     8     5    -2

La función fliplr rota una matriz en un eje vertical, de tal modo que
las columnas situadas a la izquierda queden en la parte derecha. Véase
el ejemplo a continuación:

    >> A=randi(10,3)
    A =
         4     5     3
         2     2     4
         5     6     6
    >> Ar=fliplr(A)
    Ar =
         3     5     4
         4     2     2
         6     6     5

Está claro que fliplr ejecuta una rotación basada en las columnas, pero
MATLAB dispone también de la función flipud que ejerce una rotación en
un eje horizontal o basada en las filas, enseguida se muestra un
ejemplo:

    >> A=randi(10,4)
    A =
         5     6     8     2
         9     4     5     3
         8     2     1     5
        10     7     3     6
    >> Ar=flipud(A)
    Ar =
        10     7     3     6
         8     2     1     5
         9     4     5     3
         5     6     8     2

Además de las anteriores MATLAB proporciona la función rot90 que permite
girar la matriz en un ángulo múltiplo de 90° en el sentido contrario a
las manecillas del reloj, de manera informal es como si la matriz rodase
en dirección izquierda. Los argumentos de entrada de la función son
primeramente la matriz a rotar y como segundo argumento un escalar
entero que indica el múltiplo de 90° con el cual habrá de ejecutarse la
rotación, si no se introduce un segundo argumento se asume que este será
unitario. Véanse los ejemplos a continuación:

    >> A=randi(20,3)
    A =
        14     8    10
         1    19     9
        13     1    10
    >> A90=rot90(A)  % Matriz rotada 90°
    A90 =
        10     9    10
         8    19     1
        14     1    13
    >> A180=rot90(A,2)  % Matriz  rotada en 180°
    A180 =
        10     1    13
         9    19     1
        10     8    14
    >> A270=rot90(A,3)   % Matriz rotada 270°

    A270 =

        13     1    14
         1    19     8
        10     9    10