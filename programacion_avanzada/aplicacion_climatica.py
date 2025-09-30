from estacion_meteorologica import EstacionMeteorologica
from dato_climatico import DatoClimatico
from suelo import Suelo
from fuentes_agua import FuentesAgua
from comunidad import Comunidad


class AplicacionClimatica:
    def __init__(self):
        self.__lista_estaciones = []
        self.__registros_climaticos = []
        self.__datos_suelo = []
        self.__datos_agua = []
        self.__comunidades = []

    # =====================
    # Getters y Setters
    # =====================
    def get_lista_estaciones(self):
        return self.__lista_estaciones

    def set_lista_estaciones(self, lista_estaciones):
        self.__lista_estaciones = lista_estaciones

    def get_registros_climaticos(self):
        return self.__registros_climaticos

    def set_registros_climaticos(self, registros_climaticos):
        self.__registros_climaticos = registros_climaticos

    def get_datos_suelo(self):
        return self.__datos_suelo

    def set_datos_suelo(self, datos_suelo):
        self.__datos_suelo = datos_suelo

    def get_datos_agua(self):
        return self.__datos_agua

    def set_datos_agua(self, datos_agua):
        self.__datos_agua = datos_agua

    def get_comunidades(self):
        return self.__comunidades

    def set_comunidades(self, comunidades):
        self.__comunidades = comunidades

    # =====================
    # Métodos propios
    # =====================
    def almacenar_datos(self, dato):
        """Recibe un dato climático, de suelo o agua y lo almacena en la lista correspondiente"""
        if isinstance(dato, DatoClimatico):
            self.__registros_climaticos.append(dato)
        elif isinstance(dato, Suelo):
            self.__datos_suelo.append(dato)
        elif isinstance(dato, FuentesAgua):
            self.__datos_agua.append(dato)

    def generar_historico(self):
        print("Mostrando histórico de datos climáticos...")
        for registro in self.__registros_climaticos:
            print(registro.mostrar_registro())

    def predecir_clima(self):
        # Simulación (podrías meter lógica real aquí después)
        print("Predicción: Probabilidad de lluvia del 40% 🌧️")

    def mostrar_resumen(self):
        print("===== Resumen de la Aplicación Climática =====")
        print(f"Estaciones registradas: {len(self.__lista_estaciones)}")
        print(f"Datos climáticos registrados: {len(self.__registros_climaticos)}")
        print(f"Datos de suelo registrados: {len(self.__datos_suelo)}")
        print(f"Fuentes de agua registradas: {len(self.__datos_agua)}")
        print(f"Comunidades registradas: {len(self.__comunidades)}")

# """
# ===================================
# PRUEBAS UNITARIAS
# ===================================
# """
# from estacion_meteorologica import EstacionMeteorologica
# from dato_climatico import DatoClimatico
# from suelo import Suelo
# from fuentes_agua import FuentesAgua
# from comunidad import Comunidad

# # 1. Crear una instancia de AplicacionClimatica
# app_test = AplicacionClimatica()
# print("Prueba 1: Creación - Objeto AplicacionClimatica creado.")
# assert len(app_test.get_lista_estaciones()) == 0
# assert len(app_test.get_registros_climaticos()) == 0
# assert len(app_test.get_datos_suelo()) == 0
# assert len(app_test.get_datos_agua()) == 0
# assert len(app_test.get_comunidades()) == 0

# # 2. Probar los setters
# mock_estacion = EstacionMeteorologica("E-T", "Ubi-T", "Sens-T", 10)
# mock_comunidad = Comunidad("C-T", "Com-T", "Ubi-C", [])
# app_test.set_lista_estaciones([mock_estacion])
# app_test.set_comunidades([mock_comunidad])
# print(f"Prueba 2: Setters - Nro. Estaciones: {len(app_test.get_lista_estaciones())}, Nro. Comunidades: {len(app_test.get_comunidades())}")
# assert len(app_test.get_lista_estaciones()) == 1
# assert len(app_test.get_comunidades()) == 1

# # 3. Probar almacenar_datos
# mock_dato_climatico = DatoClimatico("F-T", 0, 0, 0, 0, "N", None)
# mock_suelo = Suelo("R-T", "Cal-T", "P-T", 0, "Nut-T", "Clas-T")
# mock_agua = FuentesAgua("R-A", "Cal-A", "F-A", "T-A")

# app_test.almacenar_datos(mock_dato_climatico)
# app_test.almacenar_datos(mock_suelo)
# app_test.almacenar_datos(mock_agua)

# print(f"Prueba 3: almacenar_datos - Registros climáticos: {len(app_test.get_registros_climaticos())}")
# print(f"Prueba 3: almacenar_datos - Datos de suelo: {len(app_test.get_datos_suelo())}")
# print(f"Prueba 3: almacenar_datos - Datos de agua: {len(app_test.get_datos_agua())}")
# assert len(app_test.get_registros_climaticos()) == 1
# assert len(app_test.get_datos_suelo()) == 1
# assert len(app_test.get_datos_agua()) == 1

# # 4. Probar los getters (ya se usaron implícitamente, pero se puede hacer explícito)
# estaciones = app_test.get_lista_estaciones()
# print(f"Prueba 4: Getters - La primera estación es {estaciones[0].get_id_estacion()}")
# assert estaciones[0].get_id_estacion() == "E-T"

# # 5. Probar generar_historico, predecir_clima y mostrar_resumen
# # Estos métodos principalmente imprimen en consola. La prueba consiste en verificar que se ejecutan sin errores.
# print("\nPrueba 5: Ejecución de métodos de reporte.")
# app_test.generar_historico()
# app_test.predecir_clima()
# app_test.mostrar_resumen()
# print("Prueba 5: Métodos de reporte ejecutados.")

# print("\nPruebas para AplicacionClimatica pasadas con éxito.")