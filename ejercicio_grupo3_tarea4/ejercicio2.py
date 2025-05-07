"""
*Resolver el siguiente ejercicio con el ciclo while:*
*2. El restaurante “doña Pancha” desea construir un programa
*para calcular el valor de la propina sugerida para n clientes.
*Para cada cliente, el programa debe solicitar el valor de la
*cuenta, calcular el 15% de ese valor y mostrar así el valor de
*la propina sugerida. Al finalizar el registro de cada cliente, se
*debe preguntar si desea registrar un nuevo cliente. El
*programa finaliza cuando el usuario responda que no desea
*registrar un nuevo cliente.

! Requerimientos adicionales (casos de uso)
    * 1. Solicitar un referido al momento de mostrar la factura, es voluntario:
    * Si se selecciona que si, se solicita nombre y telefono. (Almacena)
    * 2. Total de ventas del dia.
    * 3. Si paga con propina o no.
    * 4. Factura electronica o no.
    * 5. Sugerencias (almacenar)
"""

# Mensaje de agradecimiento por el uso del servicio.
print("\n" + "="*50)
print("  Bienvenido a Restaurante Doña Pancha".center(50))
print("  Donde servimos con calor de hogar".center(50))
print("="*50)
print("\nRegistraremos los datos necesarios para el recibo del cliente.".center(50))
print("\n" + "="*50)

# Definir variables globales.
TOTAL_VENTAS = 0
REFERIDOS = []
SUGERENCIAS = []
NUMERO_CLIENTES = 0

# Definir funciones.
def valor_propina():
    """
    Este subprograma/Función se encarga de calcular la propina
    en base del valor ingresado por la caja/mesero.
    parametro: valor_cuenta
    retorno: 0.15 * valor cuenta = propina.
    """
    #variables 
    PROPINA = 0.15

    #Dato de entrada. Validación.
    while True:
        try:
            valor_cuenta = float(input("Por favor ingresa el valor de la cuenta del cliente: "))
            if valor_cuenta > 0:
                break
            print("El valor debe de ser mayor a 0")
        except ValueError:
            print("Por favor ingresa un numero valido")
    #Calculo.
    propina_sugerida = PROPINA * valor_cuenta

    return valor_cuenta, propina_sugerida

def referido():
    """
    Esta Función se trabaja el caso en el que el cliente, quiera o no, dejar un referido 
    para el restaurante, como recomendación por la atención y servicio.
    parametro: Toma de Decisiones.
    retorno: No hay.
    ! Nota: La idea es almacenar el nombre y telefono del referido, si el cliente dice que "Si".
    ! Variable Global...
    """
    #Se declara variable global.
    global REFERIDOS

    while True:
        referido_cliente = input("\nEL cliente, ¿Le gustaria dejar un referido? (si/no): ").strip().lower()
        if referido_cliente in ['si','no']:
            break
        print("Opción no valida. Por favor, ingrese 'Si' o 'No'.")
        
    if referido_cliente == 'si':
        nombre_referido = input("Por favor ingresa el nombre del referido: ")
        while True:
            telefono_referido = ("Ingrese el telefono del referido por favor: ").strip()
            try:
                if telefono_referido.isdigit() and len(telefono_referido) >= 10:
                    break
                print("Por favor ingrese un Número valido.")
            except ValueError:
                print("Por favor verifica que la información ingresada sea un número")
    
        #Almacenar el referido
        REFERIDOS.append({
            "nombre": nombre_referido,
            "telefono": telefono_referido
        })
        print("¡Rferido registrado!")
    else:
        print("No se registró ningun referido..")


    
