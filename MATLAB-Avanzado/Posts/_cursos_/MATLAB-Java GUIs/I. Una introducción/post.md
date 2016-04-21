# MATLAB-Java GUIs I. Una introducción

Bienvenidos, esta será una mini-serie de entradas dedicadas a introducir a los usuarios de MATLAB 
en el desarrollo de interfaces gráficas utilizando una combinación de controles ordinarios 
de MATLAB con controles de la librería Swing de Java. Es necesario que el lector tenga conocimientos 
sólidos en el desarrollo de interfaces gráficas en MATLAB utilizando solamente código (no GUIDE), 
de programación orientada a objetos en MATLAB, y bueno, sería sensacional si conoce algo de Java.

### Para comenzar

Las interfaces gráficas en MATLAB suelen considerarse hasta cierto punto muy limitadas 
en cuanto a apariencia, funcionalidad y sobre todo a la poca diversidad de controles 
gráficos disponibles en la librería estándar. Se extraña, por poner un ejemplo, que los 
*Static Text* tengan la posibilidad de añadir una imagen, o que a un botón le podamos 
agregar un ícono junto al texto, o bueno, varias de esas cosas que son posibles y relativamente 
sencillas de implementar en muchos otros toolkits de interfaces gráficas.

No obstante, MATLAB tiene la posibilidad (y facilidad) de integrar controles gráficos de 
la librería Swing de Java de manera muy simple en una interfaz gráfica ordinaria. 
Esto puede lograrse utilizando la función `javacomponent`, con la cual podemos *incrustar* 
controles gráficos de Java en una *figure* de MATLAB.

Para ir entrando un poco en el tema vamos a mostrar un código muy simple que 
coloca un JLabel (similar al *Static Text*) dentro de una GUI:

```matlab
import javax.swing.*

fig = figure('Name','Ejemplo MATLAB-Java',...
    'NumberTitle','off',...
    'MenuBar','none',...
    'Position',[0,0,200,100]);
centerfig(fig);

lab = JLabel('JLabel Java');
hJlab = javacomponent(lab, 'East', fig);
```


Ahora vamos a *desmenuzar* el código anterior:

Primero, importamos todas las clases de la librería Swing, también hubiese sido muy 
recomendable sólo importar la clase Java que vamos a utilizar: `import javax.swing.JLabel`. 
Pero, normalmente (*en la vida rea*l) no sólo se utiliza una de las clases de Swing, así 
que podríamos dejarlo tal cual y ya está. Al importar con `import javax.swing.*` tenemos 
disponibles todas las clases de Swing en el *workspace* de MATLAB, así, sólo necesitamos 
escribir `JLabel` para instanciar una etiqueta en lugar del `javax.swing.JLabel` que 
deberíamos colocar si no colocamos la instrucción de importar.

Lo que sigue es crear una ventana con la función `figure`, en la cual colocaremos 
nuestros controles Java. Y claro, la función `centerfig` para centrar la ventana en la pantalla.

Aquí viene la parte en donde instanciamos un objeto de la clase `JLabel`. Normalmente, en Java, 
tendríamos que escribir algo como:

```java
JLabel lab = new JLabel("JLabel Java");
``` 

Pero en MATLAB la sintaxis es más sencilla. 

Una vez tenemos creado un objeto de la clase `JLabel`, tenemos que colocarlo dentro de la ventana 
que hemos definido con anterioridad, y para eso usaremos la función `javacomponent`. Lo primero: 
la función `javacomponent` tiene la siguiente sintaxis:

```matlab
[hJ, hM] = javacomponent(javaClassName, position, parent, callback);
```

Donde `javaClassName` puede ser un objeto o una clase de Java (en este caso la etiqueta que hemos 
instanciado), `position` puede ser un vector de cuatro elementos típico de MATLAB o bien una cadena 
de texto: *South*, *West*, *North* o *East*, indicando la ubicación del elemento dentro de 
la ventana, `parent` será la ventana o panel en el cual colocaremos el objeto gráfico, y finalmente 
`callback` es un cell array de elementos *pareados* del tipo evento-handler y cuyo objetivo es 
especificar el comportamiento de un control gráfico ante un evento determinado, por ahora esto lo hemos 
dejado vacío, ya que no entraremos aún en el manejo de eventos.

La función `javacomponent` devuelve normalmente dos valores de salida: `hJ` será la referencia a 
la clase Java del control gráfico y a través de este podremos modificar sus características; `hM` 
es un handle cuasi ordinario de MATLAB y este nos servirá para modificar las propiedades de posición, 
unidades y visibilidad del objeto gráfico una vez que este haya sido agregado a la GUI MATLAB.

### Modificando las propiedades de un control Java Swing

Para modificar las propiedades de un componente creado con `javacomponent` podemos hacerlo a través de su 
referencia, por ejemplo, para el JLabel que utilizamos al principio:

```matlab
clear;clc;
import javax.swing.*

fig = figure('Name','Ejemplo MATLAB-Java',...
    'NumberTitle','off',...
    'MenuBar','none',...
    'Position',[0,0,200,100]);
centerfig(fig);

lab = JLabel('JLabel Java');
[hJLab,hMLab] = javacomponent(lab, 'North', fig);
hJLab.setOpaque(true);
hJLab.setForeground(java.awt.Color.RED);
hJLab.setBackground(java.awt.Color.YELLOW)
hJLab.setHorizontalAlignment(JLabel.CENTER);
```

Como puede notar, las propiedades se modifican a través de métodos. Todos estos métodos disponibles para 
los controles de Java Swing puede consultarlos en la [documentación oficial de Java](https://docs.oracle.com/javase/7/docs/api/javax/swing/package-summary.html).

### Para aprender más...

La referencia obligatoria y necesaria será siempre el blog [**Undocumented MATLAB**](http://undocumentedmatlab.com/) 
del gran Yair Altman, que es sin duda el lugar donde más información online encontraremos sobre la integración MATLAB-Java 
y muchas otras utilidades no documentadas de MATLAB.

También existe el libro **Undocumented Secrets of MATLAB-Java Programming** del mismo Yair Altman, muy recomendable.

<a href="https://www.crcpress.com/Undocumented-Secrets-of-MATLAB-Java-Programming/Altman/9781439869031">
	<img src="https://images.tandf.co.uk/common/jackets/amazon/978143986/9781439869031.jpg" width="15%">
</a>


### Sumario del curso

Esta lista de se irá actualizando conforme se publiquen nuevas entradas:

* [MATLAB-Java GUIs I. Una introducción]()