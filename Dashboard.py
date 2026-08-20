from dash import Dash, html, dcc, dash_table
import os

from Consultas import *
from Graficos import *

#Creamos la aplicación 

app = Dash(__name__)

app.title = "Dashboard Comercial Northwind"

#--------------------------------------------------------------------
#Obtenemos los datos llamando a todas las funciones de consultas.py.

# KPIs
kpis = obtener_kpis()

# Categorías
df_ingresos_categoria = ingresos_categoria()
df_unidades_categoria = unidades_categoria()
df_precio_categoria = precio_categoria()

# Productos
df_productos_ingresos = top_productos_ingresos()
df_productos_vendidos = top_productos_masvendidos()
df_scatter = precio_vs_unidades()

# Clientes
df_clientes = top_clientes()

df_clientes_tabla = df_clientes.copy()

df_clientes_tabla["ingresos"] = df_clientes_tabla["ingresos"].map(
    lambda x: f"${x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
)

df_clientes_tabla["participacion"] = df_clientes_tabla["participacion"].map(
    lambda x: f"{x:.2f}".replace(".", ",") + "%"
)

# Empleados
df_empleados_ingresos = top_empleados()
df_empleados_ordenes = ordenes_empleados()

# Tiempo
df_mensual = ventas_mensuales()

#--------------------------------------------------------------------

#Creamos los grágicos usando las funciones de graficos.py

fig_ingresos_categoria = grafico_ingresos_categoria(df_ingresos_categoria)

fig_unidades_categoria = grafico_unidades_categoria(df_unidades_categoria)

fig_precio_categoria = grafico_precio_categoria(df_precio_categoria)

fig_productos_ingresos = grafico_productos_ingresos(df_productos_ingresos)

fig_productos_vendidos = grafico_productos_vendidos(df_productos_vendidos)

fig_scatter = grafico_scatter_precio_unidades(df_scatter)

fig_clientes = grafico_clientes(df_clientes)

fig_empleados_ingresos = grafico_empleados_ingresos(df_empleados_ingresos)

fig_empleados_ordenes = grafico_empleados_ordenes(df_empleados_ordenes)

fig_mensual = grafico_ventas_mensuales(df_mensual)

#--------------------------------------------------------------------
#Creamos la funcion crear tarjetas 
def crear_tarjeta(titulo, valor):

    return html.Div(
        [
            html.H4(
                titulo,
                style={
                    "margin": "0",
                    "color": "#555555",
                    "fontSize": "16px"
                }
            ),

            html.H2(
                valor,
                style={
                    "margin": "10px 0 0 0",
                    "color": "#4B3F72",
                    "fontSize": "28px"
                }
            )
        ],

        style={
            "backgroundColor": "#F8F6FC",
            "border": "none",
            "borderRadius": "12px",
            "padding": "20px",
            "textAlign": "center",
            "flex": "1",
            "maxWidth": "220px",
            "boxShadow": "0 3px 10px rgba(0,0,0,0.12)"
        }
    )
#--------------------------------------------------------------------
#Creamos la primer pestaña

