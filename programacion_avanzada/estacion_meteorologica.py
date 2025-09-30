class EstacionMeteorologica:
    def __init__(self, id_estacion, ubicacion, tipo_sensores, capacidad_registro):
        self.__id_estacion = id_estacion
        self.__ubicacion = ubicacion
        self.__tipo_sensores = tipo_sensores
        self.__capacidad_registro = capacidad_registro
        self.__datos_climaticos = []  

    
# Getters y Setters
    def get_id_estacion(self):
        return self.__id_estacion

    def set_id_estacion(self, id_estacion):
        self.__id_estacion = id_estacion

    def get_ubicacion(self):
        return self.__ubicacion

    def set_ubicacion(self, ubicacion):
        self.__ubicacion = ubicacion

    def get_tipo_sensores(self):
        return self.__tipo_sensores

    def set_tipo_sensores(self, tipo_sensores):
        self.__tipo_sensores = tipo_sensores

    def get_capacidad_registro(self):
        return self.__capacidad_registro

    def set_capacidad_registro(self, capacidad_registro):
        self.__capacidad_registro = capacidad_registro

    def get_datos_climaticos(self):
        return self.__datos_climaticos

    def set_datos_climaticos(self, datos_climaticos):
        self.__datos_climaticos = datos_climaticos

    # Métodos de la clase
    def registrar_clima(self, dato_climatico):
        """Agrega un registro de clima a la estación"""
        if len(self.__datos_climaticos) < self.__capacidad_registro:
            self.__datos_climaticos.append(dato_climatico)
        else:
            print("⚠️ Capacidad de registro alcanzada.")

    def obtener_datos(self):
        """Retorna la lista de datos climáticos registrados"""
        return self.__datos_climaticos

    def mostrar_informacion(self):
        return (f"Estación ID: {self.__id_estacion}, Ubicación: {self.__ubicacion}, "
                f"Sensores: {self.__tipo_sensores}, Capacidad: {self.__capacidad_registro}, "
                f"Registros actuales: {len(self.__datos_climaticos)}")

# """
# ===================================
# PRUEBAS UNITARIAS
# ===================================
# """
# # Mock para DatoClimatico, ya que no podemos importarlo directamente sin riesgo de bucles
# class MockDatoClimatico:
#     def __init__(self, temp):
#         self.temp = temp

# # 1. Crear una instancia de EstacionMeteorologica
# estacion_test = EstacionMeteorologica("E01", "Centro", "Temp/Hum", 2)
# print(f"Prueba 1: Creación - ID: {estacion_test.get_id_estacion()}, Capacidad: {estacion_test.get_capacidad_registro()}")

# # 2. Probar los setters
# estacion_test.set_ubicacion("Norte")
# estacion_test.set_capacidad_registro(3)
# print(f"Prueba 2: Setters - Ubicación: {estacion_test.get_ubicacion()}, Capacidad: {estacion_test.get_capacidad_registro()}")

# # 3. Probar registrar_clima y obtener_datos
# dato1 = MockDatoClimatico(25)
# dato2 = MockDatoClimatico(26)
# estacion_test.registrar_clima(dato1)
# estacion_test.registrar_clima(dato2)
# registros = estacion_test.obtener_datos()
# print(f"Prueba 3: registrar_clima - Nro. de registros: {len(registros)}")
# assert len(registros) == 2

# # 4. Probar el límite de capacidad
# dato3 = MockDatoClimatico(27)
# dato4 = MockDatoClimatico(28)
# estacion_test.registrar_clima(dato3)
# print("Prueba 4: Límite de capacidad - Intentando agregar un 4to elemento a una capacidad de 3...")
# estacion_test.registrar_clima(dato4) # Esto debería imprimir una advertencia
# registros_limite = estacion_test.obtener_datos()
# print(f"Prueba 4.1: Nro. de registros final: {len(registros_limite)}")
# assert len(registros_limite) == 3

# # 5. Probar mostrar_informacion
# info = estacion_test.mostrar_informacion()
# print(f"Prueba 5: mostrar_informacion - Salida: {info}")
# assert "Registros actuales: 3" in info

# # 6. Probar set_datos_climaticos
# estacion_test.set_datos_climaticos([dato1])
# print(f"Prueba 6: set_datos_climaticos - Nro. de registros: {len(estacion_test.get_datos_climaticos())}")
# assert len(estacion_test.get_datos_climaticos()) == 1

# print("Pruebas para EstacionMeteorologica pasadas con éxito.")