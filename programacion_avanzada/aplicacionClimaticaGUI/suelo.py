from recurso_natural import RecursoNatural

class Suelo(RecursoNatural):
    def __init__(self, id_recurso, calidad, id_parcela, ph, nutrientes, clasificacion):
        super().__init__(id_recurso, calidad)  # Hereda de RecursoNatural
        self.__id_parcela = id_parcela
        self.__ph = ph
        self.__nutrientes = nutrientes
        self.__clasificacion = clasificacion

    # Getters y Setters
    def get_id_parcela(self):
        return self.__id_parcela

    def set_id_parcela(self, id_parcela):
        self.__id_parcela = id_parcela

    def get_ph(self):
        return self.__ph

    def set_ph(self, ph):
        self.__ph = ph

    def get_nutrientes(self):
        return self.__nutrientes

    def set_nutrientes(self, nutrientes):
        self.__nutrientes = nutrientes

    def get_clasificacion(self):
        return self.__clasificacion

    def set_clasificacion(self, clasificacion):
        self.__clasificacion = clasificacion

    # Métodos de la clase
    def analizar_suelo(self):
        return (f"Parcela {self.__id_parcela}: pH={self.__ph}, "
                f"Nutrientes={self.__nutrientes}, Clasificación={self.__clasificacion}, "
                f"Calidad={self.get_calidad()}")

    def es_apto_para_cultivo(self, cultivo):
        """Ejemplo simple de validación"""
        if self.__ph >= 5.5 and self.__ph <= 7.5:
            return f"✅ La parcela {self.__id_parcela} es apta para {cultivo}."
        else:
            return f"⚠️ La parcela {self.__id_parcela} NO es apta para {cultivo}."

# """
# ===================================
# PRUEBAS UNITARIAS
# ===================================
# """
# from recurso_natural import RecursoNatural

# # 1. Crear una instancia de Suelo
# suelo_test = Suelo("S001", "Fértil", "P01", 6.8, "Altos en NPK", "Franco")
# print(f"Prueba 1: Creación - ID Parcela: {suelo_test.get_id_parcela()}, pH: {suelo_test.get_ph()}")
# # Probar herencia
# print(f"Prueba 1.1: Herencia - Calidad: {suelo_test.get_calidad()}")

# # 2. Probar los setters
# suelo_test.set_ph(5.2)
# suelo_test.set_nutrientes("Bajos en N")
# print(f"Prueba 2: Setters - pH: {suelo_test.get_ph()}, Nutrientes: {suelo_test.get_nutrientes()}")

# # 3. Probar analizar_suelo
# analisis = suelo_test.analizar_suelo()
# print(f"Prueba 3: analizar_suelo - Salida: {analisis}")
# assert "pH=5.2" in analisis
# assert "Calidad=Fértil" in analisis

# # 4. Probar es_apto_para_cultivo
# # Caso 1: No apto
# aptitud1 = suelo_test.es_apto_para_cultivo("Maíz")
# print(f"Prueba 4.1: es_apto_para_cultivo (no apto) - Salida: {aptitud1}")
# assert "NO es apta" in aptitud1

# # Caso 2: Apto
# suelo_test.set_ph(6.0)
# aptitud2 = suelo_test.es_apto_para_cultivo("Fresas")
# print(f"Prueba 4.2: es_apto_para_cultivo (apto) - Salida: {aptitud2}")
# assert "es apta" in aptitud2

# print("Pruebas para Suelo pasadas con éxito.")