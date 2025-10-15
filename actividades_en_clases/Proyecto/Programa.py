# grupo2_documentacion.py

def mostrar_tema():
    print("\n**Tema:** Comportamiento de ventas y clientes.")
    print("**Problema:** No se logra identificar patrones de compra ni productos más rentables porque los datos están dispersos.")
    print("**Solución:** Integrar y analizar las bases de datos (clientes, productos, ventas, detalle_ventas) "
          "para obtener patrones como clientes frecuentes, productos más vendidos y tendencias de compra, "
          "usando consultas SQL o herramientas como Power BI.\n")

def mostrar_estructura():
    print("\n**Estructura:** Base de datos estructurada (Excel) y relacional. "
          "Se agregan campos como 'Frecuencia_cliente' y 'Producto_popular'.")
    print("**Tipo:** OLAP (analítica, basada en históricos).")
    print("**Escala:** Mediana, dependiendo del volumen de ventas y clientes.\n")

def mostrar_pseudocodigo():
    print("""
INICIO
  Cargar datos de Clientes, Ventas, Productos, Detalle_Ventas

  promedio_compra ← calcular_promedio_productos_por_cliente()

  PARA cada cliente EN Clientes HACER
      productos_comprados ← contar_productos(cliente)
      SI productos_comprados > promedio_compra ENTONCES
          cliente.etiqueta ← "Cliente Frecuente"
      FIN SI
  FIN PARA

  top5_productos ← obtener_top5_productos_mas_vendidos()

  PARA cada producto EN Productos HACER
      SI producto EN top5_productos ENTONCES
          producto.etiqueta ← "Producto Popular"
      FIN SI
  FIN PARA

  Calcular_tendencias(Ventas, Detalle_Ventas)
  Mostrar_resultados()
  Guardar_reportes()

FIN
""")

def mostrar_integrantes():
    print("\n# Grupo 2")
    print("* Benjamín Daza\n* Juan Castañeda\n* Melany Jofré\n* Victor Bonilla\n* Ivan Ortiz\n* Adriana Legua\n* Diana Alva\n* Tatiana Pinzón\n")

def menu():
    while True:
        print("=== DOCUMENTACIÓN GRUPO 2 ===")
        print("1. Ver Tema - Problema - Solución")
        print("2. Ver Estructura - Tipo - Escala")
        print("3. Ver Pseudocódigo")
        print("4. Ver Integrantes")
        print("5. Salir")

        opcion = input("Selecciona una opción (1-5): ")

        if opcion == "1":
            mostrar_tema()
        elif opcion == "2":
            mostrar_estructura()
        elif opcion == "3":
            mostrar_pseudocodigo()
        elif opcion == "4":
            mostrar_integrantes()
        elif opcion == "5":
            print("Saliendo... 👋")
            break
        else:
            print("Opción no válida, intenta de nuevo.\n")

if __name__ == "__main__":
    menu()