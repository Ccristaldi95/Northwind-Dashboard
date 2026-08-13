import plotly.express as px

#Ingresos por categoría 

def grafico_ingresos_categoria(df):

    fig = px.bar(
        df,
        x="ingresos",
        y="CategoryName",
        title="Ingresos por categoría",
        color="ingresos",
        color_continuous_scale="Blues"
    )

    fig.update_layout(
        xaxis_title="Ingresos",
        yaxis_title="Categoría",
        title_x=0.5,
        title_font=dict(
        family="Arial",
        size=18),
        coloraxis_colorbar_title="Ingresos",
            font=dict(
            family="Arial",
            size=12
        )
        )

    return fig

#Unidades vendidas por categoría

def grafico_unidades_categoria(df):
    fig = px.bar(
        df,
        x="unidades_vendidas",
        y="CategoryName",
        title="Unidades vendidas por categoría",
        color="unidades_vendidas",
        color_continuous_scale="Blues"
    )

    fig.update_layout(
        xaxis_title="Unidades vendidas",
        yaxis_title="Categoría",
        title_x=0.5,
        title_font=dict(
        family="Arial",
        size=18),
        coloraxis_colorbar_title="Unidades vendidas",
          font=dict(
            family="Arial",
            size=12
        )
    )

    return fig

#Precio promedio por categoría 

def grafico_precio_categoria(df):
    fig = px.bar(
        df,
        x="precio_promedio",
        y="CategoryName",
        title="Precio promedio por categoría",
        color="precio_promedio",
        color_continuous_scale="Blues"
    )

    fig.update_layout(
        xaxis_title="Precio promedio",
        yaxis_title="Categoría",
        title_x=0.5,
        title_font=dict(
        family="Arial",
        size=18),
        coloraxis_colorbar_title="Precio promedio",
          font=dict(
            family="Arial",
            size=12
        )
    )

    return fig

#Productos

def grafico_productos_ingresos(df):

    fig = px.bar(
        df,
        x="ingresos",
        y="ProductName",
        orientation="h",
        title="Productos con mayores ingresos",
        color="ingresos",
        color_continuous_scale="Greens"
    )

    fig.update_layout(
        xaxis_title="Ingresos",
        yaxis_title="Producto",
        title_x=0.5,
        title_font=dict(
        family="Arial",
        size=18),
        coloraxis_colorbar_title="Ingresos",
          font=dict(
            family="Arial",
            size=12
        )
    )

    return fig

#Productos más vendidos
def grafico_productos_vendidos(df): 
    fig = px.bar(
    df,
    x="total_vendidos",
    y="ProductName",
    orientation="h",
    title="Productos más vendidos",
    color="total_vendidos",
    color_continuous_scale="Greens"
    )

    fig.update_layout(
    xaxis_title="Total de productos vendidos",
    yaxis_title="Producto",
    title_x=0.5,
    title_font=dict(
        family="Arial",
        size=18),
    coloraxis_colorbar_title="Total vendidos",
      font=dict(
            family="Arial",
            size=12
        )
)

    return fig

#Análisis de precios vs ventas

def grafico_scatter_precio_unidades(df): 
    fig = px.scatter(
        df,
        x="Price",
        y="unidades_vendidas",
        title="Precio vs Unidades Vendidas",
        color="unidades_vendidas",
        color_continuous_scale="Greens"
    )

    fig.update_layout(
        xaxis_title="Precio",
        yaxis_title="Unidades vendidas",
        title_x=0.5,
        title_font=dict(
        family="Arial",
        size=18),
        coloraxis_colorbar_title="Unidades vendidas",
          font=dict(
            family="Arial",
            size=12
        )
    )

    return fig

#Clientes

def grafico_clientes(df):

    fig = px.bar(
        df,
        x="ingresos",
        y="CustomerName",
        title="Top 10 clientes",
        color="ingresos",
        color_continuous_scale="Purples"
    )

    fig.update_layout(
        xaxis_title="Ingresos",
        yaxis_title="Cliente",
        title_x=0.5,
        title_font=dict(
        family="Arial",
        size=18),
        coloraxis_colorbar_title="Ingresos",
          font=dict(
            family="Arial",
            size=12
        )
    )

    return fig

#Empleados

def grafico_empleados_ingresos(df):

    fig = px.bar(
        df,
        x="ingresos",
        y="Empleado",
        title="Ingresos por empleado",
        color="ingresos",
        color_continuous_scale="Oranges"
    )

    fig.update_layout(
        xaxis_title="Ingresos",
        yaxis_title="Empleado",
        title_x=0.5,
        title_font=dict(
        family="Arial",
        size=18),
          font=dict(
            family="Arial",
            size=12
        )
    )

    return fig

#Empleados que procesan más órdenes 

def grafico_empleados_ordenes(df):
    
    fig = px.bar(
            df,
            x="ordenes_procesadas",
            y="Empleado",
            title="Empleados que procesan más órdenes",
            color="ordenes_procesadas",
            color_continuous_scale="Oranges"
    )

    fig.update_layout(
        xaxis_title="Nº de órdenes procesadas",
        yaxis_title="Empleado",
        title_x=0.5,
        title_font=dict(
        family="Arial",
        size=18),
          font=dict(
            family="Arial",
            size=12
        )
    )

    return fig

#Evolución mensual

def grafico_ventas_mensuales(df):

    fig = px.line(
        df,
        x="mes",
        y="ingresos",
        title="Evolución mensual de ingresos",
        markers=True
    )

    fig.update_layout(
        xaxis_title="Mes",
        yaxis_title="Ingresos",
        title_x=0.5,
        title_font=dict(
        family="Arial",
        size=18),
          font=dict(
            family="Arial",
            size=12
        )
    )

    return fig