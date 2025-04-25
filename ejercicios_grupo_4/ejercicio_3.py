"""Construir un algoritmo que permita calcular el pago de un
trabajador semanalmente, para lo cual usted debe solicitar
la cantidad de horas trabajadas a la semana y el valor de la
hora y mostrar el valor del pago."""

# * Vamos a definir las variables con los datos que se solicitan para posteriormente almacenarlos.

horas_trabajo = float(input("Ingrese la cantidad de horas trabajadas a la semana: "))
valor_hora = float(input("Ingrese el valor de la hora de trabajo: "))

# ! Ahora tenemos que calcular el valor del pago :0

# Para ello, es calcular las horas de trabajo por el valor de hora. Es decir "Ej: 10 hr de trabajo por 50 pesos la hora"

pago = (horas_trabajo * valor_hora)

print(f"Valor a pagar por tus servicios: {pago}") 