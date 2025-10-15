from recurso_natural import RecursoNatural

class FuentesAgua(RecursoNatural):
    def __init__(self, id_recurso, calidad, id_fuente, tipo):
        super().__init__(id_recurso, calidad)  # Herencia desde RecursoNatural
        self.__id_fuente = id_fuente
        self.__tipo = tipo  # Ej: río, pozo, embalse

    # Getters y Setters
    def get_id_fuente(self):
        return self.__id_fuente

    def set_id_fuente(self, id_fuente):
        self.__id_fuente = id_fuente

    def get_tipo(self):
        return self.__tipo

    def set_tipo(self, tipo):
        self.__tipo = tipo

    # Métodos de la clase
    def analizar_calidad(self):
        """Devuelve un mensaje con la calidad del agua"""
        return f"Fuente {self.__id_fuente} ({self.__tipo}) tiene calidad: {self.get_calidad()}"

    def es_apta_para_riego(self):
        """Ejemplo simplificado de validación de calidad"""
        if self.get_calidad().lower() in ["excelente", "buena"]:
            return f"✅ El agua de la fuente {self.__id_fuente} es apta para riego."
        else:
            return f"⚠️ El agua de la fuente {self.__id_fuente} NO es apta para riego."

# """
# ===================================
# PRUEBAS UNITARIAS
# ===================================
# """
# from recurso_natural import RecursoNatural

# # 1. Crear una instancia de FuentesAgua
# agua_test = FuentesAgua("A001", "buena", "F01", "pozo")
# print(f"Prueba 1: Creación - ID Fuente: {agua_test.get_id_fuente()}, Tipo: {agua_test.get_tipo()}")
# # Probar herencia
# print(f"Prueba 1.1: Herencia - Calidad: {agua_test.get_calidad()}")

# # 2. Probar los setters
# agua_test.set_tipo("río")
# agua_test.set_calidad("regular")
# print(f"Prueba 2: Setters - Tipo: {agua_test.get_tipo()}, Calidad: {agua_test.get_calidad()}")

# # 3. Probar analizar_calidad
# analisis = agua_test.analizar_calidad()
# print(f"Prueba 3: analizar_calidad - Salida: {analisis}")
# assert "calidad: regular" in analisis

# # 4. Probar es_apta_para_riego
# # Caso 1: No apta
# aptitud1 = agua_test.es_apta_para_riego()
# print(f"Prueba 4.1: es_apta_para_riego (no apta) - Salida: {aptitud1}")
# assert "NO es apta" in aptitud1

# # Caso 2: Apta
# agua_test.set_calidad("excelente")
# aptitud2 = agua_test.es_apta_para_riego()
# print(f"Prueba 4.2: es_apta_para_riego (apta) - Salida: {aptitud2}")
# assert "es apta" in aptitud2

# print("Pruebas para FuentesAgua pasadas con éxito.")