"""
* Ejercicio 1.
* Resolver el siguiente ejercicio con el ciclo for:
* 1. En el Black Friday la tienda de tecnología “byte” va a realizar
* un descuento del 15% en portátiles, del 5% en cámaras y del
* 2% en el resto de artículos. Usted debe construir un programa
* que permita calcular para 25 ventas el valor del descuento,
* solicitando al usuario el tipo de artículo a comprar: portátil,
* cámara, otros, solicite el valor del artículo y muestre el
* descuento y valor final a pagar. Al final del ciclo se debe mostrar
* la cantidad de artículos vendidos en la línea portátil, la cantidad
* de artículos vendidos en la línea de cámaras y la cantidad de
* artículos de las otras líneas.
"""

# Definición de constantes
DESCUENTO_PORTATIL = 0.15
DESCUENTO_CAMARA = 0.05
DESCUENTO_OTROS = 0.02
NUM_VENTAS = 25
# Inicialización de contadores
contador_portatiles = 0
contador_camaras = 0
contador_otros = 0

# Inicializacion de variables "ventas en las lineas"
ventas_portatiles = 0
ventas_camaras = 0
ventas_otros = 0

# Inicializacion de varaibles para el valor con el descuento
ventas_portatiles_desc = 0  # Valor con descuento
ventas_camaras_desc = 0     # Valor con descuento
ventas_otros_desc = 0       # Valor con descuento


# Bucle para realizar las ventas
for venta in range(NUM_VENTAS):
    # Preguntar si desea continuar
    continuar = input("¿Desea registrar una venta? (s/n): ").strip().lower()
    if continuar != 's':
        break 
    # Solicitar el articulo a comprar
    articulo = input("Ingrese el tipo de artículo a comprar (portátil, cámara, otros): ").strip().lower()
    print("Elegiste:", articulo)

    # Validar el tipo de artículo
    while articulo not in ["portátil", "cámara", "otros"]:
        print("Tipo de artículo no válido. Intente nuevamente. Tildes se consideran.")
        articulo = input("Ingrese el tipo de artículo a comprar (portátil, cámara, otros): ").strip().lower()

    
    # Solicitar el valor del artículo
    valor_articulo = float(input("Ingrese el valor del artículo: "))

    # Validar el valor del artículo
    while valor_articulo <= 0:
        print("El valor del artículo debe ser mayor que cero. Intente nuevamente.")
        valor_articulo = float(input("Ingrese el valor del artículo: "))


    # Calcular el descuento y el valor final a pagar
    if articulo == "portátil":
        descuento = valor_articulo * DESCUENTO_PORTATIL
        valor_final = valor_articulo - descuento
        contador_portatiles += 1
        ventas_portatiles += valor_articulo
        ventas_portatiles_desc += valor_final
    elif articulo == "cámara":
        descuento = valor_articulo * DESCUENTO_CAMARA
        valor_final = valor_articulo - descuento
        contador_camaras += 1
        ventas_camaras += valor_articulo
        ventas_camaras_desc += valor_final
    else:
        descuento = valor_articulo * DESCUENTO_OTROS
        valor_final = valor_articulo - descuento
        contador_otros += 1
        ventas_otros += valor_articulo
        ventas_otros_desc += valor_final

    # Mostrar el descuento y el valor final a pagar
    print(f"Descuento: {descuento:.2f}")
    print(f"Valor final a pagar: {valor_final:.2f}")


# Mostrar la cantidad de artículos vendidos en cada línea
print(f"\nSe registraron {venta + 1 if continuar == 's' else venta} ventas en total.")
print("\nResumen de ventas por cantidad:")
print(f"Cantidad de portátiles vendidos: {contador_portatiles}")
print(f"Cantidad de cámaras vendidas: {contador_camaras}")
print(f"Cantidad de otros artículos vendidos: {contador_otros}")

# Mostrar el total de ventas por línea (precio original)
print("\nTotal de ventas (sin descuento):")
print(f"Total ventas portátiles: ${ventas_portatiles:,.2f}")
print(f"Total ventas cámaras: ${ventas_camaras:,.2f}")
print(f"Total ventas otros artículos: ${ventas_otros:,.2f}")

# Mostrar el total de ventas por línea (con descuento)
print("\nTotal de ventas (con descuento aplicado):")
print(f"Total ventas portátiles: ${ventas_portatiles_desc:,.2f}")
print(f"Total ventas cámaras: ${ventas_camaras_desc:,.2f}")
print(f"Total ventas otros artículos: ${ventas_otros_desc:,.2f}")

# Mostrar resumen final de ventas
total_ventas_original = ventas_portatiles + ventas_camaras + ventas_otros
total_ventas_descuento = ventas_portatiles_desc + ventas_camaras_desc + ventas_otros_desc
total_descuentos = total_ventas_original - total_ventas_descuento

print("\nResumen final:")
print(f"Total de ventas sin descuento: ${total_ventas_original:,.2f}")
print(f"Total de ventas con descuento: ${total_ventas_descuento:,.2f}")
print(f"Total de descuentos aplicados: ${total_descuentos:,.2f}")

