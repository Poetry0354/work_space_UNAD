import sqlite3

# -------------------------------------------------------
# Función para conectar a la base de datos
# -------------------------------------------------------
def conectar():
    """Establece conexión con la base de datos."""
    return sqlite3.connect("aplicacion_climatica.db")


# -------------------------------------------------------
# Función para crear las tablas
# -------------------------------------------------------
def crear_tablas():
    """Crea todas las tablas necesarias para la aplicación."""
    conexion = conectar()
    cursor = conexion.cursor()

    # ------------------------------
    # Tabla de estaciones
    # ------------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS estaciones (
        id_estacion TEXT PRIMARY KEY,
        ubicacion TEXT NOT NULL,
        tipo_sensores TEXT,
        capacidad INTEGER
    )
    """)

    # ------------------------------
    # Tabla de datos climáticos
    # ------------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS datos_climaticos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha_hora TEXT,
        temperatura REAL,
        precipitacion REAL,
        humedad REAL,
        velocidad_viento REAL,
        direccion_viento TEXT,
        estacion_id TEXT,
        FOREIGN KEY (estacion_id) REFERENCES estaciones(id_estacion)
    )
    """)

    # ------------------------------
    # Tabla de suelos
    # ------------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS suelos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_recurso TEXT,
        calidad TEXT,
        id_parcela TEXT,
        ph REAL,
        nutrientes TEXT,
        clasificacion TEXT
    )
    """)

    # ------------------------------
    # Tabla de fuentes de agua
    # ------------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS fuentes_agua (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_recurso TEXT,
        calidad TEXT,
        id_fuente TEXT,
        tipo TEXT
    )
    """)

    # ------------------------------
    # Tabla de comunidades
    # ------------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS comunidades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_agricultor TEXT,
        nombre TEXT,
        ubicacion TEXT
    )
    """)

    conexion.commit()
    conexion.close()
    print("✅ Tablas creadas correctamente y base de datos lista.")


# -------------------------------------------------------
# Ejecutar solo si se ejecuta directamente el script
# -------------------------------------------------------
if __name__ == "__main__":
    crear_tablas()
