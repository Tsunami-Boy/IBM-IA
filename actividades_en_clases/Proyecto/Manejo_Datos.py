import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# pip install openpyxl # para archivps Excel .xlsx modernos

def graficar_boxplot(columna, df):
    sns.boxplot(y=df[columna])
    plt.title(f'Distribución de {columna}')
    plt.savefig(f'Graficos/boxplot_{columna}.png', dpi=300, bbox_inches='tight')  # 🔹 guarda el gráfico
    plt.close()

def graficar_scatter(x_col, y_col, df):
    plt.figure(figsize=(8,6))
    sns.scatterplot(x=df[x_col], y=df[y_col])
    plt.title(f'Dispersión de {y_col} vs {x_col}')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.savefig(f'Graficos/scatter_{y_col}_vs_{x_col}.png', dpi=300, bbox_inches='tight')  # 🔹 guarda el gráfico
    plt.close()

def graficar_barras(columna, df):
    plt.figure(figsize=(10,6))
    suma_por_producto = (df.groupby('nombre_producto')[columna].sum().sort_values(ascending=False).head(10))
    suma_por_producto.plot(kind='bar')
    plt.title(f'Top productos por {columna}')
    plt.xlabel('Producto')
    plt.ylabel(columna)
    plt.savefig(f'Graficos/barras_{columna}.png', dpi=300, bbox_inches='tight')  # 🔹 guarda el gráfico
    plt.close()

print("\n --- Manejo de datos desde archivos Excel --- \n")

df_clientes = pd.read_excel('DB/Clientes.xlsx')
df_ventas = pd.read_excel('DB/Ventas.xlsx')
df_productos = pd.read_excel('DB/Productos.xlsx')
df_detalles_ventas = pd.read_excel('DB/Detalle_ventas.xlsx')

# Información de los DataFrames

print("A continuación se muestra la información del DataFrame de clientes: \n")
print(df_clientes.info())

print("\nA continuación se muestra la información del DataFrame de detalles de ventas: \n")
print(df_detalles_ventas.info())

print("\nA continuación se muestra la información del DataFrame de productos: \n")
print(df_productos.info())

print("\nA continuación se muestra la información del DataFrame de ventas: \n")
print(df_ventas.info())

# Mostrar primeras n filas de cada DataFrame como ejemplo

n = 4  # número de filas a mostrar
print(f"\nPrimeras {n} filas del DataFrame de clientes:\n", df_clientes.head(n))
print(f"\nPrimeras {n} filas del DataFrame de detalles de ventas:\n", df_detalles_ventas.head(n))
print(f"\nPrimeras {n} filas del DataFrame de productos:\n", df_productos.head(n))
print(f"\nPrimeras {n} filas del DataFrame de ventas:\n", df_ventas.head(n))

# Valores nulos o faltantes en cada DataFrame

print("\nValores nulos en el DataFrame de clientes:\n", df_clientes.isnull().sum())
print("\nValores nulos en el DataFrame de detalles de ventas:\n", df_detalles_ventas.isnull().sum())
print("\nValores nulos en el DataFrame de productos:\n", df_productos.isnull().sum())
print("\nValores nulos en el DataFrame de ventas:\n", df_ventas.isnull().sum())

# Filas duplicadas en cada DataFrame

print("\nFilas duplicadas en el DataFrame de clientes según email:", df_clientes.duplicated(subset="email").sum())
print("Filas duplicadas en el DataFrame de detalles de ventas:", df_detalles_ventas.duplicated().sum())
print("Filas duplicadas en el DataFrame de productos según su nombre:", df_productos.duplicated(subset="nombre_producto").sum())
print("Filas duplicadas en el DataFrame de ventas:", df_ventas.duplicated().sum())

# Manejo de espacios en las columnas de texto

df_clientes['nombre_cliente'] = df_clientes['nombre_cliente'].str.strip()
df_clientes['email'] = df_clientes['email'].str.strip()
df_clientes['ciudad'] = df_clientes['ciudad'].str.strip()

df_detalles_ventas['nombre_producto'] = df_detalles_ventas['nombre_producto'].str.strip()

df_productos['nombre_producto'] = df_productos['nombre_producto'].str.strip()
df_productos['categoria'] = df_productos['categoria'].str.strip()

df_ventas['nombre_cliente'] = df_ventas['nombre_cliente'].str.strip()
df_ventas['email'] = df_ventas['email'].str.strip()
df_ventas['medio_pago'] = df_ventas['medio_pago'].str.strip()

# Estadísticas descriptivas básicas

