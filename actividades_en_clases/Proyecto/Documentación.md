# Grupo 2

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

**Solución:** Integrar y analizar las bases de datos (clientes, productos, ventas, detalle_ventas) para obtener tendencias como  productos más vendido o productos que más contribuyen por categoría, usando consultas o herramientas como Power BI.

## Estructura - Tipo - Escala (de la BD)

**Estructura:** base de datos estructurada (excel) y relacional. Se agregan campos como: "Frecuencia_cliente", "Producto_popular". 

**Tipo:** OLAP, ya que se usaría para el análisis de datos a partir de históricos y registros. 

**Escala:** se espera una escala mediana, ya que esta podría variar según la cantidad de ventas y clientes que interactúen con el sistema.

## Información - Pasos - Pseudocódigo

<img width="352" height="713" alt="image" src="https://github.com/user-attachments/assets/ecc0df84-485d-4c45-87d4-0649415f3f75" />

**Pasos**
1. Cargar los datos de las BD
2. Guardar en total_ventas los 5 productos más vendidos
3. Guardar en total_importe el dinero total vendido por producto (precio unitario x cantidad vendido)
4. Etiquetar cada producto como "Producto popular" o "Producto menos popular" si el producto está dentro de total_ventas.
5. Guardar en total_generado_cat la cantidad de dinero total generado por cada categoría
6. Guardar en porcentaje_participación la división de total_importe/total_generado_cat para cada producto y su categoria respectivamente
7. Etiquetar cada producto como "Producto más relevante" o "Producto menos relevante" si el producto tiene un porcentaje de participación superior al 80%

```bash
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
  porcentaje_participacion ← calcular_porcentaje_participacion_producto() # Por cada producto y su categoria: total_importe / total_generado_cat

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
```
## Sugerencias de Copilot

Se siguió el paso a paso del archivo python, con el fin de aligerar el trabajo a realizar. 