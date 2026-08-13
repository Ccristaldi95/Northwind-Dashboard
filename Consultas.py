import sqlite3
import pandas as pd

# Conexión con la base de datos 
conn = sqlite3.connect("/Users/constanza/Documents/SQL con Dalto/northwind.db")

# Función para obtener KPIs

def obtener_kpis():

    query = """
    SELECT
        SUM(p.Price * od.Quantity) AS ingresos_totales,
        COUNT(DISTINCT o.OrderID) AS ordenes,
        COUNT(DISTINCT o.CustomerID) AS clientes,
        (SELECT COUNT(*) FROM Products) AS productos
    FROM Orders o
    INNER JOIN OrderDetails od
        ON o.OrderID = od.OrderID
    INNER JOIN Products p
        ON od.ProductID = p.ProductID
    """

    return pd.read_sql_query(query, conn)

kpis = obtener_kpis()
print(kpis)

# Función: ingresos por categoría

def ingresos_categoria():

    query = """
    SELECT
        CategoryName,
        SUM(p.Price*od.Quantity) AS ingresos

    FROM Categories c

    INNER JOIN Products p
        ON c.CategoryID = p.CategoryID

    INNER JOIN OrderDetails od
        ON p.ProductID = od.ProductID

    GROUP BY CategoryName
    ORDER BY ingresos DESC
    """

    return pd.read_sql_query(query, conn)

# Función: Unidades por categoría 

def unidades_categoria():

    query = """
    SELECT CategoryName, sum(quantity) as unidades_vendidas FROM Categories c
    inner join Products p ON c.CategoryID=p.CategoryID
    inner join OrderDetails od ON p.ProductID=od.ProductID
    GROUP by c.CategoryID
    order by unidades_vendidas DESC"""

    return pd.read_sql_query(query, conn)

# Precio promedio por categoría 

def precio_categoria():
    query = '''SELECT CategoryName, round(avg(price)) as precio_promedio FROM Categories c
    inner join Products p ON c.CategoryID=p.CategoryID
    inner join OrderDetails od ON p.ProductID=od.ProductID
    group by c.CategoryID
    order by precio_promedio'''
    
    return pd.read_sql_query(query, conn)

# Función: ingresos por productos

def top_productos_ingresos():
    query = ''' SELECT ProductName, sum(quantity *Price) as ingresos FROM Products p
    inner join OrderDetails od ON p.ProductID=od.ProductID
    group by p.ProductID
    order by ingresos DESC
    LIMIT 10
    '''
    return pd.read_sql_query(query, conn)

# Función: Productos mas vendidods

def top_productos_masvendidos():
    query = '''SELECT ProductName, sum(quantity) as total_vendidos FROM Products p
    inner join OrderDetails od ON p.ProductID=od.ProductID
    GROUP by p.ProductID
    order by total_vendidos DESC
    LIMIT 10 '''
    return pd.read_sql_query(query, conn)

#Función: precios vs ventas

def precio_vs_unidades():
    
    query= '''SELECT
    ProductName,
    Price,
    SUM(Quantity) AS unidades_vendidas
    FROM Products p
    INNER JOIN OrderDetails od
    ON p.ProductID = od.ProductID
    GROUP BY p.ProductID'''
    return pd.read_sql_query(query, conn)

#Función: top 10 mejores clientes

def top_clientes():
    query = '''SELECT CustomerName, sum(Price*quantity) as ingresos FROM Customers c
    inner join Orders o ON c.CustomerID=o.CustomerID
    inner join OrderDetails od ON od.OrderID=o.OrderID
    inner join Products p ON od.ProductID=p.ProductID
    group by c.CustomerID
    order by ingresos DESC
    LIMIT 10 '''
    df = pd.read_sql_query(query, conn)
   
  # Calcular ingresos totales
    query_total = """
        SELECT SUM(p.Price * od.Quantity) AS ingresos_totales
        FROM OrderDetails od
        INNER JOIN Products p
            ON od.ProductID = p.ProductID
        """
    ingresos_totales = pd.read_sql_query(query_total, conn).iloc[0, 0]
    
    df["participacion"] = (
        df["ingresos"] / ingresos_totales * 100
    ).round(2)

    return df

#Función: Top 10 empleados que generan más ingresos

def top_empleados():
    
    query = '''SELECT FirstName || ' ' || LastName AS Empleado, sum(Price*quantity) as ingresos  FROM Employees e
    inner join Orders o ON e.EmployeeID=o.EmployeeID
    inner join OrderDetails od ON od.OrderID=o.OrderID
    inner join Products p ON od.ProductID=p.ProductID
    group by e.EmployeeID
    order by ingresos DESC
    LIMIT 10'''

    return pd.read_sql_query(query,conn)

#Función: empleados que genera más órdenes 

def ordenes_empleados():
    
    query = '''SELECT FirstName || ' ' || LastName AS Empleado, count(OrderID) as ordenes_procesadas  FROM Employees e
    inner join Orders o ON e.EmployeeID=o.EmployeeID
    group by e.EmployeeID
    order by ordenes_procesadas DESC'''

    return pd.read_sql_query(query,conn)

#Función: ingresos por mes

def ventas_mensuales():
    query = '''SELECT
    strftime('%Y-%m', OrderDate) AS mes,
    SUM(p.Price * od.Quantity) AS ingresos
    FROM Orders o
    INNER JOIN OrderDetails od
    ON o.OrderID = od.OrderID
    INNER JOIN Products p
    ON od.ProductID = p.ProductID
    GROUP BY mes
    ORDER BY mes'''

    return pd.read_sql_query(query, conn)

