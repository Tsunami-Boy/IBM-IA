def mostrar_integrantes():
    print("\n===========================================================\n")
    print("\n# Grupo 2")
    print("""
          ⭐ Benjamín Daza
          ⭐ Juan Castañeda
          ⭐ Melany Jofré
          ⭐ Victor Bonilla
          ⭐ Ivan Ortiz
          ⭐ Adriana Legua
          ⭐ Diana Alva
          ⭐ Tatiana Pinzón
    """)
    print("\n===========================================================\n")

def mostrar_preguntas_previas():
    print("\n===========================================================\n")
    print("""
    1. ¿Qué enfoque queremos abarcar?
    2. ¿Cómo se comportan las ventas?
    3. ¿Existen productos que generan mucho dinero?
    4. ¿Cuáles serán los productos más vendidos?
    5. ¿Los productos más vendidos son los que generan más dinero?
    """)
    print("\n===========================================================\n")

def mostrar_tema():
    print("\n===========================================================\n")
    print("""
    Tema: Comportamiento de ventas de productos respecto a sus categorías.

    Problema: El dueño de una tienda no logra identificar patrones de compra ni productos más rentables porque los datos están dispersos o sin procesar.

    Solución: Integrar y analizar las bases de datos (clientes, productos, ventas, detalle_ventas) para obtener tendencias como  productos más vendido o productos que más contribuyen por categoría, usando consultas o herramientas como Power BI, a partir de un procesamiento de datos compilado en un programa Python.
    """)
    print("\n===========================================================\n")

def mostrar_estructura():
    print("\n===========================================================\n")
    print("""
    Estructura: base de datos estructurada (excel) y relacional.

    Escala: se espera una escala mediana, ya que esta podría variar según la cantidad de ventas y clientes que interactúen con el sistema.

    Conforme a lo anterior, las tablas a trabajar son las siguientes:

    ✅ Tabla Clientes:
    * id_cliente (INT) (PK)
    * nombre_cliente (STRING)
    * email (STRING)
    * ciudad (STRING)
    * fecha (DATE)

    ✅ Detalle_ventas:
    * id_venta (INT) (PK)
    * id_producto (INT) (FK)
    * nombre_producto (STRING)
    * cantidad (INT)
    * precio_unitario (INT)
    * importe (INT)

    ✅ Productos:
    * id_producto (INT) (PK)
    * nombre_producto (STRING)
    * categoría (STRING)
    * precio_unitario (INT)

    ✅ Ventas:
    * id_ventas (INT) (PK)
    * fecha (DATE)
    * id_cliente (INT) (FK)
    * nombre_cliente (STRING)
    * email (STRING)
    * medio_pago (STRING)
    """)
    print("\n===========================================================\n")

def mostrar_pseudocodigo():
    print("\n===========================================================\n")
    print("""
    Pasos: 
    1. Cargar los datos de las BD
    2. Guardar en total_ventas los 5 productos más vendidos
    3. Guardar en total_importe el dinero total vendido por producto (precio unitario x cantidad vendido)
    4. Etiquetar cada producto como "Producto popular" o "Producto menos popular" si el producto está dentro de total_ventas.
    5. Guardar en total_generado_cat la cantidad de dinero total generado por cada categoría
    6. Guardar en porcentaje_participación la división de total_importe/total_generado_cat para cada producto y su categoria respectivamente
    7. Etiquetar cada producto como "Producto más relevante" o "Producto menos relevante" si el producto tiene un porcentaje de participación superior al 80%

    Pseudocódigo: 
          
    INICIO
    Cargar datos de Clientes, Ventas, Productos, Detalle_Ventas

    total_ventas ← calcular_ventas_por_producto() 
    total_importe ← calcular_importes_por_producto() 

    PARA cada producto EN Productos HACER
        SI producto EN total_ventas ENTONCES
            producto.etiqueta ← "Producto popular"
        SI NO ENTONCES
            producto.etiqueta ← "Producto menos popular"
        FIN 
    FIN

    total_generado_cat ← calcular_dinero_generado_por_categoria()
    porcentaje_participacion ← calcular_porcentaje_participacion_producto()

    PARA cada producto EN Productos HACER
        SI procentaje_participacion[producto] > 80% ENTONCES
            producto.etiqueta ← "Producto más rentable"
        SI NO
            producto.etiqueta ← "Producto menos rentable"
        FIN 
    FIN 

    Calcular_tendencias(Ventas, Detalle_Ventas)
    Mostrar_resultados()
    Guardar_reportes()

    FIN
    """)
    print("\n===========================================================\n")
    
def mostrar_ia():
    print("\n===========================================================\n")
    print("""
    </> Prompt 1: Soy estudiante de Python, crea un programa que pueda mostrar la documentación de forma interactiva, a través de los distintos temas del documento. Las interacciones solo deben ser por consola y a través del ingreso de números.

    * Se siguió la recomendación hecha por la IA, solo cambiando un par de detalles de la forma en que se muestran por terminal la documentación.

    </> Prompt 2: Soy colaborador en un grupo de desarrollo, hazme una estructura de documentación a partir de los siguientes temas: [temas], que sea separado por subtemas. Recomienda solo la estructura, no el desarrollo.

    * Se siguió la recomendación hecha por la IA, complementando con diagramas y pseudocódigo.
    """)
    print("\n===========================================================\n")

