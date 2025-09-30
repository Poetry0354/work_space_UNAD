class RecursoNatural:
    def __init__(self, id_recurso, calidad):
        self.__id_recurso = id_recurso
        self.__calidad = calidad

    # Getters y Setters
    def get_id_recurso(self):
        return self.__id_recurso

    def set_id_recurso(self, id_recurso):
        self.__id_recurso = id_recurso

    def get_calidad(self):
        return self.__calidad

    def set_calidad(self, calidad):
        self.__calidad = calidad

    def mostrar_informacion(self):
        return f"Recurso ID: {self.__id_recurso}, Calidad: {self.__calidad}"

# """
# ===================================
# PRUEBAS UNITARIAS
# ===================================
# """
# # 1. Crear una instancia de RecursoNatural
# recurso_test = RecursoNatural("RN001", "Buena")
# print(f"Prueba 1: Creación de objeto - ID: {recurso_test.get_id_recurso()}, Calidad: {recurso_test.get_calidad()}")

# # 2. Probar los setters
# recurso_test.set_id_recurso("RN002")
# recurso_test.set_calidad("Mala")
# print(f"Prueba 2: Setters - ID: {recurso_test.get_id_recurso()}, Calidad: {recurso_test.get_calidad()}")

# # 3. Probar el método mostrar_informacion
# info = recurso_test.mostrar_informacion()
# print(f"Prueba 3: mostrar_informacion - Salida: {info}")
# assert info == "Recurso ID: RN002, Calidad: Mala"
# print("Pruebas para RecursoNatural pasadas con éxito.")