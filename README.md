# 🤖 Personalized Greeting Generator

Proyecto en Python que genera un saludo personalizado a partir de datos ingresados por el usuario. Está diseñado con una arquitectura modular para separar la lógica, utilidades y el punto de entrada de forma profesional.

## 🚀 Características

-   Interacción mediante `input()` para recibir nombre, edad y color
    favorito.
-   Validación de los datos ingresados para evitar entradas vacías.
-   Limpieza y formateo del texto para asegurar consistencia.
-   Uso de Programación Orientada a Objetos (OOP) para construir el
    mensaje.
-   Diseño modular: `main.py`, `builder.py` y `utils.py`.

## 📂 Estructura del Proyecto

    Personalized_Greeting_Generator/
    ├── src/
    │   ├── main.py
    │   └── generator/
    │       ├── __init__.py
    │       ├── builder.py
    │       └── utils.py  
    ├── LICENSE
    ├── README.md
    └── requirements.txt

## ▶️ Cómo Ejecutar

Desde la raíz del proyecto, ingresar al directorio `src/` y ejecutar:

``` bash
python main.py
```

## 💬 Ejemplo de Uso

    Enter your name: Oscar
    Enter your age: 33
    Enter your favorite color: blue

    ---- Personalized Greeting Message -----
    Hello Oscar!
    You are 33 years old.
    Your favorite color is Blue.
    You're now ready to start your Python adventure!

## ⚙️ Tecnologías y Dependencias

-   Python 3.x
-   No se requieren librerías externas para esta versión.

## 👤 Autor

**Oscar Caceres** GitHub: https://github.com/csodcaceres

## 📄 Licencia

MIT License
