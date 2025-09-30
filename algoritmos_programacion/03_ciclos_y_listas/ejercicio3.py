"""
Ciclo White.
3. La empresa Netflix desea saber en una encuesta a 15 personas
para saber cuántas horas promedio invierten en mirar sus
contenidos los domingos. Para esto, usted debe construir un
programa que solicite la cantidad de horas que invierte cada
persona encuestada el domingo, almacenando ese dato en una
lista y que muestre el promedio de horas de todo el grupo.

! Plus: Validación de Entrada de datos o Identificar tiempo maximo y minimo.

"""
#Variables Globales.
ENCUESTADOS = 15
PROMEDIO_HORAS = 0
HORAS = []

#* Funciones (programación modular)

def solicitar_datos_ingresar():
    """
    Solicita y valida la cantidad de horas de Netflix vistas por una persona.

    Pide al usuario que ingrese el número de horas que una persona vio Netflix
    el domingo. Valida que la entrada sea un número no negativo.
    Agrega el dato válido a la lista global HORAS.
    Continúa pidiendo la entrada hasta que se ingrese un valor válido.

    Efecto secundario: Modifica la lista global HORAS.
    """
    #Variable global
    global HORAS

    while True:
        try:
            horas_ingresadas = float(input("Por favor ingresa las horas del Domingo: "))
            if horas_ingresadas >= 0:
                break
            else: 
                print("ERROR: Las horas no pueden ser negativas")
        except ValueError:
            print("Valor invalido por favor, ingresa nuevamente")

    #!Almacenamiento de datos.
    HORAS.append(horas_ingresadas)

    print(f"Has ingresado: {horas_ingresadas}. Dato valido")

def promedio(HORAS):
    """
    Calcula el promedio de horas de visualización de Netflix.

    Recibe una lista que contiene las horas de visualización de Netflix
    por parte de varias personas y calcula el promedio de esas horas.
    Suma todos los valores en la lista y los divide por la cantidad de elementos
    para obtener el promedio.

    Args:
        HORAS (list): Una lista de números (generalmente float o int) donde cada
        elemento representa las horas de Netflix vistas por una persona.

    Returns:
        float: El promedio calculado de las horas. Retorna 0.0 si la lista está vacía
        para evitar una división por cero.

    """

    # Verificamos si la lista está vacía
    if not HORAS:
        return 0.0
    
    # Calculamos la suma de todas las horas
    suma_horas = sum(HORAS)
    
    # Calculamos el promedio dividiendo la suma entre la cantidad de elementos
    promedio_horas = suma_horas / len(HORAS)
    
    return promedio_horas

def representacion_datos(promedio_horas):
    """
    Representación de datos.

    Se recibe como parametro el promedio de las horas para luego imprimir por pantalla
    al final del flujo.

    Args: 
        promedio_horas(retorno): Es el resultado del calculo de la función promedio.
    """
    print("\n" + "="*50)
    print("  Resultado de Encuestas".center(50))
    print("  Tiempo de entretenimiento Netflix".center(50))
    print("="*50)
    
    print(f"\nEste es el promedio de las horas de entretenimiento: {promedio_horas}")

def main(ENCUESTADOS): 
    """
    Función principal que orquesta la encuesta de horas de Netflix.

    Controla el flujo del programa para solicitar datos de un número
    específico de encuestados, calcula el promedio y muestra los resultados.

    Args:
        ENCUESTADOS (int): El número total de personas a encuestar.
    """
    print("\n" + "="*50)
    print("  Encuestas Netflix - HORAS VISTAS".center(50))
    print("="*50)

    
    print(f"\nSe solicitará la cantidad de horas para: {ENCUESTADOS} personas")

    # --- CONTROL DEL FLUJO ---

    # Bucle para solicitar datos a cada encuestado
    print("\n--- Inicio de la recopilación de datos ---")
    for i in range(ENCUESTADOS):
        # Opcional: Mostrar a qué persona se le está pidiendo el dato
        print(f"\n--- Ingresando datos para la Persona {i + 1} de {ENCUESTADOS} ---")

        # Llama a la función que pide, valida y guarda el dato en la lista global HORAS
        solicitar_datos_ingresar()

    print("\n--- Recopilación de datos finalizada ---")

    # Calcular el promedio una vez que se tienen todos los datos
    # Pasamos la lista global HORAS a la función promedio
    promedio_final = promedio(HORAS)

    # Mostrar los resultados llamando a la función de representación
    # Pasamos el promedio calculado (promedio_final) a representacion_datos
    representacion_datos(promedio_final)


if __name__ == "__main__":
    main(ENCUESTADOS) 