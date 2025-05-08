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
    argumento: valor_cuenta
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
    
    # Mostrar información de la cuenta y propina
    print("\n" + "="*50)
    print("DETALLE DE LA CUENTA".center(50))
    print("="*50)
    print(f"Valor de la cuenta: ${valor_cuenta:,.2f}")
    print(f"Propina sugerida (15%): ${propina_sugerida:,.2f}")
    print("="*50)

    return valor_cuenta, propina_sugerida

def referido():
    """
    Esta Función se trabaja el caso en el que el cliente, quiera o no, dejar un referido 
    para el restaurante, como recomendación por la atención y servicio.
    argumentos: Toma de Decisiones.
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
            telefono_referido = input("Ingrese el telefono del referido por favor: ").strip()
            try:
                if telefono_referido.isdigit() and len(telefono_referido) == 10:
                    break
                print("Por favor ingrese un Número valido.")
            except ValueError:
                print("Por favor verifica que la información ingresada sea un número")
    
        #Almacenar el referido
        REFERIDOS.append({
            "nombre": nombre_referido,
            "telefono": telefono_referido
        })
        print("¡Referido registrado!")
    else:
        print("No se registró ningun referido..")


def pagar_propina(valor_cuenta, propina_sugerida):
    """
    Se hace toma de decisiones sobre si paga con la propina o no.
    Si paga con la propina, se suma al total de la cuenta, si no, no se actualiza.
    
    argumentos: "valor de cuenta" a actualizar..., propina sugerida a utilisar.
    retorno: Valor actualizado o no, con propina.
    """
    #variable global
    global TOTAL_VENTAS

    while True:
        pagar_con_propina = input("\nEl Cliente pagará con propina? (si/no): ").strip().lower()
        if pagar_con_propina in ['si', 'no']:
            break
        print("Opción no válida. Por favor, ingrese 'si' o 'no'.")

    valor_total_cuenta = valor_cuenta
    pago_propina = False

    if pagar_con_propina == 'si':
        valor_total_cuenta += propina_sugerida
        pago_propina = True
        print(f"El cliente pagará ${propina_sugerida:,.2f} de propina")
    else:
        print("El cliente no pagará la propina sugerida.")

    #Se almacena el valor con la propina
    TOTAL_VENTAS += valor_total_cuenta
    print(f"\nVenta registrada: ${valor_total_cuenta:,.2f}")
    print(f"Total de ventas del día: ${TOTAL_VENTAS:,.2f}")

    return valor_total_cuenta, pago_propina


def factura_electronica():
    """
    Toma de decisiones, si el cliente quiere la factura electronica o no.
    argumentos: Si o no
    retorno: True si quiere factura, False si no
    """

    while True:
        fact_electronica = input("\n¿El Cliente quiere factura electronica? (si/no): ").strip().lower()
        if fact_electronica in ['si', 'no']:
            break
        print("Por favor ingresa una opción válida")

    if fact_electronica == 'si':
        print("Se imprime la factura electrónica")
        return True
    else:
        print("El cliente no quiere factura electrónica")
        return False


def sugerencias():
    """
    Se almacena si el cliente quiere dejar una sugerencia sobre le servicio.
    """
    #Variable global
    global SUGERENCIAS

    while True:
        recomendaciones = input("\n¿El cliente quiere dejar alguna sugerencia? (si/no)")
        if recomendaciones in ['si', 'no']:
            break
        print("Opción no válida. Por favor, ingrese 'si' o 'no'.")

    if recomendaciones == 'si':
        sugerencia = input("\nPor favor, ingresa la sugerencia: ")
        #!Almacenar
        SUGERENCIAS.append({
            "Sugerencias": sugerencia
        })

def mostrar_factura(valor_cuenta, propina_sugerida, pago_propina, tiene_factura_electronica):
    """
    Muestra un formato de factura detallado para el cliente.
    """
    print("\n" + "="*50)
    print("RESTAURANTE DOÑA PANCHA".center(50))
    print("FACTURA DE VENTA".center(50))
    print("="*50)
    
    # Detalles de la cuenta
    print(f"{'Subtotal:':<30} ${valor_cuenta:>15,.2f}")
    if pago_propina:
        print(f"{'Propina (15%):':<30} ${propina_sugerida:>15,.2f}")
        total = valor_cuenta + propina_sugerida
    else:
        print(f"{'Propina:':<30} {'No aplicada':>16}")
        total = valor_cuenta
    
    print("-"*50)
    print(f"{'TOTAL A PAGAR:':<30} ${total:>15,.2f}")
    print("-"*50)
    
    # Información adicional
    print("\nInformación adicional:")
    print(f"Factura electrónica: {'Sí' if tiene_factura_electronica else 'No'}")
    
    print("\n" + "="*50)
    print("¡Gracias por su visita!".center(50))
    print("Vuelva pronto".center(50))
    print("="*50)

def mostrar_resumen_dia():
    """
    Muestra un resumen detallado de las operaciones del día
    """
    print("\n" + "="*60)
    print("RESUMEN DEL DÍA - RESTAURANTE DOÑA PANCHA".center(60))
    print("="*60)
    
    # Información general
    print(f"\nTotal de clientes atendidos: {NUMERO_CLIENTES}")
    print(f"Total de ventas del día: ${TOTAL_VENTAS:,.2f}")
    
    # Mostrar referidos
    print("\nReferidos registrados:")
    if REFERIDOS:
        for ref in REFERIDOS:
            print(f"- {ref['nombre']}: {ref['telefono']}")
    else:
        print("- No se registraron referidos")
    
    # Mostrar sugerencias
    print("\nSugerencias recibidas:")
    if SUGERENCIAS:
        for sug in SUGERENCIAS:
            print(f"- {sug['Sugerencias']}")
    else:
        print("- No se registraron sugerencias")
    
    print("\n" + "="*60)

def main():
    """Función principal que ejecuta el programa"""
    global NUMERO_CLIENTES
    
    while True:
        NUMERO_CLIENTES += 1
        print(f"\nCliente #{NUMERO_CLIENTES}")
        
        # Procesar cliente
        valor_cuenta, propina = valor_propina()
        total, pago_propina = pagar_propina(valor_cuenta, propina)
        referido()
        tiene_factura_electronica = factura_electronica()
        sugerencias()
        
        # Mostrar factura
        mostrar_factura(valor_cuenta, propina, pago_propina, tiene_factura_electronica)
        
        # Preguntar por nuevo cliente
        continuar = input("\n¿Desea registrar un nuevo cliente? (si/no): ").strip().lower()
        if continuar != 'si':
            break
    
    # Mostrar resumen del día
    mostrar_resumen_dia()

if __name__ == "__main__":
    main()

