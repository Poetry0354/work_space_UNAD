"""

Realizar el siguiente ejercicio con la instrucción if..else
mediante condicionales anidados (es decir dentro de la
instrucción else colocar una nueva condición if..else)


Los alumnos del profesor Juan requieren un programa que les indique si
han aprobado el curso. Para esto, usted debe solicitar la nota definitiva
y si dicha nota es menor a 3, muestre un mensaje indicando que no ha
aprobado el curso. Si es igual 3 y menor a 4.5 debe mostrar un mensaje
que informe que el alumno ha aprobado el curso, si la nota es mayor a
4.5 muestre el mensaje que ha probado el curso con un desempeño
superior.


"""

print(
    "Bienvenido al programa de evaluación de notas del curso, vamor a calcular si passaste o no"
)
print("Por favor ingresa tu nota definitiva")

try:
    # Solicita al usuario que ingrese su nota definitiva y la convierte a un número flotante.
    nota_definitiva = float(input("Nota definitiva: "))

    # Verifica la nota y proporciona retroalimentación.
    if nota_definitiva < 3:
        print("No aprobó el curso.")  # Nota menor a 3: No aprobó el curso.
    elif 3 <= nota_definitiva < 4.5:
        print(
            "Aprobó el curso, muchas felicidades."
        )  # Nota entre 3 y 4.5: Aprobó el curso.
    else:
        print(
            "Aprobó el curso con un desempeño superior."
        )  # Nota 4.5 o mayor: Desempeño superior.
except ValueError:
    # Maneja entradas inválidas (valores no numéricos).
    print("Entrada inválida. Por favor, ingrese un número.")
