from aplicacion_climatica import AplicacionClimatica
from estacion_meteorologica import EstacionMeteorologica
from dato_climatico import DatoClimatico
from suelo import Suelo
from fuentes_agua import FuentesAgua
from comunidad import Comunidad


def def main():
    # Crear aplicación
    app = AplicacionClimatica()

    # Crear objetos de prueba
    estacion = EstacionMeteorologica("E001", "Tolima", "Temperatura/Humedad", 1000)
    # CORREGIDO: Argumentos de precipitación y humedad intercambiados
    dato_clima = DatoClimatico("2025-09-21 10:00", 25.5, 10, 60, 5, "Norte", estacion)

    
    suelo = Suelo("R001", "Buena", "S001", 6.5, "Rico en nitrógeno", "Franco arenoso")

    agua = FuentesAgua("A001", "Regular", "R001", "pozo")
    # CORREGIDO: Se pasa el objeto 'suelo' en lugar de una lista de strings
    comunidad = Comunidad("C001", "Agricultor Pedro", "Zona rural", [suelo])

    # Registrar en la aplicación
    app.set_lista_estaciones([estacion])
    app.set_comunidades([comunidad])
    app.almacenar_datos(dato_clima)
    app.almacenar_datos(suelo)
    app.almacenar_datos(agua)

    # Mostrar resultados
    app.mostrar_resumen()
    print("\n--- Histórico ---")
    app.generar_historico()
    print("\n--- Predicción ---")
    app.predecir_clima()


if __name__ == "__main__":
    main()
