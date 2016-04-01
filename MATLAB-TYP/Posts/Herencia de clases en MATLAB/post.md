# Herencia de clases en MATLAB

En el ambiente de la programación orientada a objetos herencia refiere a la posibilidad de crear 
clase nuevas utilizando como base una existente, de modo que la nueva clase *hereda* los métodos 
y atributos de la clase *padre*.

En MATLAB la sintaxis para heredar de una clase es post-poniendo a la definición de clase 
un signo *menor que* y la clase de la cual se hereda (superclase).

```matlab
classdef clase < SuperClase
	% Cuerpo de la clase
	% ...
end
```

Para ejemplificar de mejor manera la forma de heredar de una clase MATLAB vamos a crear una superclase 
llamada `Animal` y una subclase `Perro`. A continuación se adjuntan ambas:

```matlab
classdef Animal < handle
    % Clase animal heredada de la superclase handle.
    properties
        tipo; % Propiedades de clase
        edad;
    end
    
    methods
        function desplazar(obj,distancia)
            % El método desplazar imprime cierta distancia 
            % que se ha desplazado nuestro Animal.
            fprintf('%s se ha desplazado %g metros\n',obj.tipo,distancia);
        end
        function crecer(obj)
            % Aumenta en la unidad la propiedad de clase "edad"
            obj.edad = obj.edad + 1;
        end
    end
end
```

```matlab
classdef Perro < Animal
    % Clase Perro, heredada de Animal
    properties
        raza; % Nueva propiedad de clase
    end
    
    methods
        function obj = Perro(raza,edad)
            obj.raza = raza;
            % Inicializamos las propiedades heredadas de la 
            % superclase Animal con valores pre-definidos.
            obj.edad = edad;
            obj.tipo = 'Perro';
        end
        function ladrar(obj)
            % El método ladrar sólo lo tienen disponible 
            % los perros.
            fprintf('El perro de raza %s ha ladrado\n',obj.raza);
        end
    end
    
end
```

La clase `Animal` también hereda de una superclase `handle`, la cual es una clase abstracta de MATLAB que permite 
el manejo adecuado de los atributos de clases.


