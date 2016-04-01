classdef Math
    
    properties (Constant=true)
        PI = pi; % Constante "pi"
        E = exp(1); % Constante "e"
    end
    
    methods (Static=true)
        function m = maximo(a,b)
            % Determina el m�ximo de dos valores
            if a>b
                m = a;
            else
                m = b;
            end
        end
        
        function m = minimo(a,b)
            % Determina el m�nimo de dos valores
            if a<b
                m = a;
            else
                m = b;
            end
        end
    end
end