print("\nEstadísticas descriptivas del DataFrame de clientes:\n", df_clientes.describe(include='all'))
print("\nEstadísticas descriptivas del DataFrame de detalles de ventas:\n", df_detalles_ventas.describe(include='all'))
print("\nEstadísticas descriptivas del DataFrame de productos:\n", df_productos.describe(include='all'))
print("\nEstadísticas descriptivas del DataFrame de ventas:\n", df_ventas.describe(include='all'))

# Análisis para distribución de datos numéricos

print(f"\nAnálisis de distribución para la columna 'cantidad' en el DataFrame de detalles de ventas:\nPromedio: {df_detalles_ventas['cantidad'].mean()}\nMediana: {df_detalles_ventas['cantidad'].median()}\nModa: {df_detalles_ventas['cantidad'].mode().iloc[0]}")
print(f"\nAnálisis de distribución para la columna 'precio_unitario' en el DataFrame de detalles de ventas:\nPromedio: {df_detalles_ventas['precio_unitario'].mean()}\nMediana: {df_detalles_ventas['precio_unitario'].median()}\nModa: {df_detalles_ventas['precio_unitario'].mode().iloc[0]}")
print(f"\nAnálisis de distribución para la columna 'importe' en el DataFrame de detalles de ventas:\nPromedio: {df_detalles_ventas['importe'].mean()}\nMediana: {df_detalles_ventas['importe'].median()}\nModa: {df_detalles_ventas['importe'].mode().iloc[0]}\n")

# Rango
print("Rango de los datos numéricos en el DataFrame de detalles de ventas:")
print(f"Rango de 'cantidad': {df_detalles_ventas['cantidad'].max() - df_detalles_ventas['cantidad'].min()}")
print(f"Rango de 'precio_unitario': {df_detalles_ventas['precio_unitario'].max() - df_detalles_ventas['precio_unitario'].min()}")
print(f"Rango de 'importe': {df_detalles_ventas['importe'].max() - df_detalles_ventas['importe'].min()}\n")

# Correlaciones

print("Matriz de correlación del DataFrame de detalles de ventas:\n", df_detalles_ventas[['importe','cantidad','precio_unitario']].corr())

# Outliers usando el método del rango intercuartílico (IQR)

Q1_importe = df_detalles_ventas['importe'].quantile(0.25)
Q3_importe = df_detalles_ventas['importe'].quantile(0.75)
Q1_cantidad = df_detalles_ventas['cantidad'].quantile(0.25)
Q3_cantidad = df_detalles_ventas['cantidad'].quantile(0.75)
Q1_precio = df_detalles_ventas['precio_unitario'].quantile(0.25)
Q3_precio = df_detalles_ventas['precio_unitario'].quantile(0.75)

IQR_importe = Q3_importe - Q1_importe
IQR_cantidad = Q3_cantidad - Q1_cantidad
IQR_precio = Q3_precio - Q1_precio

limite_inferior_importe = Q1_importe - 1.5 * IQR_importe
limite_superior_importe = Q3_importe + 1.5 * IQR_importe
limite_inferior_cantidad = Q1_cantidad - 1.5 * IQR_cantidad
limite_superior_cantidad = Q3_cantidad + 1.5 * IQR_cantidad
limite_inferior_precio = Q1_precio - 1.5 * IQR_precio
limite_superior_precio = Q3_precio + 1.5 * IQR_precio

outliers_importe = df_detalles_ventas[(df_detalles_ventas['importe'] < limite_inferior_importe) | (df_detalles_ventas['importe'] > limite_superior_importe)]
outliers_cantidad = df_detalles_ventas[(df_detalles_ventas['cantidad'] < limite_inferior_cantidad) | (df_detalles_ventas['cantidad'] > limite_superior_cantidad)]
outliers_precio = df_detalles_ventas[(df_detalles_ventas['precio_unitario'] < limite_inferior_precio) | (df_detalles_ventas['precio_unitario'] > limite_superior_precio)]

print("\nNúmero de outliers detectados usando el método IQR:")
print(f"Número de outliers en 'importe': {outliers_importe.shape[0]}")
print(f"Número de outliers en 'cantidad': {outliers_cantidad.shape[0]}")
print(f"Número de outliers en 'precio_unitario': {outliers_precio.shape[0]}\n")

print(f"Filas de outliers en 'importe':\n{outliers_importe}\n")

# Gráfico

graficar_boxplot('importe',df_detalles_ventas)
graficar_boxplot('cantidad',df_detalles_ventas)
graficar_boxplot('precio_unitario',df_detalles_ventas)

graficar_scatter('cantidad','importe',df_detalles_ventas)
graficar_scatter('precio_unitario','importe',df_detalles_ventas)
graficar_scatter('precio_unitario','cantidad',df_detalles_ventas)

graficar_barras('importe',df_detalles_ventas)
graficar_barras('cantidad',df_detalles_ventas)