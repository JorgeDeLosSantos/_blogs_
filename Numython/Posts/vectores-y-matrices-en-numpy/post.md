# Vectores y matrices en NumPy

NumPy es una librería muy útil y un *estándar* en Python para el manejo de matrices y/o arreglos que 
contienen datos de tipo numérico. La mayoría del ecosistema científico de Python está basado en 
los arreglos de NumPy para el manejo de datos.

Normalmente se acostumbra importar el módulo NumPy utilizando el alias **np**:

```python
>>> import numpy as np
```

Se puede crear un arreglo de NumPy a partir de una lista ordinaria de Python, utilizando la 
función `np.array`.

```python
>>> lista=[-1,0,2,5,8]
>>> A=np.array(lista)
>>> A
array([-1,  0,  2,  5,  8])
```

La función `np.array` crea un objeto de la clase `numpy.ndarray`,

```python
>>> type(A)
<type 'numpy.ndarray'>
```

Si se requiere crear una matriz debe pasarse como argumento de entrada una lista de listas, donde 
cada sublista representa una fila de la matriz, por ejemplo para definir la matriz $M$ siguiente:

$$
M = \left(\begin{matrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9 \\
\end{matrix}\right)
$$

utilizando una lista de listas,

```python
>>> M=np.array([[1,2,3],[4,5,6],[7,8,9]])
>>> M
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
```

Se puede determinar la forma (número de filas y columnas) de una matriz o arreglo utilizando la 
propiedad `shape` de la clase `numpy.ndarray`.

```python
>>> A.shape
(5L,)
>>> M.shape
(3L, 3L)
```

En entradas posteriores veremos cómo realizar operaciones matriciales con matrices vectores.
