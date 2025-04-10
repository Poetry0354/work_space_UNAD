"""
Realizar el siguiente ejercicio con la instrucción if..elif..else

El equipo de futbol “los invencibles” está convocando a jóvenes de su
ciudad que quieran ser porteros. Para esto quiere saber cuántos goles en
contra ha tenido el aspirante en los últimos 5 partidos. Acorde a la
siguiente tabla, mostrar el nivel en el cual queda clasificado el aspirante:

CANTIDAD DE GOLES NIVEL
MÁS DE 12 GOLES BAJO
ENTRE 5 Y 12 GOLES MEDIO
ENTRE 0 Y 4 GOLES ALTO

Nota. Esta tabla muestra los rangos de goles para determinar el Nivel de
clasificación.

"""

# Imprime un mensaje de bienvenida al usuario
print("Bienvenido a la convocatoria, estamos muy feciles de tenerte, ;)")
print()

# Explica el propósito del programa y solicita al usuario que ingrese datos
print(
    "Vamos a empezar la convocatoria, por favor digite en numeros la cantidad de goles que a recibido en su contra: "
)

# Captura la cantidad de goles recibidos en los últimos 5 partidos como un número entero
goles_recibidos = int(
    input("Ingrese la cantidad de goles recibidos en los últimos 5 partidos: ")
)

# Evalúa la cantidad de goles recibidos para determinar el nivel del jugador
if goles_recibidos > 12:
    nivel = "BAJO"  # Nivel bajo si los goles recibidos son mayores a 12
elif 5 <= goles_recibidos <= 12:
    nivel = "MEDIO"  # Nivel medio si los goles recibidos están entre 5 y 12
elif 0 <= goles_recibidos <= 4:
    nivel = "ALTO"  # Nivel alto si los goles recibidos están entre 0 y 4
else:
    # Maneja el caso de entrada inválida (número negativo)
    nivel = "INVALIDO"
    print("El número de goles ingresado no es válido. Debe ser un número positivo.")
    exit()  # Termina el programa si la entrada es inválida

# Muestra el nivel del jugador basado en la evaluación anterior
print("El nivel de su juego es el siguiente: ", nivel)
print("Gracias por participar en la convocatoria")
