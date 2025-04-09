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

print("Bienvenido a la convocatoria, estamos muy feciles de tenerte, ;)")
print()

print(
    "Vamos a empezar la convocatoria, por favor digite en numeros la cantidad de goles que a recibido en su contra: "
)

goles_recibidos = int(
    input("Ingrese la cantidad de goles recibidos en los últimos 5 partidos: ")
)

if goles_recibidos > 12:
    nivel = "BAJO"
elif 5 <= goles_recibidos <= 12:
    nivel = "MEDIO"
elif 0 <= goles_recibidos <= 4:
    nivel = "ALTO"
else:
    nivel = "INVALIDO"
    print("El número de goles ingresado no es válido. Debe ser un número positivo.")
    exit()

print("El nivel de su juego es el siguiente: ", nivel)
print("Gracias por participar en la convocatoria")
