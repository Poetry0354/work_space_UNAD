"""
Realizar el siguiente ejercicio con la instrucción if..else
La tienda deportiva “Sports” desea realizar una campaña de fidelización
con sus clientes y dependiendo del día de la semana, creará campañas
para los fanáticos de un deporte; construir un programa en el cual
ingrese el día de la semana y muestre por consola qué artículos del
deporte asociado tendrán descuento:
LUNES FUTBOL
MARTES TENIS
MIÉRCOLES CICLISMO
JUEVES ATLETISMO
VIERNES NATACIÓN
SÁBADO MONTAÑISMO
Nota. Esta tabla muestra los deportes por campañas en días definidos
"""

print("Bienvenido a la tienda de artículos deportivos 'Sports'")
print()
print("Recuerde que tenemos una campaña de fidelización con descuentos especiales")
print()
print(
    "Ven y consulta por nuestros productos, en especial en el día de hoy para tu deporte favorito"
)

print("Por favor ingresa el dia de la semana en mayúsculas")

# Definición de la variable para el día de la semana
dia = input("Ingrese el día de la semana: ")

# Verificar el día de la semana y mostrar el deporte asociado
dias_semana = {
    "LUNES": "FUTBOL",
    "MARTES": "TENIS",
    "MIÉRCOLES": "CICLISMO",
    "JUEVES": "ATLETISMO",
    "VIERNES": "NATACIÓN",
    "SÁBADO": "MONTAÑISMO",
}
# Verificar si el día ingresado es válido
if dia in dias_semana:
    deporte = dias_semana[dia]
    print(f"Hoy es {dia}, y el deporte asociado es {deporte}.")
else:
    print(
        "El día ingresado no es válido. Por favor, ingrese un día de la semana en mayúsculas y verifique tildes."
    )
# Mensaje de despedida
print("Gracias por su visita")
print("Esperamos verte pronto en nuestra tienda")
