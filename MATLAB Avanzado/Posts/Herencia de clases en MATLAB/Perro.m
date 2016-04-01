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

