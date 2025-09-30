class DatoClimatico:
    def __init__(self, fecha_hora, temperatura, precipitacion, humedad, velocidad_viento, direccion_viento, estacion_asociada):
        self.__fecha_hora = fecha_hora
        self.__temperatura = temperatura
        self.__precipitacion = precipitacion
        self.__humedad = humedad
        self.__velocidad_viento = velocidad_viento
        self.__direccion_viento = direccion_viento
        self.__estacion_asociada = estacion_asociada  # Referencia a EstacionMeteorologica

    # Getters y Setters
    def get_fecha_hora(self):
        return self.__fecha_hora

    def set_fecha_hora(self, fecha_hora):
        self.__fecha_hora = fecha_hora

    def get_temperatura(self):
        return self.__temperatura

    def set_temperatura(self, temperatura):
        self.__temperatura = temperatura

    def get_precipitacion(self):
        return self.__precipitacion

    def set_precipitacion(self, precipitacion):
        self.__precipitacion = precipitacion

    def get_humedad(self):
        return self.__humedad

    def set_humedad(self, humedad):
        self.__humedad = humedad

    def get_velocidad_viento(self):
        return self.__velocidad_viento

    def set_velocidad_viento(self, velocidad_viento):
        self.__velocidad_viento = velocidad_viento

    def get_direccion_viento(self):
        return self.__direccion_viento

    def set_direccion_viento(self, direccion_viento):
        self.__direccion_viento = direccion_viento

    def get_estacion_asociada(self):
        return self.__estacion_asociada

    def set_estacion_asociada(self, estacion_asociada):
        self.__estacion_asociada = estacion_asociada

    # Métodos de la clase
    def mostrar_registro(self):
        return (f"[{self.__fecha_hora}] Temp: {self.__temperatura}°C, "
                f"Precipitación: {self.__precipitacion}mm, Humedad: {self.__humedad}%, "
                f"Viento: {self.__velocidad_viento} km/h {self.__direccion_viento}, "
                f"Estación: {self.__estacion_asociada.get_id_estacion() if self.__estacion_asociada else 'N/A'}")

    @staticmethod
    def calcular_promedio(lista_datos):
        """Calcula el promedio de temperatura de una lista de DatoClimatico"""
        if not lista_datos:
            return None
        total_temp = sum(d.get_temperatura() for d in lista_datos)
        return total_temp / len(lista_datos)

    def exportar_registro(self):
        """Devuelve un diccionario exportable (ej. para JSON o CSV)"""
        return {
            "fecha_hora": self.__fecha_hora,
            "temperatura": self.__temperatura,
            "precipitacion": self.__precipitacion,
            "humedad": self.__humedad,
            "velocidad_viento": self.__velocidad_viento,
            "direccion_viento": self.__direccion_viento,
            "estacion_asociada": self.__estacion_asociada.get_id_estacion() if self.__estacion_asociada else None
        }

# """
# ===================================
# PRUEBAS UNITARIAS
# ===================================
# """
# # Mock para EstacionMeteorologica
# class MockEstacion:
#     def __init__(self, id_estacion):
#         self._id_estacion = id_estacion
#     def get_id_estacion(self):
#         return self._id_estacion

# # 1. Crear una instancia de DatoClimatico
# estacion_mock = MockEstacion("E-TEST")
# dato_test = DatoClimatico("2025-01-01 12:00", 22, 5, 80, 15, "Sur", estacion_mock)
# print(f"Prueba 1: Creación - Temp: {dato_test.get_temperatura()}, Estación: {dato_test.get_estacion_asociada().get_id_estacion()}")

# # 2. Probar los setters
# dato_test.set_temperatura(23.5)
# dato_test.set_humedad(78)
# print(f"Prueba 2: Setters - Temp: {dato_test.get_temperatura()}, Humedad: {dato_test.get_humedad()}")

# # 3. Probar mostrar_registro
# registro_str = dato_test.mostrar_registro()
# print(f"Prueba 3: mostrar_registro - Salida: {registro_str}")
# assert "Temp: 23.5°C" in registro_str
# assert "Estación: E-TEST" in registro_str

# # 4. Probar el método estático calcular_promedio
# dato_a = DatoClimatico("d1", 20, 0, 0, 0, "N", None)
# dato_b = DatoClimatico("d2", 30, 0, 0, 0, "N", None)
# promedio = DatoClimatico.calcular_promedio([dato_a, dato_b])
# print(f"Prueba 4: calcular_promedio - Promedio: {promedio}")
# assert promedio == 25

# # 5. Probar exportar_registro
# export_dict = dato_test.exportar_registro()
# print(f"Prueba 5: exportar_registro - Salida: {export_dict}")
# assert export_dict["temperatura"] == 23.5
# assert export_dict["estacion_asociada"] == "E-TEST"

# print("Pruebas para DatoClimatico pasadas con éxito.")