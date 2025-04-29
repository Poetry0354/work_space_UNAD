"""
* Ejercicio 1.
* Resolver el siguiente ejercicio con el ciclo for:
* 1. En el Black Friday la tienda de tecnología "byte" va a realizar
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

# Definición de constantes y diccionarios
DESCUENTOS = {
    'portátil': 0.15,
    'cámara': 0.05,
    'otros': 0.02
}

NUM_VENTAS = 25

# Diccionario para almacenar las ventas
ventas = {
    'portátil': {'cantidad': 0, 'total_sin_descuento': 0, 'total_con_descuento': 0},
    'cámara': {'cantidad': 0, 'total_sin_descuento': 0, 'total_con_descuento': 0},
    'otros': {'cantidad': 0, 'total_sin_descuento': 0, 'total_con_descuento': 0}
}

# Diccionario para detallar los artículos en "otros"
otros_articulos = {}

# Bucle para realizar las ventas
for venta in range(NUM_VENTAS):
    continuar = input("\n¿Desea registrar una venta? (s/n): ").strip().lower()
    if continuar != 's':
        break

    print("\nOpciones de artículos:")
    print("1. Portátil")
    print("2. Cámara")
    print("3. Otros")
    
    opcion = input("Seleccione el número del artículo (1-3): ").strip()
    
    # Validar la opción
    while opcion not in ['1', '2', '3']:
        print("Opción no válida. Intente nuevamente.")
        print("\nOpciones de artículos:")
        print("1. Portátil")
        print("2. Cámara")
        print("3. Otros")
        opcion = input("Seleccione el número del artículo (1-3): ").strip()
    
    # Mapear número a artículo
    mapeo_articulos = {
        '1': 'portátil',
        '2': 'cámara',
        '3': 'otros'
    }
    
    articulo = mapeo_articulos[opcion]
    
    # Si es "otros", pedir detalle
    if opcion == "3":
        detalle_articulo = input("Especifique el tipo de artículo: ").strip().lower()
        otros_articulos[detalle_articulo] = otros_articulos.get(detalle_articulo, 0) + 1
        print(f"Registrado como: otros - {detalle_articulo}")
    
    # Solicitar y validar el valor del artículo
    while True:
        try:
            valor_articulo = float(input("Ingrese el valor del artículo: $"))
            if valor_articulo <= 0:
                print("El valor debe ser mayor que cero.")
                continue
            break
        except ValueError:
            print("Por favor ingrese un valor numérico válido.")

    # Calcular descuento y actualizar ventas
    descuento = valor_articulo * DESCUENTOS[articulo]
    valor_final = valor_articulo - descuento

    # Actualizar el diccionario de ventas
    ventas[articulo]['cantidad'] += 1
    ventas[articulo]['total_sin_descuento'] += valor_articulo
    ventas[articulo]['total_con_descuento'] += valor_final

    # Mostrar el descuento y valor final
    print(f"\nDescuento aplicado: ${descuento:.2f}")
    print(f"Valor final a pagar: ${valor_final:.2f}")

# Mostrar resumen de ventas
print("\nResumen de ventas:")
ventas_realizadas = 0

for articulo, datos in ventas.items():
    if datos["cantidad"] > 0:
        print(f"\nArtículo: {articulo.capitalize()}")
        print(f"Cantidad vendida: {datos['cantidad']}")
        print(f"Total sin descuento: ${datos['total_sin_descuento']:,.2f}")
        print(f"Total con descuento: ${datos['total_con_descuento']:,.2f}")
        ventas_realizadas += datos["cantidad"]

# Si hay artículos en "otros", mostrar el detalle
if otros_articulos:
    print("\nDetalle de artículos en categoría 'otros':")
    for articulo, cantidad in otros_articulos.items():
        print(f"- {articulo.capitalize()}: {cantidad} unidad(es)")

# Calcular totales generales
total_sin_descuento = sum(datos["total_sin_descuento"] for datos in ventas.values())
total_con_descuento = sum(datos["total_con_descuento"] for datos in ventas.values())
total_descuento = total_sin_descuento - total_con_descuento

# Mostrar totales generales
print(f"\nTotal de ventas realizadas: {ventas_realizadas}")
print(f"Total sin descuentos: ${total_sin_descuento:,.2f}")
print(f"Total con descuentos: ${total_con_descuento:,.2f}")
print(f"Total de descuentos aplicados: ${total_descuento:,.2f}")

