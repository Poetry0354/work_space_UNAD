"""Construir un algoritmo que permita calcular el área de un
triángulo, para lo cual debe solicitar la medida de la base y
de la altura y mostrar el área calculada."""

# * Debemos antes definir las varaibles que vamos a utilizar que seria la base y la altura
base = float(input("Ingrese la base del triangulo: "))
altura = float(input("Ingrese la altura del triangulo: "))
respuesta = input("")

# * Ahora procedemos a calcular el area del triangulo
area = (base * altura) / 2

# * FINALMENTE mostramos el resultado
print(f"El area del triangulo es: {area}")




