"""Martha desea calcular el total y el promedio de gastos de los
últimos 5 meses, para lo cual ha solicitado su ayuda en la
construcción de un algoritmo que solicite el valor de los
gastos de cada mes, sume el valor de esos gastos, calcule el
promedio y muestre estos resultados."""

# * Debemos antes definir las varaibles que vamos a utilizar que seria los gastos de cada mes
gasto_enero = float(input("Ingrese el gasto de enero: "))
gasto_febrero = float(input("Ingrese el gasto de febrero: "))
gasto_marzo = float(input("Ingrese el gasto de marzo: "))
gasto_abril = float(input("Ingrese el gasto de abril: "))
gasto_mayo = float(input("Ingrese el gasto de mayo: "))

# ? Podemos hacer uso de una lista para almacenar los gastos de cada mes

gastos = [gasto_enero, gasto_febrero, gasto_marzo, gasto_abril, gasto_mayo]

# ! Ahora si podemos hacer uso de la funcion sum() para sumar los gastos, que es sumar en otras palabras.

total_gastos = sum(gastos)

# ? Ahora nos preguntamos ¿Como calculamos el promedio de los gastos? 
# * RTA: Para calcular el promedio de los gastos, debemos sumar todos los gastos y dividirlos entre la cantidad de gastos que tenemos.
# * En este caso tenemos 5 gastos, entonces dividimos la suma de los gastos entre 5

promedio_gastos = total_gastos / 5

# * FINALMENTE mostramos el resultado
print(f"El total de los gastos es: {total_gastos}")
print(f"El promedio de los gastos es: {promedio_gastos}")
print("Que tenga un buen dia señora Martha")





