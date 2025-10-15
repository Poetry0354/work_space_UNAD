class Comunidad:
    def __init__(self, id_agricultor, nombre, ubicacion, parcelas=None):
        self.__id_agricultor = id_agricultor
        self.__nombre = nombre
        self.__ubicacion = ubicacion
        self.__parcelas = parcelas if parcelas is not None else []  # Lista de objetos Suelo

    # Getters y Setters
    def get_id_agricultor(self):
        return self.__id_agricultor

    def set_id_agricultor(self, id_agricultor):
        self.__id_agricultor = id_agricultor

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_ubicacion(self):
        return self.__ubicacion

    def set_ubicacion(self, ubicacion):
        self.__ubicacion = ubicacion

    def get_parcelas(self):
        return self.__parcelas

    def set_parcelas(self, parcelas):
        self.__parcelas = parcelas

    # Métodos de la clase
    def consultar_datos(self):
        return (f"Agricultor {self.__nombre} (ID: {self.__id_agricultor}) "
                f"Ubicación: {self.__ubicacion}, Parcelas: {len(self.__parcelas)}")

    def generar_reporte(self):
        reporte = f"📋 Reporte de la comunidad {self.__nombre}\n"
        for parcela in self.__parcelas:
            reporte += f" - {parcela.analizar_suelo()}\n"
        return reporte

    def tomar_decision(self):
        """Ejemplo simple de toma de decisiones"""
        if any(p.get_ph() < 5.5 for p in self.__parcelas):
            return "⚠️ Se recomienda aplicar encalado en algunas parcelas."
        return "✅ Las parcelas están en condiciones óptimas."

# """
# ===================================
# PRUEBAS UNITARIAS
# ===================================
# """
# # Mock para Suelo
# class MockSuelo:
#     def __init__(self, ph, analisis="Análisis de prueba"):
#         self._ph = ph
#         self._analisis = analisis
#     def get_ph(self):
#         return self._ph
#     def analizar_suelo(self):
#         return self._analisis

# # 1. Crear una instancia de Comunidad
# parcela1 = MockSuelo(6.5)
# parcela2 = MockSuelo(5.0)
# comunidad_test = Comunidad("AGR01", "Comunidad Test", "Zona Norte", [parcela1, parcela2])
# print(f"Prueba 1: Creación - Nombre: {comunidad_test.get_nombre()}, Nro. Parcelas: {len(comunidad_test.get_parcelas())}")

# # 2. Probar los setters
# comunidad_test.set_nombre("Comunidad Avanzada")
# comunidad_test.set_parcelas([parcela1])
# print(f"Prueba 2: Setters - Nombre: {comunidad_test.get_nombre()}, Nro. Parcelas: {len(comunidad_test.get_parcelas())}")

# # 3. Probar consultar_datos
# datos = comunidad_test.consultar_datos()
# print(f"Prueba 3: consultar_datos - Salida: {datos}")
# assert "Parcelas: 1" in datos

# # 4. Probar generar_reporte
# comunidad_test.set_parcelas([parcela1, parcela2])
# reporte = comunidad_test.generar_reporte()
# print(f"Prueba 4: generar_reporte - Salida: {reporte.strip()}")
# assert reporte.count("Análisis de prueba") == 2

# # 5. Probar tomar_decision
# # Caso 1: Se recomienda acción
# decision1 = comunidad_test.tomar_decision()
# print(f"Prueba 5.1: tomar_decision (acción requerida) - Salida: {decision1}")
# assert "recomienda aplicar encalado" in decision1

# # Caso 2: Condiciones óptimas
# comunidad_test.set_parcelas([parcela1])
# decision2 = comunidad_test.tomar_decision()
# print(f"Prueba 5.2: tomar_decision (óptimas) - Salida: {decision2}")
# assert "condiciones óptimas" in decision2

# print("Pruebas para Comunidad pasadas con éxito.")