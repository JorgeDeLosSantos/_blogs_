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

