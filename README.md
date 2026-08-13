#  Dashboard Comercial - Northwind

Dashboard interactivo desarrollado en Python y Dash para analizar el desempeño comercial de la base de datos Northwind.

##  Objetivo

Analizar las ventas y el desempeño comercial de la empresa mediante indicadores y visualizaciones que permitan identificar tendencias y principales actores del negocio.

##  Tecnologías utilizadas

- Python
- Pandas
- SQLite
- SQL
- Plotly
- Dash

##  Análisis realizado

El dashboard permite analizar:

- KPIs generales del negocio
- Evolución mensual de los ingresos
- Ingresos por categoría
- Unidades vendidas por categoría
- Precio promedio por categoría
- Productos con mayores ingresos
- Productos más vendidos
- Relación entre precio y unidades vendidas
- Principales clientes por ingresos
- Desempeño de empleados
- Cantidad de órdenes procesadas por empleado

##  Principales hallazgos

- Los ingresos totales ascienden a $386.424,23.
- La categoría Bebidas se destaca por sus ingresos y unidades vendidas.
- Los productos con mayores ingresos no necesariamente son los más vendidos.
- Los 10 principales clientes concentran aproximadamente el 51% de los ingresos.
- Margaret Peacock presenta el mayor desempeño tanto en ingresos como en órdenes procesadas.
- La evolución mensual permite identificar cambios en el nivel de ingresos a lo largo del período analizado.

##  Estructura del proyecto

```text
Northwind_Dashboard/
│
├── dashboard.py
├── Consultas.py
├── Graficos.py
├── northwind.db
├── requirements.txt
