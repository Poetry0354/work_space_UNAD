"""
*Resolver el siguiente ejercicio usando una función:*
4. Construir una función que permita verificar acorde a los niveles
de azúcar de un paciente si el paciente es diabético. Para esto,
la función debe recibir como parámetro el nivel de glucosa y con
ese nivel realizar la clasificación del paciente acorde a esta
tabla:
Tabla 2
Nivel de glucosa de acuerdo con el criterio médico de
valoración.
Nivel de glucosa Criterio médico
Menor o igual a 75 ml Hipoglucemia
Mayor a 75 ml y menor a 105 ml Normal
Entre 195 y 126 ml Prediabetes
Mayor a 126 Diabetes
Nota. Esta tabla muestra el Nivel de glucosa para la valoración del
Criterio médico.
"""

def solicitar_nivel_glucosa():
    """
    Solicita y valida el nivel de glucosa ingresado por el usuario.

    Returns:
        float: El nivel de glucosa validado
    """
    while True:
        try:
            nivel = float(input("Por favor ingrese el nivel de glucosa (ml): "))
            if nivel >= 0:
                return nivel
            print("El nivel de glucosa no puede ser negativo.")
        except ValueError:
            print("Por favor ingrese un número válido.")

def clasificar_diabetes(nivel_glucosa):
    """
    Clasifica el estado de diabetes de un paciente basado en su nivel de glucosa.

    Args:
        nivel_glucosa (float o int): El nivel de glucosa del paciente en ml.

    Returns:
        str: La clasificación del paciente
    """
    if nivel_glucosa < 0:
        return "Nivel inválido"
    elif nivel_glucosa <= 75:
        return "Hipoglucemia"
    elif nivel_glucosa < 105:
        return "Normal"
    elif nivel_glucosa <= 126:
        return "Prediabetes"
    else:
        return "Diabetes"

def mostrar_resultado(nivel_glucosa, clasificacion):
    """
    Muestra el resultado de la clasificación de manera formateada.

    Args:
        nivel_glucosa (float): El nivel de glucosa del paciente
        clasificacion (str): La clasificación obtenida
    """
    print("\n" + "="*50)
    print("  Clasificación de Nivel de Glucosa".center(50))
    print("="*50)
    print(f"\nNivel de glucosa: {nivel_glucosa:.1f} ml")
    print(f"Criterio médico: {clasificacion}")
    print("="*50)

def main():
    """
    Función principal que controla el flujo del programa.
    """
    print("\n" + "="*50)
    print("  Sistema de Clasificación de Diabetes".center(50))
    print("  Basado en Niveles de Glucosa".center(50))
    print("="*50)

    while True:
        # Solicitar y validar el nivel de glucosa
        nivel_glucosa = solicitar_nivel_glucosa()
        
        # Clasificar el nivel de glucosa
        clasificacion = clasificar_diabetes(nivel_glucosa)
        
        # Mostrar el resultado
        mostrar_resultado(nivel_glucosa, clasificacion)
        
        # Preguntar si desea continuar
        continuar = input("\n¿Desea clasificar otro paciente? (si/no): ").lower().strip()
        if continuar != 'si':
            break

    print("\n¡Gracias por usar el sistema de clasificación!")

if __name__ == "__main__":
    main()