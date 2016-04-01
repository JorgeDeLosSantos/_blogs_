# Métodos estáticos en una clase MATLAB

Los métodos estáticos son aquellos que pueden ser ejecutados sin necesidad de crear una instancia de 
la clase. En MATLAB pueden utilizarse para agrupar funciones dentro de una misma clase que haga las 
veces de una *librería* de funciones.

En la definición de una clase MATLAB se pueden crear diversos bloques de metodos (`methods`) o propiedades 
(`properties`), con diferentes configuraciones, por ejemplo, se puede definir un bloque de métodos ordinarios 
y otro bloque de métodos estáticos. Un bloque de métodos estáticos se indica colocando el modificador 
`(Static=true)` como sigue:

```matlab
classdef Clase

	properties
		% Propiedades de clase
	end

	methods
		% Métodos ordinarios
	end

	methods (Static=true)
		% Métodos estáticos
	end
end
```

Para ejemplificar cómo funcionan los métodos estáticos vamos a crear una clase `Math` que contendrá 
los métodos estáticos `minimo` y `maximo`, que calcularán el valor mínimo y máximo de dos valores pasados 
como argumento. A continuación se coloca el contenido del fichero de la clase Math que hemos creado:


```matlab
classdef Math
    
    properties (Constant=true)
        PI = pi; % Constante "pi"
        E = exp(1); % Constante "e"
    end
    
    methods (Static=true)
        function m = maximo(a,b)
            % Determina el máximo de dos valores
            if a>b
                m = a;
            else
                m = b;
            end
        end
        
        function m = minimo(a,b)
            % Determina el mínimo de dos valores
            if a<b
                m = a;
            else
                m = b;
            end
        end
    end
end
```

Podemos entonces *llamar* a los métodos `maximo` y `minimo` sin necesidad de crear una instancia:

```matlab
>> Math.minimo(10,20)
ans =
    10
>> Math.maximo(10,20)
ans =
    20
```
