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
#* Funciones (programación modular)

def clasificar_diabetes(nivel_glucosa):
    """
    Clasifica el estado de diabetes de un paciente basado en su nivel de glucosa.

    Evalúa el nivel de glucosa proporcionado y lo clasifica en una de las
    siguientes categorías médicas según la Tabla 2 del criterio médico:
    - Hipoglucemia
    - Normal
    - Prediabetes
    - Diabetes

    Args:
        nivel_glucosa (float o int): El nivel de glucosa del paciente en ml.
                                     Se espera un valor numérico.

    Returns:
        str: La clasificación del paciente ("Hipoglucemia", "Normal",
             "Prediabetes", "Diabetes"). Retorna "Nivel inválido" si el
             nivel es negativo (aunque la tabla no lo cubre, es una buena
             práctica).

    """
    # Principio de Algoritmia: Uso de estructuras condicionales (if-elif-else)
    # para seguir el criterio de clasificación de la tabla.

    # Validación básica: aunque la tabla no lo especifica, los niveles negativos
    # no son médicamente coherentes.
    if nivel_glucosa < 0:
        return "Nivel inválido"
    elif nivel_glucosa <= 75:
        return "Hipoglucemia"
    # Nota: El rango 'Normal' es > 75 y menor a 105.
    # Si no es <= 75, entonces es > 75. Solo necesitamos verificar que sea < 105.
    elif nivel_glucosa < 105:
        return "Normal"
    # Nota: El rango 'Prediabetes' es entre 105 y 126.
    # Si no es < 105, entonces es >= 105. Solo necesitamos verificar que sea <= 126.
    elif nivel_glucosa <= 126:
        return "Prediabetes"
    # Nota: El rango 'Diabetes' es > 126.
    # Si no cayó en ninguna de las categorías anteriores, entonces es > 126.
    else:
        return "Diabetes"

#* --- Ejemplo de Uso ---

# Puedes probar la función con diferentes niveles de glucosa:
nivel1 = 60
clasificacion1 = clasificar_diabetes(nivel1)
print(f"Nivel de glucosa: {nivel1} ml -> Criterio: {clasificacion1}") # Salida: Hipoglucemia

nivel2 = 90
clasificacion2 = clasificar_diabetes(nivel2)
print(f"Nivel de glucosa: {nivel2} ml -> Criterio: {clasificacion2}") # Salida: Normal

nivel3 = 105
clasificacion3 = clasificar_diabetes(nivel3)
print(f"Nivel de glucosa: {nivel3} ml -> Criterio: {clasificacion3}") # Salida: Prediabetes (Entra en el rango "Entre 105 y 126")

nivel4 = 120
clasificacion4 = clasificar_diabetes(nivel4)
print(f"Nivel de glucosa: {nivel4} ml -> Criterio: {clasificacion4}") # Salida: Prediabetes

nivel5 = 130
clasificacion5 = clasificar_diabetes(nivel5)
print(f"Nivel de glucosa: {nivel5} ml -> Criterio: {clasificacion5}") # Salida: Diabetes

nivel6 = 75
clasificacion6 = clasificar_diabetes(nivel6)
print(f"Nivel de glucosa: {nivel6} ml -> Criterio: {clasificacion6}") # Salida: Hipoglucemia (Incluye el 75)

nivel7 = 126
clasificacion7 = clasificar_diabetes(nivel7)
print(f"Nivel de glucosa: {nivel7} ml -> Criterio: {clasificacion7}") # Salida: Prediabetes (Incluye el 126)

nivel8 = -10
clasificacion8 = clasificar_diabetes(nivel8)
print(f"Nivel de glucosa: {nivel8} ml -> Criterio: {clasificacion8}") # Salida: Nivel inválido
