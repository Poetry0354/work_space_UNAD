"""

Realizar el siguiente ejercicio con la instrucción if..else
En el Black Friday, la tienda de artículos deportivos “Sports” va a
realizar un descuento del 25% en toda su línea de productos si el valor
es mayor a 200000, le han solicitado a usted que construya un
programa que solicite el valor del producto a comprar, muestre el valor
del descuento si aplica y el valor final a pagar.

"""

print("Bienvenido a la tienda de artículos deportivos 'Sports'")
print(
    "Recuerde que en el Black Friday tenemos un descuento del 25% en productos mayores a 200000 pesos colombianos"
)

# Definición de la tasa de descuento
descuento = 0.25

# Solicitar al usuario el valor del producto
producto = float(
    input(
        "Ingrese el valor del producto a comprar:  (en pesos colombianos, solo números por favor) "
    )
)

# Verificar si el producto aplica para descuento
if producto > 200000:
    # Calcular el descuento y el valor final
    descuento2 = producto * descuento
    valor_final = producto - descuento2
    print(f"El valor del descuento es: {descuento2}")
    print(f"El valor final a pagar es: {valor_final}")
else:
    # Caso en el que no aplica descuento
    print("No aplica descuento")
    print(f"El valor final a pagar es: {producto}")

# Mensaje de despedida
print("Gracias por su compra")
