# Definiendo clases en MATLAB

Las clases son el *alma* de la POO, y suelen definirse en ficheros
únicos. En MATLAB pueden crearse utilizando un fichero *.m ordinario y
colocando en este la sintaxis para la definición de una clase, la cual
se muestra enseguida:

```matlab
classdef nombreClase
    % Descripción de la clase
    
    properties
        % Atributos
    end
    
    methods
        % Métodos
    end
    
end
```

En la mayoría de los lenguajes que soportan POO se utiliza la palabra
clave class para definir una clase, pero en MATLAB `class` se utiliza para
identificar el tipo o clase de una variable u objeto, y en cambio se
utiliza `classdef` para definir una clase. Los atributos de una clase se
definen en un bloque properties-end, y pueden simplemente ser declarados
sin asignación de valores. Los métodos de la clase se especifican dentro
de un bloque methods-end, incluyendo al constructor de la clase.

### El constructor de la clase

El constructor de una clase es parte esencial de la misma y en este se
definen los argumentos o parámetros formales necesarios para crear un
objeto de la clase, de ahí su importancia. En MATLAB el constructor se
considera, de manera no estricta, un método y por tanto se define dentro
del bloque correspondiente a los métodos. Así pues, incluyendo al
constructor la definición de una clase sería algo similar a:

```matlab
classdef nombreClase
    % Descripción de la clase
    
    properties
        % Atributos
    end
    
    methods
        function obj = nombreClase(args)
           % Constructor de la clase 
        end
        % ...
        % Métodos
        % ...
    end
    
end
```

En lo anterior obj es, dentro la definición de la clase, una referencia
al objeto instanciado y es obligatorio el colocarlo como *valor de
salida* (en la terminología de funciones); claro que el identificador
`obj` puede cambiarlo por cualesquiera otro de su comodidad (`this` o
`self` podrían ser buenas opciones, claro, mucho influye el hecho de
haber programado en otro lenguaje de POO en este tipo de *adopciones* de
estilo). Tal como se ejemplifica, el nombre de la función que funge como
constructor debe ser el mismo que el de la clase, además deben
especificarse los argumentos que se utilizarán para crear un objeto.

### La clase Persona, una primera aproximación

En la sección anterior hemos visto la sintaxis para definir una clase,
pero como casi todo siempre es mejor asociar un concepto teórico con un
ejemplo concreto. Para tal fin crearemos la clase Persona, de naturaleza
muy sencilla pero significativa.

En principio vamos a definir las propiedades o atributos que habrán de
caracterizar a un objeto de la clase Persona, así pues, dada la
simplicidad del caso solamente utilizaremos el nombre y la edad para
*construir* un objeto de esta clase. Por ahora no definiremos método
alguno, solamente el constructor de la clase. Véase la definición
resultante:

```matlab
classdef Persona
    % Persona
    %
    % Ejemplo :
    %           p1 = Persona('Jorge',22);
    %           p2 = Persona('Anna',28);          
    %
    
    properties % Atributos de la clase
        nombre;
        edad;
    end
    
    methods
        function obj = Persona(nombre,edad) % Constructor
            obj.edad=edad;
            obj.nombre=nombre;
        end
    end
    
end
```

Para *testear* una clase podemos crear un script en donde colocar las
instrucciones necesarias para crear un objeto de la misma. No obstante,
por ahora haremos esto en la ventana de comandos de la siguiente manera:

```matlab
>> p = Persona('Ana',25);
>> whos
  Name      Size            Bytes  Class      Attributes
  p         1x1               118  Persona        
```