def informacion_basica():
    print("\n===========================================================\n")
    print('''
    ✅ Se muestran las primeras 4 filas del dataset para una mejor visualización.  
    ✅ La base de datos no tiene valores nulos ni vacíos.  
    ✅ No hay duplicados:
    - Clientes verificados por email → sin duplicados.  
    - Productos verificados por nombre → sin duplicados.  

    ✂️ Se eliminaron posibles espacios al inicio y final de las columnas tipo string.  
    🔍 Los tipos de datos fueron revisados y concuerdan correctamente, por lo que no fue necesario realizar cambios.
    ''')
    print("\n===========================================================\n")

def analisis_estadistico():
    print("\n===========================================================\n")
    print('''
    💰 Importe
    - Promedio: 7.730
    - Mediana: 6.702
    - Moda: 4.435  
    - Mínimo: 272  
    - Máximo: 24.865  
    - Distribución: 📈 sesgada positivamente

    📦 Cantidad Vendida
    - Promedio: 2.96  
    - Mediana: 3  
    - Moda: 2  
    - Mínimo: 1  
    - Máxima: 5  
    - Distribución: ⚖️ normal o ligeramente sesgada

    💵 Precio Unitario
    - Promedio: 2.654  
    - Mediana: 2.512  
    - Moda: 3.444  
    - Mínimo: 272  
    - Máximo: 4.982  
    - Distribución: 📈 sesgada positivamente
    ''')
    print("\n===========================================================\n")

def correlaciones():
    print("\n===========================================================\n")
    print('''
    | Relación                   | Coeficiente  | Interpretación                    |
    |----------------------------|--------------|-----------------------------------|
    | Importe ↔ Cantidad         | 0.599        | Relación directa                  |
    | Cantidad ↔ Precio Unitario | -0.074       | Sin relación lineal significativa |
    | Precio Unitario ↔ Importe  | 0.679        | Relación directa                  |

    🧩 Conclusiones:
    - El importe y la cantidad varían de forma directa.  
    - La cantidad y el precio unitario casi no tienen relación lineal.  
    - El precio unitario y el importe se relacionan directamente.
    ''')
    print("\n===========================================================\n")

def outliers():
    print("\n===========================================================\n")
    print('''
    Método usado: IQR (Rango Intercuartílico)

    | Variable        | Outliers detectados |
    |-----------------|---------------------|
    | Importe         | 7                   |
    | Cantidad        | 0                   |
    | Precio Unitario | 0                   |

    📊 Conclusión:  
    Los outliers se mantienen, ya que representan productos con ventas o importes excepcionalmente altos, relevantes para el análisis de rentabilidad.  
    Estos se observan claramente en los boxplots generados por el programa.
    ''')
    print("\n===========================================================\n")

def analisis_resultados():
    print("\n===========================================================\n")
    print('''
    A partir de los gráficos de barras se obtuvo:

    🏆 Productos con mayor importe total:
    1. Desodorante Aerosol  
    2. Queso Rallado 150g  
    3. Pizza Congelada Muzzarella  
    4. Ron 700 ml  
    5. Yerba Mate Suave 1KG  

    📦 Productos más vendidos (cantidad):
    1. Salsa de Tomate 500g  
    2. Queso Rallado 150g  
    3. Hamburguesas Congeladas x4  
    4. Vino Blanco 750ml  
    5. Aceitunas Verdes 200g 
    ''')
    print("\n===========================================================\n")

def proximos_pasos():
    print("\n===========================================================\n")
    print('''
    - 🔹 Separar los productos por categorías.  
    - 🔹 Analizar el método de pago más utilizado en los 5 productos más vendidos.  
    - 🔹 Guardar bases de datos con información procesada y relevante.
    ''')
    print("\n===========================================================\n")

def menu():
    print("Bienvenid@s a la Documentación del Grupo 2.")
    
    while True:
        print("=== Seleccione una de las opciones para ver ===")
        print("SPRINT 1 DOCUMENTACIÓN 📚")
        print("1. ❓ Preguntas Previas")
        print("2. ⚠️ Tema - Problema - Solución")
        print("3. 🏗️ Estructura - Tipo - Escala (de la BD)")
        print("4. 📍 Información - Pasos - Pseudocódigo")
        print("5. 🤖 Sugerencias de Copilot")
        print("6. 🏢 Integrantes Grupo 2")
        print("SPRINT 2 DOCUMENTACIÓN 📚")
        print("7. 📊 Información Básica ")
        print("8. 📈 Análisis estadístico")
        print("9. 🔗 Correlaciones")
        print("10. ⚠️ Outliers")
        print("11. 📉 Análisis de resultados")
        print("12. 🔜 Próximos pasos")
        print("13. 👋 Salir")

        opcion = input("Selecciona una opción (1-13): ")

        if opcion == "1":
            mostrar_preguntas_previas()
        elif opcion == "2":
            mostrar_tema()
        elif opcion == "3":
            mostrar_estructura()
        elif opcion == "4":
            mostrar_pseudocodigo()
        elif opcion == "5":
            mostrar_ia()
        elif opcion == "6":
            mostrar_integrantes()
        elif opcion == "7":
            informacion_basica()
        elif opcion == "8":
            analisis_estadistico()
        elif opcion == "9":
            correlaciones()
        elif opcion == "10":
            outliers()
        elif opcion == "11":
            analisis_resultados()
        elif opcion == "12":
            proximos_pasos()
        elif opcion == "13":
            print("Saliendo... 👋")
            break
        else:
            print("Opción no válida, intenta de nuevo.\n")

if __name__ == "__main__":
    menu()