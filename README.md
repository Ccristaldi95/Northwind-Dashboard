# Dashboard Comercial - Northwind

Análisis exploratorio y dashboard interactivo desarrollado en Python
para analizar el desempeño comercial de la base de datos Northwind.

##  Dashboard Interactivo

[Ver Dashboard Interactivo]

##  Análisis exploratorio de datos

El proyecto comienza con un análisis exploratorio de los datos,
utilizando Python, Pandas, SQL y visualizaciones para identificar
patrones de ventas, productos, categorías y clientes.

 [Ver EDA](EDA/Northwind_EDA.ipynb)

##  Objetivo

Analizar las ventas y el desempeño comercial de la empresa mediante
indicadores y visualizaciones que permitan identificar tendencias y
principales actores del negocio.

##  Tecnologías

- Python
- Pandas
- SQLite
- Matplotlib
- Seaborn
- Plotly
- Dash

##  Dashboard

El dashboard permite analizar:

- KPIs generales
- Evolución mensual de ingresos
- Ingresos por categoría
- Unidades vendidas
- Productos
- Clientes
- Desempeño de empleados


##  Principales hallazgos

- Los ingresos totales ascienden a $386.424,23.
- La categoría Bebidas se destaca por sus ingresos y unidades vendidas.
- Los productos con mayores ingresos no necesariamente son los más vendidos.
- Los 10 principales clientes concentran aproximadamente el 51% de los ingresos.
- Margaret Peacock presenta el mayor desempeño tanto en ingresos como en órdenes procesadas.
- La evolución mensual permite identificar cambios en el nivel de ingresos a lo largo del período analizado.

##  Estructura del proyecto

Northwind-Dashboard/
│
├── EDA/
│   └── Northwind_EDA.ipynb
├── Dashboard.py
├── Consultas.py
├── Graficos.py
├── northwind.db
├── requirements.txt
└── README.md
