**Biblioteca investigada:** PyQt6  

---

## 1. Selección de la biblioteca
Se ha seleccionado **PyQt6** como biblioteca para el desarrollo de la interfaz gráfica. Es un conjunto de enlaces de Python para Qt (un robusto framework de C++), diseñado nativamente bajo el paradigma de **Programación Orientada a Objetos (POO)**, lo cual permite estructurar aplicaciones escalables mediante clases, atributos y métodos.

---

## 2. Investigación

1. **¿Qué es la biblioteca seleccionada y cuál es su propósito principal?**  
   Es un *wrapper* o envoltorio de Python para la biblioteca Qt. Su propósito es facilitar la creación de aplicaciones de escritorio multiplataforma con interfaces gráficas modernas, fluidas y profesionales.

2. **¿Qué tipo de aplicaciones permite desarrollar?**  
   Permite desarrollar desde utilidades y herramientas de escritorio sencillas hasta paneles de control complejos (*dashboards*), software científico y reproductores multimedia multiplataforma (Windows, macOS y Linux).

3. **¿Cómo se instala y qué requisitos necesita?**  
   - **Requisitos:** Python 3.8 o superior.
   - **Instalación:** Se instala fácilmente mediante el gestor de paquetes `pip` ejecutando en la terminal:
     ```bash
     pip install PyQt6
     ```

4. **¿Cuáles son sus principales componentes o elementos gráficos?**  
   - **`QMainWindow` / `QWidget`:** Ventana principal y contenedores base.
   - **Widgets:** Elementos interactivos como botones (`QPushButton`), etiquetas de texto (`QLabel`), campos de texto (`QLineEdit`), entre otros.
   - **Layouts (Diseños):** Gestores automáticos de posicionamiento como `QVBoxLayout` (vertical) y `QHBoxLayout` (horizontal).

5. **¿Cómo maneja los eventos del usuario (clics del mouse, teclado)?**  
   Utiliza un sistema denominado **Señales y Slots (Signals & Slots)**. Cuando ocurre una acción del usuario (ej. hacer clic en un botón), el widget emite una *señal* (como `clicked`). Dicha señal se conecta a un *slot* (una función o método de clase) que ejecuta la lógica de respuesta.

6. **¿Qué ventajas y limitaciones presenta frente a Tkinter?**  
   - **Ventajas:** Apariencia visual mucho más moderna y nativa, sistema de diseño automático superior (`layouts`), arquitectura 100% orientada a objetos y mayor robustez.
   - **Limitaciones:** Curva de aprendizaje ligeramente más pronunciada que Tkinter y mayor tamaño en los archivos compilados/ejecutables.

---

## 3. Descripción del Ejemplo Mínimo (Contador Interactivo)
La aplicación desarrollada consiste en un **contador numérico interactivo**. Cuenta con:
- Una ventana principal gráfica.
- Etiquetas de texto (`QLabel`) que muestran el título y el valor actual del contador.
- Un botón interactivo (`QPushButton`) para incrementar el valor.
- Un evento de clic que actualiza en tiempo real la interfaz gráfica sin necesidad de reiniciar.

---

## 4. Explicación del Funcionamiento
1. **Cómo se crea la ventana principal:** Se define una clase (`ContadorApp`) que hereda de `QMainWindow`. En su constructor, se configuran propiedades como el título con `setWindowTitle()` y las dimensiones de la ventana con `setFixedSize()`.
2. **Cómo se crean y muestran los componentes gráficos:** Se instancian objetos de tipo `QLabel` y `QPushButton`. Estos componentes se organizan visualmente de manera vertical utilizando un contenedor de diseño (`QVBoxLayout`).
3. **Qué evento se implementó y cómo se detecta:** Se implementó el evento de **clic del mouse** sobre el botón interactivo. PyQt lo detecta de forma automática a través de su señal nativa `clicked`.
4. **Qué método responde al evento:** El método de clase `incrementar_contador(self)` actúa como el *slot* receptor que se activa automáticamente cada vez que el botón es presionado.
5. **Cómo se modifica la interfaz después de la interacción:** Dentro del método, se incrementa la variable interna del contador (`self.contador`) y se invoca inmediatamente el método `setText()` sobre la etiqueta numérica para refrescar su contenido en pantalla.

---

## 5. Reto Adicional: Aplicación de Programación Orientada a Objetos (POO)
El código implementa el paradigma de POO de la siguiente manera:
- **Herencia:** La clase principal `ContadorApp` hereda de `QMainWindow`, reutilizando el ciclo de vida y la estructura completa de una ventana.
- **Encapsulamiento y Atributos:** El estado de la aplicación (`self.contador`) y los widgets visuales se gestionan como atributos de la instancia (`self`), asegurando un acceso limpio y ordenado desde cualquier método de la clase.
- **Métodos especializados:** La lógica de interacción se encuentra aislada en el método `incrementar_contador()`, separando la maquetación visual del procesamiento de datos.

---

## 🚀 Instrucciones de Instalación y Ejecución
1. Clona este repositorio o descarga los archivos fuente (`main.py`).
2. Abre tu terminal en la carpeta del proyecto.
3. Instala la biblioteca PyQt6 ejecutando:
   ```bash
   pip install PyQt6