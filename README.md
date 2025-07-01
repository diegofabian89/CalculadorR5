# Calculador Realise 5


## Descripción

CalculadorR5 es una aplicación de consola para realizar operaciones matemáticas básicas (suma, resta, multiplicación y división), con un sistema de historial y generación de reportes gráficos de las operaciones realizadas por los usuarios esta es la `version 5 `.

---

## Estructura del proyecto

CalculadorR5/  
|── img / contine las graficas generadas del dataframe en png




│  
├── .venv/ # Entorno virtual de Python  
├── classes/ # Carpeta para clases de la aplicacion  
├── data/  
│ └── historial.csv # Archivo CSV que almacena el historial de operaciones  
├── models/  
│ ├── ui/ # Interfaz de usuario y menú  
│ │ ├── init.py  
│ │ ├── menu.py # Menú principal de la aplicación  
│ │ ├── secondMenu.py # Segundo menú o submenú   
│ │ ├── user_options.py # Opciones específicas para el usuario  
│ │ └── welcome.py # Pantalla o lógica de bienvenida al usuario  
│ ├── init.py  
│ ├── calculator_utils.py # Funciones de cálculo (suma, resta, etc.)  
│ ├── data_utils.py # Utilidades para manejo de datos y CSV  
│ ├── report.py # Generación de reportes y gráficos estadísticos en pdf   
│ └── validation_utils.py # Funciones de validación de entradas y datos   
├── reports/ Contiene las graficas generadas del dataframe en formato png , ademas de un archivo pdf que contiene todas estas graficas juntas  
├── main.py # Archivo principal para ejecutar la aplicación  


---

## Funciones principales

- **main.py**  
  Punto de entrada de la aplicación, controla el flujo general y la interacción con el usuario.

- **models/ui/menu.py**  
  Contiene el menú principal donde el usuario selecciona las opciones y se recogen los datos para las operaciones.

- **models/calculator_utils.py**  
  Funciones que realizan las operaciones matemáticas básicas y recoge los resultados

- **models/data_utils.py**  
  Funciones para gestionar la lectura y escritura del historial en archivos CSV.

- **models/report.py**  
  Funciones para generar reportes gráficos sobre las operaciones realizadas, utilizando librerías como `pandas`, `matplotlib` y `seaborn`.

- **models/validation_utils.py**  
  Funciones que validan las entradas del usuario para evitar errores y entradas inválidas.

- **data/historial.csv**  
  Archivo donde se almacena el historial de operaciones de los usuarios.

## Cómo ejecutar el proyecto

1. Clonar el repositorio  
   ```bash
   git clone https://github.com/diegofabian89/CalculadorR5.git

### Crear y activar el entorno virtual

```shell

python -m venv .venv
```
```
source .venv/bin/activate   # En Linux/Mac
.venv\Scripts\activate      # En Windows  
```
### Instalar dependencias
``` shell
pip install -r requirements.txt
```
### Ejecutar la aplicación

``` python

python main.py

```

## Requisitos
`Python 3.x`

`pandas`

`matplotlib`

`seaborn`

