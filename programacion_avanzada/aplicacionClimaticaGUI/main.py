from aplicacion_climatica import AplicacionClimatica
from estacion_meteorologica import EstacionMeteorologica
from dato_climatico import DatoClimatico
from suelo import Suelo
from fuentes_agua import FuentesAgua
from comunidad import Comunidad

def mostrar_menu():
    """Muestra el menú principal en la consola."""
    print("\n===== MENÚ DE APLICACIÓN CLIMÁTICA =====")
    print("1. Crear nueva Estación Meteorológica")
    print("2. Registrar Dato Climático")
    print("3. Registrar Datos de Suelo")
    print("4. Registrar Fuente de Agua")
    print("5. Crear nueva Comunidad de Agricultores")
    print("6. Mostrar Resumen General")
    print("7. Mostrar Histórico de Datos Climáticos")
    print("8. Salir")
    return input("Seleccione una opción: ")

def crear_estacion(app):
    """Solicita datos al usuario para crear una EstacionMeteorologica."""
    print("\n--- Crear Estación ---")
    id_estacion = input("ID de la estación: ")
    ubicacion = input("Ubicación: ")
    tipo_sensores = input("Tipo de sensores: ")
    capacidad = int(input("Capacidad de registro: "))
    
    estacion = EstacionMeteorologica(id_estacion, ubicacion, tipo_sensores, capacidad)
    # Usamos el setter para añadir la estación a la lista de la app
    app.set_lista_estaciones(app.get_lista_estaciones() + [estacion])
    print(f"✅ Estación '{id_estacion}' creada y registrada.")

def registrar_dato_climatico(app):
    """Solicita datos para registrar un DatoClimatico."""
    print("\n--- Registrar Dato Climático ---")
    if not app.get_lista_estaciones():
        print("⚠️ Primero debe crear al menos una estación meteorológica.")
        return

    print("Estaciones disponibles:")
    for i, est in enumerate(app.get_lista_estaciones()):
        print(f"{i + 1}. {est.get_id_estacion()}")
    
    try:
        opcion = int(input("Seleccione la estación asociada: ")) - 1
        estacion_sel = app.get_lista_estaciones()[opcion]
    except (ValueError, IndexError):
        print("⚠️ Selección no válida.")
        return

    fecha_hora = input("Fecha y hora (YYYY-MM-DD HH:MM): ")
    temperatura = float(input("Temperatura (°C): "))
    precipitacion = float(input("Precipitación (mm): "))
    humedad = float(input("Humedad (%): "))
    viento_vel = float(input("Velocidad del viento (km/h): "))
    viento_dir = input("Dirección del viento: ")

    dato = DatoClimatico(fecha_hora, temperatura, precipitacion, humedad, viento_vel, viento_dir, estacion_sel)
    app.almacenar_datos(dato)
    print("✅ Dato climático registrado.")

def registrar_suelo(app):
    """Solicita datos para registrar un Suelo."""
    print("\n--- Registrar Datos de Suelo ---")
    id_recurso = input("ID del recurso: ")
    calidad = input("Calidad del suelo: ")
    id_parcela = input("ID de la parcela: ")
    ph = float(input("pH del suelo: "))
    nutrientes = input("Nutrientes principales: ")
    clasificacion = input("Clasificación del suelo: ")

    suelo = Suelo(id_recurso, calidad, id_parcela, ph, nutrientes, clasificacion)
    app.almacenar_datos(suelo)
    print("✅ Datos de suelo registrados.")

def registrar_agua(app):
    """Solicita datos para registrar una Fuente de Agua."""
    print("\n--- Registrar Fuente de Agua ---")
    id_recurso = input("ID del recurso: ")
    calidad = input("Calidad del agua (excelente, buena, regular, mala): ")
    id_fuente = input("ID de la fuente: ")
    tipo = input("Tipo de fuente (río, pozo, embalse, etc.): ")

    agua = FuentesAgua(id_recurso, calidad, id_fuente, tipo)
    app.almacenar_datos(agua)
    print("✅ Fuente de agua registrada.")

def crear_comunidad(app):
    """Solicita datos para crear una Comunidad."""
    print("\n--- Crear Comunidad ---")
    id_agricultor = input("ID del agricultor líder: ")
    nombre = input("Nombre de la comunidad: ")
    ubicacion = input("Ubicación de la comunidad: ")
    
    # En un sistema real, aquí se podrían seleccionar parcelas existentes
    comunidad = Comunidad(id_agricultor, nombre, ubicacion, [])
    app.set_comunidades(app.get_comunidades() + [comunidad])
    print(f"✅ Comunidad '{nombre}' creada y registrada.")


def main():
    """Función principal que ejecuta el menú interactivo."""
    app = AplicacionClimatica()

    while True:
        opcion = mostrar_menu()
        
        if opcion == '1':
            crear_estacion(app)
        elif opcion == '2':
            registrar_dato_climatico(app)
        elif opcion == '3':
            registrar_suelo(app)
        elif opcion == '4':
            registrar_agua(app)
        elif opcion == '5':
            crear_comunidad(app)
        elif opcion == '6':
            print("\n--- Resumen General ---")
            app.mostrar_resumen()
        elif opcion == '7':
            print("\n--- Histórico de Datos Climáticos ---")
            app.generar_historico()
        elif opcion == '8':
            print("👋 Saliendo de la aplicación. ¡Hasta pronto!")
            break
        else:
            print("⚠️ Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()