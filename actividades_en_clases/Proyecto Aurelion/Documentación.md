Grupo 2

* Benjamín Daza
* Juan Castañeda
* Melany Jofré
* Victor Bonilla
* Ivan Ortiz
* Adriana Legua
* Diana Alva
* Tatiana Pinzón

## Tema - Problema - Solución

**Tema:** Comportamiento de ventas y clientes.

**Problema:** No se logra identificar patrones de compra ni productos más rentables porque los datos están dispersos.

**Solución:** Integrar y analizar las bases de datos (clientes, productos, ventas, detalle_ventas) para obtener patrones como clientes frecuentes, productos más vendidos y tendencias de compra, usando consultas SQL o herramientas como Power BI.

## Estructura - Tipo - Escala (de la BD)

**Estructura:** base de datos estructurada (excel) y relacional. Se agregan campos como: "Frecuencia_cliente", "Producto_popular". 

**Tipo:** OLAP, ya que se usaría para el análisis de datos a partir de históricos y registros. 

**Escala:** se espera una escala mediana, ya que esta podría variar según la cantidad de ventas y clientes que interactúen con el sistema.

## Información - Pasos - Pseudocódigo

´´´bash
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
´´´