app.layout = html.Div([ #Todo lo que esté dentro de este Div será la interfaz de mi aplicación
    
    html.H1(
    "Dashboard Comercial - Northwind",
    style={
        "textAlign": "center",
        "color": "#4B3F72",
        "fontSize": "32px",
        "marginBottom": "5px"
    }
),

html.P(
    "Análisis de ventas, clientes, productos y desempeño comercial",
    style={
         "textAlign": "center",
        "color": "#666666",
        "fontSize": "16px",
        "marginTop": "0px",
        "marginBottom": "25px"
    }
),

    dcc.Tabs([ #Acá creamos un conjunto de pestañas.

        dcc.Tab( #Esto crea una pestaña, que la llamamos resumen
                label="Resumen",
                children=[
                    html.H2("Resumen Ejecutivo"),

                    html.Hr(), #crea una línea horizontal
                    
                     html.Div(
                    
                        [   

                            crear_tarjeta(
                                "💰 Ingresos Totales",
                                f"${kpis['ingresos_totales'].iloc[0]:,.2f}"
                            ),
                    
                            crear_tarjeta(
                                "🛒 Órdenes",
                                kpis["ordenes"].iloc[0]
                            ),

                            crear_tarjeta(
                                "👥 Clientes",
                                kpis["clientes"].iloc[0]
                            ),

                            crear_tarjeta(
                                "📦 Productos",
                                kpis["productos"].iloc[0]
                            )
                        ],
            
                        style={
                            "display": "flex", #acomoda los elementos en fila
                            "justifyContent": "space-around" #deja espacios entre ellas
                        } 

                     ),
                     
                    html.Br(), #salto de línea
                    
                    dcc.Graph(
                        figure=fig_mensual
                    ),
                    html.Div(
    [
        html.H3(
            "Insights principales",
            style={
                "color": "#4B3F72",
                "marginBottom": "10px"
            }
        ),

        html.P(
            "El análisis muestra la evolución de los ingresos a lo largo del período "
            "y permite identificar los principales indicadores comerciales de Northwind."
        )
    ],
    style={
        "backgroundColor": "#F8F6FC",
        "borderRadius": "12px",
        "padding": "20px",
        "marginTop": "20px",
        "boxShadow": "0 2px 8px rgba(0,0,0,0.08)"
    }
)
                
                ]
            ),
                
        dcc.Tab(
                label="Categorías", 
                    children=[ #Todo lo que pongamos acá aparecerá cuando el usuario haga clic en "Categorías".
                    html.H2("Análisis de Categorías"),

                    html.P(
                        "En esta sección se analiza el desempeño de las categorías de productos "
                        "según los ingresos generados, las unidades vendidas y el precio promedio."),

                    html.Hr(),
                    
                    html.Div([

                            dcc.Graph(
                                figure=fig_ingresos_categoria,
                                style={"width": "50%"}
                            ),

                            dcc.Graph(
                                figure=fig_unidades_categoria,
                                style={"width": "50%"}
                            )

                        ],

                        style={
                            "display": "flex",
                            "justifyContent": "space-between",
                            "gap": "20px"
                        }

                    ),

                    dcc.Graph(
                        figure=fig_precio_categoria
                    ),
                    
                    html.H3("Conclusión"),

                    html.P(
                        "Las categorías presentan comportamientos diferentes en términos de ingresos, "
                        "volumen de ventas y precio promedio. Una categoría puede generar mayores ingresos "
                        "por vender productos de mayor valor, mientras que otra puede destacarse por vender "
                        "una mayor cantidad de unidades."
                    )

                ]
            ),
        
        dcc.Tab(
                label="Productos",
                children=[
                    html.H2("Análisis de Productos"),

                    html.P(
                        "En esta sección se analizan los productos que generan mayores ingresos, "
                        "los más vendidos y la relación entre el precio y las unidades comercializadas."
                    ),
                    html.Hr(),

                html.Div(

                    [

                        dcc.Graph(
                            figure=fig_productos_ingresos,
                            style={"width": "50%"}
                        ),

                        dcc.Graph(
                            figure=fig_productos_vendidos,
                            style={"width": "50%"}
                        )

                    ],

                    style={
                         "display": "flex",
                        "justifyContent": "space-between",
                        "gap": "20px"
                    }

                ),

                dcc.Graph(
                    figure=fig_scatter
                ),
                
                html.H3("Conclusión"),

                html.P(
                    "Los productos que generan mayores ingresos no necesariamente son los más vendidos. "
                    "Esto indica que el precio del producto influye significativamente en la generación de ingresos, "
                    "por lo que vender un mayor volumen no siempre implica obtener mayores ganancias.")
            ]),
            
            dcc.Tab(
                    label="Clientes",
                    children=[

                    html.H2("Análisis de Clientes"),

                    html.P(
                        "En esta sección se identifican los clientes que generan mayores ingresos "
                        "para la empresa, permitiendo reconocer aquellos con mayor impacto en las ventas."
                    ),

                    html.Hr(),

                    dcc.Graph(
                        figure=fig_clientes
                    ),
                    
                    dash_table.DataTable(

                        data=df_clientes_tabla.to_dict("records"),

                        columns=[
                            {"name": "Cliente", "id": "CustomerName"},
                            {"name": "Ingresos", "id": "ingresos"},
                            {"name": "Participación (%)", "id": "participacion"},
                        ],

                        style_table={
                            "width": "70%",
                            "margin": "auto"
                        },

                        style_header={
                            "backgroundColor": "#5B3A9A",
                            "color": "white",
                            "fontWeight": "bold",
                            "textAlign": "center"
                        },

                        style_cell={
                            "textAlign": "center",
                            "padding": "8px"
                        },

                        style_data_conditional=[
                            {
                                "if": {"row_index": "odd"},
                                "backgroundColor": "#f8f9fa"
                            }
                        ]

                    ),

                    html.H3("Conclusión"),

                    html.P(
                        "Los ingresos se concentran en un grupo reducido de clientes. "
                        "Los 10 principales clientes representan aproximadamente el 51% "
                        "de los ingresos totales, lo que resalta la importancia de implementar "
                        "estrategias de fidelización para estos clientes clave."
                    )

                ]
            ),
            dcc.Tab(
                label="Empleados",
                children=[

                    html.H2("Análisis de Empleados"),

                    html.P(
                        "En esta sección se analiza el desempeño de los empleados "
                        "considerando los ingresos generados y la cantidad de órdenes procesadas."
                    ),

                    html.Hr(),

                    html.H3("Ingresos generados por empleado"),

                    dcc.Graph(
                        figure=fig_empleados_ingresos
                    ),

                    html.H3("Órdenes procesadas por empleado"),

                    dcc.Graph(
                        figure=fig_empleados_ordenes
                    ),

                    html.H3("Conclusión"),

                    html.P(
                        "Si bien Margaret Peacock lidera tanto en ingresos como en cantidad de órdenes procesadas, "
                        "el resto de los empleados no mantiene exactamente el mismo orden. "
                        "Esto indica que procesar una mayor cantidad de órdenes no siempre implica generar mayores ingresos, "
                        "ya que el valor económico de las ventas también depende del tipo de productos comercializados."
                    )

                ]
            ),
            
            dcc.Tab(
                label="Conclusiones",
                children=[

                    html.H2("📋 Conclusiones Generales"),

                    html.Hr(),

                    html.H3("Resumen del análisis"),

                    html.Ul([

                        html.Li(
                            "Los ingresos totales ascienden a "
                            f"${kpis['ingresos_totales'].iloc[0]:,.2f}, "
                            "distribuidos entre múltiples categorías, productos, clientes y empleados."
                        ),

                        html.Li(
                            "La categoría 'Bebidas' es la que genera mayores ingresos y también lidera en unidades vendidas, "
                            "confirmando su importancia dentro del negocio."
                        ),

                        html.Li(
                            "Los productos con mayores ingresos no coinciden necesariamente con los más vendidos, "
                            "lo que demuestra que el precio del producto tiene un impacto importante sobre la facturación."
                        ),

                        html.Li(
                            "Los diez principales clientes concentran aproximadamente el 51% de los ingresos, "
                            "evidenciando una fuerte dependencia de un grupo reducido de clientes."
                        ),

                        html.Li(
                            "Margaret Peacock es la empleada con mejor desempeño tanto en ingresos como en órdenes procesadas. "
                            "Sin embargo, para el resto de los empleados la cantidad de órdenes no siempre se traduce en mayores ingresos."
                        ),

                        html.Li(
                            "La evolución mensual muestra un crecimiento sostenido de los ingresos entre octubre de 1996 y enero de 1997, "
                            "alcanzando su máximo en enero. La disminución observada en febrero probablemente se deba a que el mes no cuenta con todos los registros."
                        )

                    ]),

                    html.Hr(),

                    html.H3("Conclusión Final"),

                    html.P(
                        "El análisis permitió identificar los principales impulsores del negocio y evidenció que "
                        "la generación de ingresos depende de múltiples factores, como el precio de los productos, "
                        "la fidelización de clientes estratégicos y el desempeño comercial de los empleados. "
                        "Este dashboard facilita el monitoreo de indicadores clave y puede servir como herramienta "
                        "de apoyo para la toma de decisiones."
                    )

                ]
            ),

        ])
    ],
                       style={
                        "backgroundColor": "#FAFAFC",
                        "minHeight": "100vh", #hace que el fondo ocupe toda la altura de la pantalla, incluso si una pestaña tiene poco contenido.
                        "padding": "20px 40px",
                        "fontFamily": "Arial"
    }
)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8050))
    app.run(host="0.0.0.0", port=port)