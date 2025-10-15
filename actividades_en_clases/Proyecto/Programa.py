def mostrar_integrantes():
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

def mostrar_preguntas_previas():
    print("""
    1. ¿Qué enfoque queremos abarcar?
    2. ¿Cómo se comportan las ventas?
    3. ¿Existen productos que generan mucho dinero?
    4. ¿Cuáles serán los productos más vendidos?
    5. ¿Los productos más vendidos son los que generan más dinero?
    """)

def mostrar_tema():
    print("""
    Tema: Comportamiento de ventas de productos respecto a sus categorías.

    Problema: El dueño de una tienda no logra identificar patrones de compra ni productos más rentables porque los datos están dispersos o sin procesar.

    Solución: Integrar y analizar las bases de datos (clientes, productos, ventas, detalle_ventas) para obtener tendencias como  productos más vendido o productos que más contribuyen por categoría, usando consultas o herramientas como Power BI, a partir de un procesamiento de datos compilado en un programa Python.
    """)

def mostrar_estructura():
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

def mostrar_pseudocodigo():
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
    
def mostrar_ia():
    print("""
    </> Prompt 1: Soy estudiante de Python, crea un programa que pueda mostrar la documentación de forma interactiva, a través de los distintos temas del documento. Las interacciones solo deben ser por consola y a través del ingreso de números.

    * Se siguió la recomendación hecha por la IA, solo cambiando un par de detalles de la forma en que se muestran por terminal la documentación.

    </> Prompt 2: Soy colaborador en un grupo de desarrollo, hazme una estructura de documentación a partir de los siguientes temas: [temas], que sea separado por subtemas. Recomienda solo la estructura, no el desarrollo.

    * Se siguió la recomendación hecha por la IA, complementando con diagramas y pseudocódigo.
    """)

def menu():
    print("Bienvenid@s a la Documentación del Grupo 2.")
    
    while True:
        print("=== Seleccione una de las opciones para ver ===")
        print("1. ❓ Preguntas Previas")
        print("2. ⚠️ Tema - Problema - Solución")
        print("3. 🏗️ Estructura - Tipo - Escala (de la BD)")
        print("4. 📍 Información - Pasos - Pseudocódigo")
        print("5. 🤖 Sugerencias de Copilot")
        print("6. 🏢 Integrantes Grupo 2")
        print("7. Salir")

        opcion = input("Selecciona una opción (1-7): ")

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
            print("Saliendo... 👋")
            break
        else:
            print("Opción no válida, intenta de nuevo.\n")

if __name__ == "__main__":
    menu()