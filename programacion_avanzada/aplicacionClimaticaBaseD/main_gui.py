import tkinter as tk
from tkinter import messagebox
from db import conectar, crear_tablas
import sqlite3 
from tkinter import ttk
import matplotlib.pyplot as plt
import subprocess
import os
import sys
import os

# --- Función para abrir el chat de soporte ---
def abrir_chat_soporte():
    """
    Lanza el cliente de chat en un proceso separado, usando una ruta absoluta
    y el ejecutable de Python correcto.
    """
    try:
        # Obtenemos la ruta absoluta del directorio donde se encuentra este script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Construimos la ruta completa para chat_client.py
        client_path = os.path.join(script_dir, 'chat_client.py')
        
        if not os.path.exists(client_path):
            messagebox.showerror("Error", f"No se pudo encontrar el script en la ruta:\n{client_path}")
            return

        # Usamos sys.executable para garantizar que se use el mismo intérprete de Python
        subprocess.Popen([sys.executable, client_path])

    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error al abrir el chat: {e}")

# --------------------------------------------------------
# Funciones de los botones
# --------------------------------------------------------
def abrir_estaciones():
    win = tk.Toplevel(ventana)
    win.title("📡 Registrar Estación Meteorológica")
    win.geometry("700x500")
    win.config(bg="#f1faee")

    tk.Label(win, text="Registro de Estaciones", font=("Arial", 14, "bold"), bg="#f1faee").pack(pady=10)

    frame = tk.Frame(win, bg="#f1faee")
    frame.pack(pady=10)

    # --- Campos de formulario ---
    tk.Label(frame, text="ID Estación:", bg="#f1faee").grid(row=0, column=0, sticky="w")
    entry_id = tk.Entry(frame, width=30)
    entry_id.grid(row=0, column=1, pady=5)

    tk.Label(frame, text="Ubicación:", bg="#f1faee").grid(row=1, column=0, sticky="w")
    entry_ubic = tk.Entry(frame, width=30)
    entry_ubic.grid(row=1, column=1, pady=5)

    tk.Label(frame, text="Tipo de Sensores:", bg="#f1faee").grid(row=2, column=0, sticky="w")
    entry_sens = tk.Entry(frame, width=30)
    entry_sens.grid(row=2, column=1, pady=5)

    tk.Label(frame, text="Capacidad de Registro:", bg="#f1faee").grid(row=3, column=0, sticky="w")
    entry_cap = tk.Entry(frame, width=30)
    entry_cap.grid(row=3, column=1, pady=5)

    # --- Tabla ---
    tabla = ttk.Treeview(win, columns=("ID", "Ubicación", "Sensores", "Capacidad"), show="headings", height=10)
    tabla.heading("ID", text="ID Estación")
    tabla.heading("Ubicación", text="Ubicación")
    tabla.heading("Sensores", text="Tipo de Sensores")
    tabla.heading("Capacidad", text="Capacidad")
    tabla.pack(fill="both", expand=True, padx=20, pady=10)

    scrollbar = ttk.Scrollbar(win, orient="vertical", command=tabla.yview)
    tabla.configure(yscroll=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    # --- Mostrar datos ---
    def mostrar_estaciones():
        for fila in tabla.get_children():
            tabla.delete(fila)
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM estaciones")
        for est in cursor.fetchall():
            tabla.insert("", "end", values=est)
        conexion.close()

    # --- Guardar nueva estación ---
    def guardar_estacion():
        id_est = entry_id.get().strip()
        ubic = entry_ubic.get().strip()
        sens = entry_sens.get().strip()
        cap = entry_cap.get().strip()

        if not id_est or not ubic or not sens or not cap:
            messagebox.showwarning("Campos vacíos", "Por favor completa todos los campos.")
            return
        try:
            cap = int(cap)
        except ValueError:
            messagebox.showerror("Error", "La capacidad debe ser un número entero.")
            return

        try:
            conexion = conectar()
            cursor = conexion.cursor()
            cursor.execute(
                "INSERT INTO estaciones (id_estacion, ubicacion, tipo_sensores, capacidad) VALUES (?, ?, ?, ?)",
                (id_est, ubic, sens, cap)
            )
            conexion.commit()
            conexion.close()
            messagebox.showinfo("Éxito", f"✅ Estación '{id_est}' guardada correctamente.")
            limpiar_campos()
            mostrar_estaciones()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", f"⚠️ Ya existe una estación con el ID '{id_est}'.")

    # --- Cargar datos seleccionados ---
    def seleccionar_estacion(event):
        seleccion = tabla.selection()
        if not seleccion:
            return
        valores = tabla.item(seleccion[0], "values")
        entry_id.delete(0, tk.END)
        entry_id.insert(0, valores[0])
        entry_ubic.delete(0, tk.END)
        entry_ubic.insert(0, valores[1])
        entry_sens.delete(0, tk.END)
        entry_sens.insert(0, valores[2])
        entry_cap.delete(0, tk.END)
        entry_cap.insert(0, valores[3])

    tabla.bind("<<TreeviewSelect>>", seleccionar_estacion)

    # --- Actualizar estación seleccionada ---
    def actualizar_estacion():
        id_est = entry_id.get().strip()
        ubic = entry_ubic.get().strip()
        sens = entry_sens.get().strip()
        cap = entry_cap.get().strip()

        if not id_est:
            messagebox.showwarning("Error", "Selecciona una estación primero.")
            return
        try:
            cap = int(cap)
        except ValueError:
            messagebox.showerror("Error", "La capacidad debe ser un número.")
            return

        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("""
            UPDATE estaciones
            SET ubicacion=?, tipo_sensores=?, capacidad=?
            WHERE id_estacion=?
        """, (ubic, sens, cap, id_est))
        conexion.commit()
        conexion.close()

        messagebox.showinfo("Actualizado", f"🔄 Estación '{id_est}' actualizada correctamente.")
        limpiar_campos()
        mostrar_estaciones()

    # --- Eliminar estación ---
    def eliminar_estacion():
        seleccion = tabla.selection()
        if not seleccion:
            messagebox.showwarning("Atención", "Selecciona una estación para eliminar.")
            return
        id_est = tabla.item(seleccion[0], "values")[0]

        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM estaciones WHERE id_estacion = ?", (id_est,))
        conexion.commit()
        conexion.close()

        messagebox.showinfo("Eliminado", f"🗑️ Estación '{id_est}' eliminada.")
        mostrar_estaciones()

    # --- Limpiar campos ---
    def limpiar_campos():
        entry_id.delete(0, tk.END)
        entry_ubic.delete(0, tk.END)
        entry_sens.delete(0, tk.END)
        entry_cap.delete(0, tk.END)

    # --- Botones ---
    boton_frame = tk.Frame(win, bg="#f1faee")
    boton_frame.pack(pady=10)

    tk.Button(boton_frame, text="💾 Guardar", bg="#457b9d", fg="white",
              font=("Arial", 10, "bold"), command=guardar_estacion).grid(row=0, column=0, padx=5)

    tk.Button(boton_frame, text="🗑️ Eliminar", bg="#e63946", fg="white",
              font=("Arial", 10, "bold"), command=eliminar_estacion).grid(row=0, column=1, padx=5)

    tk.Button(boton_frame, text="✏️ Actualizar", bg="#f4a261", fg="white",
              font=("Arial", 10, "bold"), command=actualizar_estacion).grid(row=0, column=2, padx=5)

    tk.Button(boton_frame, text="🧹 Limpiar", bg="#a8dadc", fg="black",
              font=("Arial", 10, "bold"), command=limpiar_campos).grid(row=0, column=3, padx=5)

    mostrar_estaciones()  # carga inicial



def abrir_dato_climatico():
    win = tk.Toplevel(ventana)
    win.title("🌦️ Registrar Dato Climático")
    win.geometry("850x550")
    win.config(bg="#f1faee")

    tk.Label(win, text="Registro de Datos Climáticos", font=("Arial", 14, "bold"), bg="#f1faee").pack(pady=10)

    frame = tk.Frame(win, bg="#f1faee")
    frame.pack(pady=20)

    # --- Campos ---
    tk.Label(frame, text="Fecha y Hora (YYYY-MM-DD HH:MM):", bg="#f1faee").grid(row=0, column=0, sticky="w")
    entry_fecha = tk.Entry(frame, width=30)
    entry_fecha.grid(row=0, column=1, pady=5)

    tk.Label(frame, text="Temperatura (°C):", bg="#f1faee").grid(row=1, column=0, sticky="w")
    entry_temp = tk.Entry(frame, width=30)
    entry_temp.grid(row=1, column=1, pady=5)

    tk.Label(frame, text="Precipitación (mm):", bg="#f1faee").grid(row=2, column=0, sticky="w")
    entry_prec = tk.Entry(frame, width=30)
    entry_prec.grid(row=2, column=1, pady=5)

    tk.Label(frame, text="Humedad (%):", bg="#f1faee").grid(row=3, column=0, sticky="w")
    entry_hum = tk.Entry(frame, width=30)
    entry_hum.grid(row=3, column=1, pady=5)

    tk.Label(frame, text="Velocidad del Viento (m/s):", bg="#f1faee").grid(row=4, column=0, sticky="w")
    entry_vv = tk.Entry(frame, width=30)
    entry_vv.grid(row=4, column=1, pady=5)

    tk.Label(frame, text="Dirección del Viento:", bg="#f1faee").grid(row=5, column=0, sticky="w")
    entry_dir = tk.Entry(frame, width=30)
    entry_dir.grid(row=5, column=1, pady=5)

    tk.Label(frame, text="Estación:", bg="#f1faee").grid(row=6, column=0, sticky="w")

    # --- Combobox con las estaciones ---
    estaciones_combo = ttk.Combobox(frame, width=27, state="readonly")
    estaciones_combo.grid(row=6, column=1, pady=5)

    # Cargar estaciones desde la base
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT id_estacion FROM estaciones")
    estaciones = [fila[0] for fila in cursor.fetchall()]
    conexion.close()
    estaciones_combo["values"] = estaciones

    # --- Tabla ---
    tabla = ttk.Treeview(win, columns=("ID", "Fecha", "Temp", "Prec", "Hum", "Viento", "Dir", "Estación"), show="headings", height=10)
    for col, text in zip(tabla["columns"], ["ID", "Fecha y Hora", "Temp (°C)", "Prec (mm)", "Humedad (%)", "Vel. Viento", "Dir. Viento", "Estación"]):
        tabla.heading(col, text=text)
    tabla.pack(fill="both", expand=True, padx=20, pady=10)

    scrollbar = ttk.Scrollbar(win, orient="vertical", command=tabla.yview)
    tabla.configure(yscroll=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    # --- Mostrar datos ---
    def mostrar_datos():
        for fila in tabla.get_children():
            tabla.delete(fila)
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM datos_climaticos")
        for dato in cursor.fetchall():
            tabla.insert("", "end", values=dato)
        conexion.close()

    # --- Guardar dato climático ---
    def guardar_dato():
        fecha = entry_fecha.get().strip()
        temp = entry_temp.get().strip()
        prec = entry_prec.get().strip()
        hum = entry_hum.get().strip()
        vv = entry_vv.get().strip()
        dirv = entry_dir.get().strip()
        estacion = estaciones_combo.get().strip()

        if not all([fecha, temp, prec, hum, vv, dirv, estacion]):
            messagebox.showwarning("Campos vacíos", "Por favor completa todos los campos.")
            return

        try:
            temp, prec, hum, vv = float(temp), float(prec), float(hum), float(vv)
        except ValueError:
            messagebox.showerror("Error", "Los campos numéricos deben contener números válidos.")
            return

        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO datos_climaticos (fecha_hora, temperatura, precipitacion, humedad, velocidad_viento, direccion_viento, estacion_id)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (fecha, temp, prec, hum, vv, dirv, estacion))
        conexion.commit()
        conexion.close()

        messagebox.showinfo("Éxito", f"✅ Dato climático guardado correctamente para la estación {estacion}.")
        limpiar_campos()
        mostrar_datos()

    # --- Limpiar campos ---
    def limpiar_campos():
        entry_fecha.delete(0, tk.END)
        entry_temp.delete(0, tk.END)
        entry_prec.delete(0, tk.END)
        entry_hum.delete(0, tk.END)
        entry_vv.delete(0, tk.END)
        entry_dir.delete(0, tk.END)
        estaciones_combo.set("")

    # --- Botones ---
    boton_frame = tk.Frame(win, bg="#f1faee")
    boton_frame.pack(pady=10)

    tk.Button(boton_frame, text="💾 Guardar", bg="#457b9d", fg="white",
              font=("Arial", 10, "bold"), command=guardar_dato).grid(row=0, column=0, padx=5)
    tk.Button(boton_frame, text="🧹 Limpiar", bg="#a8dadc", fg="black",
              font=("Arial", 10, "bold"), command=limpiar_campos).grid(row=0, column=1, padx=5)
    tk.Button(boton_frame, text="🔄 Actualizar Tabla", bg="#f4a261", fg="white",
              font=("Arial", 10, "bold"), command=mostrar_datos).grid(row=0, column=2, padx=5)

    mostrar_datos()  # carga inicial de registros


def abrir_suelo():
    win = tk.Toplevel(ventana)
    win.title("🌱 Registrar Suelo")
    win.geometry("850x600")
    win.config(bg="#f1faee")

    tk.Label(win, text="Registro de Suelos", font=("Arial", 14, "bold"), bg="#f1faee").pack(pady=10)

    frame = tk.Frame(win, bg="#f1faee")
    frame.pack(pady=20)

    # --- Campos del formulario ---
    tk.Label(frame, text="ID Recurso:", bg="#f1faee").grid(row=0, column=0, sticky="w")
    entry_id_recurso = tk.Entry(frame, width=30)
    entry_id_recurso.grid(row=0, column=1, pady=5)

    tk.Label(frame, text="Calidad:", bg="#f1faee").grid(row=1, column=0, sticky="w")
    entry_calidad = tk.Entry(frame, width=30)
    entry_calidad.grid(row=1, column=1, pady=5)

    tk.Label(frame, text="ID Parcela:", bg="#f1faee").grid(row=2, column=0, sticky="w")
    entry_parcela = tk.Entry(frame, width=30)
    entry_parcela.grid(row=2, column=1, pady=5)

    tk.Label(frame, text="pH:", bg="#f1faee").grid(row=3, column=0, sticky="w")
    entry_ph = tk.Entry(frame, width=30)
    entry_ph.grid(row=3, column=1, pady=5)

    tk.Label(frame, text="Nutrientes:", bg="#f1faee").grid(row=4, column=0, sticky="w")
    entry_nutrientes = tk.Entry(frame, width=30)
    entry_nutrientes.grid(row=4, column=1, pady=5)

    tk.Label(frame, text="Clasificación:", bg="#f1faee").grid(row=5, column=0, sticky="w")
    entry_clasificacion = tk.Entry(frame, width=30)
    entry_clasificacion.grid(row=5, column=1, pady=5)

    # --- Tabla ---
    tabla = ttk.Treeview(win, columns=("ID", "Recurso", "Calidad", "Parcela", "pH", "Nutrientes", "Clasificación"), show="headings", height=10)
    for col, text in zip(tabla["columns"], ["ID", "ID Recurso", "Calidad", "ID Parcela", "pH", "Nutrientes", "Clasificación"]):
        tabla.heading(col, text=text)
    tabla.pack(fill="both", expand=True, padx=20, pady=10)

    scrollbar = ttk.Scrollbar(win, orient="vertical", command=tabla.yview)
    tabla.configure(yscroll=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    # --- Mostrar suelos ---
    def mostrar_suelos():
        for fila in tabla.get_children():
            tabla.delete(fila)
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM suelos")
        for suelo in cursor.fetchall():
            tabla.insert("", "end", values=suelo)
        conexion.close()

    # --- Guardar suelo ---
    def guardar_suelo():
        id_recurso = entry_id_recurso.get().strip()
        calidad = entry_calidad.get().strip()
        parcela = entry_parcela.get().strip()
        ph = entry_ph.get().strip()
        nutrientes = entry_nutrientes.get().strip()
        clasificacion = entry_clasificacion.get().strip()

        if not all([id_recurso, calidad, parcela, ph, nutrientes, clasificacion]):
            messagebox.showwarning("Campos vacíos", "Por favor completa todos los campos.")
            return

        try:
            ph = float(ph)
        except ValueError:
            messagebox.showerror("Error", "El valor de pH debe ser numérico.")
            return

        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO suelos (id_recurso, calidad, id_parcela, ph, nutrientes, clasificacion)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (id_recurso, calidad, parcela, ph, nutrientes, clasificacion))
        conexion.commit()
        conexion.close()

        messagebox.showinfo("Éxito", f"✅ Suelo '{id_recurso}' guardado correctamente.")
        limpiar_campos()
        mostrar_suelos()

    # --- Limpiar campos ---
    def limpiar_campos():
        entry_id_recurso.delete(0, tk.END)
        entry_calidad.delete(0, tk.END)
        entry_parcela.delete(0, tk.END)
        entry_ph.delete(0, tk.END)
        entry_nutrientes.delete(0, tk.END)
        entry_clasificacion.delete(0, tk.END)

    # --- Eliminar registro ---
    def eliminar_suelo():
        seleccion = tabla.selection()
        if not seleccion:
            messagebox.showwarning("Atención", "Selecciona un suelo para eliminar.")
            return
        id_suelo = tabla.item(seleccion[0], "values")[0]
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM suelos WHERE id = ?", (id_suelo,))
        conexion.commit()
        conexion.close()
        messagebox.showinfo("Eliminado", f"🗑️ Suelo ID {id_suelo} eliminado correctamente.")
        mostrar_suelos()

    # --- Botones ---
    boton_frame = tk.Frame(win, bg="#f1faee")
    boton_frame.pack(pady=10)

    tk.Button(boton_frame, text="💾 Guardar", bg="#457b9d", fg="white",
              font=("Arial", 10, "bold"), command=guardar_suelo).grid(row=0, column=0, padx=5)
    tk.Button(boton_frame, text="🗑️ Eliminar", bg="#e63946", fg="white",
              font=("Arial", 10, "bold"), command=eliminar_suelo).grid(row=0, column=1, padx=5)
    tk.Button(boton_frame, text="🧹 Limpiar", bg="#a8dadc", fg="black",
              font=("Arial", 10, "bold"), command=limpiar_campos).grid(row=0, column=2, padx=5)
    tk.Button(boton_frame, text="🔄 Actualizar Tabla", bg="#f4a261", fg="white",
              font=("Arial", 10, "bold"), command=mostrar_suelos).grid(row=0, column=3, padx=5)

    mostrar_suelos()


def abrir_fuente_agua():
    win = tk.Toplevel(ventana)
    win.title("💧 Registrar Fuente de Agua")
    win.geometry("850x600")
    win.config(bg="#f1faee")

    tk.Label(win, text="Registro de Fuentes de Agua", font=("Arial", 14, "bold"), bg="#f1faee").pack(pady=10)

    frame = tk.Frame(win, bg="#f1faee")
    frame.pack(pady=20)

    # --- Campos del formulario ---
    tk.Label(frame, text="ID Recurso:", bg="#f1faee").grid(row=0, column=0, sticky="w")
    entry_id_recurso = tk.Entry(frame, width=30)
    entry_id_recurso.grid(row=0, column=1, pady=5)

    tk.Label(frame, text="Calidad:", bg="#f1faee").grid(row=1, column=0, sticky="w")
    entry_calidad = tk.Entry(frame, width=30)
    entry_calidad.grid(row=1, column=1, pady=5)

    tk.Label(frame, text="ID Fuente:", bg="#f1faee").grid(row=2, column=0, sticky="w")
    entry_fuente = tk.Entry(frame, width=30)
    entry_fuente.grid(row=2, column=1, pady=5)

    tk.Label(frame, text="Tipo de Fuente:", bg="#f1faee").grid(row=3, column=0, sticky="w")
    entry_tipo = tk.Entry(frame, width=30)
    entry_tipo.grid(row=3, column=1, pady=5)

    # --- Tabla ---
    tabla = ttk.Treeview(win, columns=("ID", "Recurso", "Calidad", "Fuente", "Tipo"), show="headings", height=10)
    for col, text in zip(tabla["columns"], ["ID", "ID Recurso", "Calidad", "ID Fuente", "Tipo de Fuente"]):
        tabla.heading(col, text=text)
    tabla.pack(fill="both", expand=True, padx=20, pady=10)

    scrollbar = ttk.Scrollbar(win, orient="vertical", command=tabla.yview)
    tabla.configure(yscroll=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    # --- Mostrar fuentes ---
    def mostrar_fuentes():
        for fila in tabla.get_children():
            tabla.delete(fila)
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM fuentes_agua")
        for fuente in cursor.fetchall():
            tabla.insert("", "end", values=fuente)
        conexion.close()

    # --- Guardar fuente ---
    def guardar_fuente():
        id_recurso = entry_id_recurso.get().strip()
        calidad = entry_calidad.get().strip()
        fuente = entry_fuente.get().strip()
        tipo = entry_tipo.get().strip()

        if not all([id_recurso, calidad, fuente, tipo]):
            messagebox.showwarning("Campos vacíos", "Por favor completa todos los campos.")
            return

        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO fuentes_agua (id_recurso, calidad, id_fuente, tipo)
            VALUES (?, ?, ?, ?)
        """, (id_recurso, calidad, fuente, tipo))
        conexion.commit()
        conexion.close()

        messagebox.showinfo("Éxito", f"✅ Fuente '{id_fuente}' registrada correctamente.")
        limpiar_campos()
        mostrar_fuentes()

    # --- Limpiar campos ---
    def limpiar_campos():
        entry_id_recurso.delete(0, tk.END)
        entry_calidad.delete(0, tk.END)
        entry_fuente.delete(0, tk.END)
        entry_tipo.delete(0, tk.END)

    # --- Eliminar fuente ---
    def eliminar_fuente():
        seleccion = tabla.selection()
        if not seleccion:
            messagebox.showwarning("Atención", "Selecciona una fuente para eliminar.")
            return
        id_fuente = tabla.item(seleccion[0], "values")[0]
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM fuentes_agua WHERE id = ?", (id_fuente,))
        conexion.commit()
        conexion.close()
        messagebox.showinfo("Eliminado", f"🗑️ Fuente ID {id_fuente} eliminada.")
        mostrar_fuentes()

    # --- Botones ---
    boton_frame = tk.Frame(win, bg="#f1faee")
    boton_frame.pack(pady=10)

    tk.Button(boton_frame, text="💾 Guardar", bg="#457b9d", fg="white",
              font=("Arial", 10, "bold"), command=guardar_fuente).grid(row=0, column=0, padx=5)
    tk.Button(boton_frame, text="🗑️ Eliminar", bg="#e63946", fg="white",
              font=("Arial", 10, "bold"), command=eliminar_fuente).grid(row=0, column=1, padx=5)
    tk.Button(boton_frame, text="🧹 Limpiar", bg="#a8dadc", fg="black",
              font=("Arial", 10, "bold"), command=limpiar_campos).grid(row=0, column=2, padx=5)
    tk.Button(boton_frame, text="🔄 Actualizar Tabla", bg="#f4a261", fg="white",
              font=("Arial", 10, "bold"), command=mostrar_fuentes).grid(row=0, column=3, padx=5)

    mostrar_fuentes()


def abrir_comunidad():
    win = tk.Toplevel(ventana)
    win.title("👩‍🌾 Registrar Comunidad")
    win.geometry("850x550")
    win.config(bg="#f1faee")

    tk.Label(win, text="Registro de Comunidades", font=("Arial", 14, "bold"), bg="#f1faee").pack(pady=10)

    frame = tk.Frame(win, bg="#f1faee")
    frame.pack(pady=20)

    # --- Campos del formulario ---
    tk.Label(frame, text="ID Agricultor:", bg="#f1faee").grid(row=0, column=0, sticky="w")
    entry_id_agricultor = tk.Entry(frame, width=30)
    entry_id_agricultor.grid(row=0, column=1, pady=5)

    tk.Label(frame, text="Nombre de la Comunidad:", bg="#f1faee").grid(row=1, column=0, sticky="w")
    entry_nombre = tk.Entry(frame, width=30)
    entry_nombre.grid(row=1, column=1, pady=5)

    tk.Label(frame, text="Ubicación:", bg="#f1faee").grid(row=2, column=0, sticky="w")
    entry_ubicacion = tk.Entry(frame, width=30)
    entry_ubicacion.grid(row=2, column=1, pady=5)

    # --- Tabla ---
    tabla = ttk.Treeview(win, columns=("ID", "Agricultor", "Nombre", "Ubicación"), show="headings", height=10)
    for col, text in zip(tabla["columns"], ["ID", "ID Agricultor", "Nombre", "Ubicación"]):
        tabla.heading(col, text=text)
    tabla.pack(fill="both", expand=True, padx=20, pady=10)

    scrollbar = ttk.Scrollbar(win, orient="vertical", command=tabla.yview)
    tabla.configure(yscroll=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    # --- Mostrar comunidades ---
    def mostrar_comunidades():
        for fila in tabla.get_children():
            tabla.delete(fila)
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM comunidades")
        for com in cursor.fetchall():
            tabla.insert("", "end", values=com)
        conexion.close()

    # --- Guardar comunidad ---
    def guardar_comunidad():
        id_agricultor = entry_id_agricultor.get().strip()
        nombre = entry_nombre.get().strip()
        ubicacion = entry_ubicacion.get().strip()

        if not all([id_agricultor, nombre, ubicacion]):
            messagebox.showwarning("Campos vacíos", "Por favor completa todos los campos.")
            return

        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO comunidades (id_agricultor, nombre, ubicacion)
            VALUES (?, ?, ?)
        """, (id_agricultor, nombre, ubicacion))
        conexion.commit()
        conexion.close()

        messagebox.showinfo("Éxito", f"✅ Comunidad '{nombre}' registrada correctamente.")
        limpiar_campos()
        mostrar_comunidades()

    # --- Limpiar campos ---
    def limpiar_campos():
        entry_id_agricultor.delete(0, tk.END)
        entry_nombre.delete(0, tk.END)
        entry_ubicacion.delete(0, tk.END)

    # --- Eliminar comunidad ---
    def eliminar_comunidad():
        seleccion = tabla.selection()
        if not seleccion:
            messagebox.showwarning("Atención", "Selecciona una comunidad para eliminar.")
            return
        id_com = tabla.item(seleccion[0], "values")[0]
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM comunidades WHERE id = ?", (id_com,))
        conexion.commit()
        conexion.close()
        messagebox.showinfo("Eliminado", f"🗑️ Comunidad ID {id_com} eliminada correctamente.")
        mostrar_comunidades()

    # --- Botones ---
    boton_frame = tk.Frame(win, bg="#f1faee")
    boton_frame.pack(pady=10)

    tk.Button(boton_frame, text="💾 Guardar", bg="#457b9d", fg="white",
              font=("Arial", 10, "bold"), command=guardar_comunidad).grid(row=0, column=0, padx=5)
    tk.Button(boton_frame, text="🗑️ Eliminar", bg="#e63946", fg="white",
              font=("Arial", 10, "bold"), command=eliminar_comunidad).grid(row=0, column=1, padx=5)
    tk.Button(boton_frame, text="🧹 Limpiar", bg="#a8dadc", fg="black",
              font=("Arial", 10, "bold"), command=limpiar_campos).grid(row=0, column=2, padx=5)
    tk.Button(boton_frame, text="🔄 Actualizar Tabla", bg="#f4a261", fg="white",
              font=("Arial", 10, "bold"), command=mostrar_comunidades).grid(row=0, column=3, padx=5)

    mostrar_comunidades()



def mostrar_resumen():
    win = tk.Toplevel(ventana)
    win.title("📊 Resumen General del Sistema")
    win.geometry("750x550")
    win.config(bg="#f1faee")

    tk.Label(win, text="📊 Resumen de la Aplicación Climática", font=("Arial", 16, "bold"), bg="#f1faee", fg="#1d3557").pack(pady=20)

    frame = tk.Frame(win, bg="#f1faee")
    frame.pack(pady=20)

    # --- Función para obtener los totales ---
    def obtener_totales():
        conexion = conectar()
        cursor = conexion.cursor()
        tablas = {
            "Estaciones": "SELECT COUNT(*) FROM estaciones",
            "Datos Climáticos": "SELECT COUNT(*) FROM datos_climaticos",
            "Suelos": "SELECT COUNT(*) FROM suelos",
            "Fuentes de Agua": "SELECT COUNT(*) FROM fuentes_agua",
            "Comunidades": "SELECT COUNT(*) FROM comunidades"
        }

        resultados = {}
        for nombre, consulta in tablas.items():
            try:
                cursor.execute(consulta)
                resultados[nombre] = cursor.fetchone()[0]
            except:
                resultados[nombre] = 0
        conexion.close()
        return resultados

    # --- Mostrar los resultados ---
    def actualizar_resumen():
        for widget in frame.winfo_children():
            widget.destroy()

        resultados = obtener_totales()

        fila = 0
        colores = ["#a8dadc", "#f1faee", "#e9f5f5", "#cdeae3", "#f8edeb"]
        emojis = ["📡", "🌦️", "🌱", "💧", "👩‍🌾"]

        for (nombre, total), color, emoji in zip(resultados.items(), colores, emojis):
            card = tk.Frame(frame, bg=color, relief="solid", bd=1)
            card.grid(row=fila, column=0, padx=10, pady=8, sticky="ew")

            tk.Label(card, text=f"{emoji} {nombre}", font=("Arial", 13, "bold"), bg=color).pack(side="left", padx=15)
            tk.Label(card, text=f"{total}", font=("Arial", 13), bg=color, fg="#1d3557").pack(side="right", padx=15)

            fila += 1

    # --- Gráfico con matplotlib ---
    def mostrar_grafico():
        resultados = obtener_totales()
        nombres = list(resultados.keys())
        valores = list(resultados.values())

        # Si no hay datos, mostrar advertencia
        if sum(valores) == 0:
            messagebox.showwarning("Sin datos", "No hay registros en la base de datos para graficar.")
            return

        plt.figure(figsize=(7, 5))
        plt.bar(nombres, valores, color=["#457b9d", "#1d3557", "#a8dadc", "#f4a261", "#e63946"])
        plt.title("Resumen de Registros por Tabla", fontsize=14, fontweight="bold")
        plt.ylabel("Cantidad de Registros")
        plt.xticks(rotation=15)
        plt.tight_layout()
        plt.show()

    # --- Botones ---
    boton_frame = tk.Frame(win, bg="#f1faee")
    boton_frame.pack(pady=10)

    tk.Button(
        boton_frame, text="🔄 Actualizar Resumen", bg="#457b9d", fg="white",
        font=("Arial", 10, "bold"), command=actualizar_resumen
    ).grid(row=0, column=0, padx=10)

    tk.Button(
        boton_frame, text="📈 Ver Gráfico", bg="#2a9d8f", fg="white",
        font=("Arial", 10, "bold"), command=mostrar_grafico
    ).grid(row=0, column=1, padx=10)

    # --- Cargar datos iniciales ---
    actualizar_resumen()


def salir():
    ventana.destroy()


# --------------------------------------------------------
# Ventana principal
# --------------------------------------------------------
ventana = tk.Tk()
ventana.title("🌤️ Aplicación Climática")
ventana.geometry("400x500")
ventana.config(bg="#e9f5f5")

tk.Label(ventana, text="Menú Principal", font=("Arial", 16, "bold"), bg="#e9f5f5").pack(pady=15)

# Botones del menú principal
botones = [
    ("📡 Registrar Estación", abrir_estaciones),
    ("🌦️ Registrar Dato Climático", abrir_dato_climatico),
    ("🌱 Registrar Suelo", abrir_suelo),
    ("💧 Registrar Fuente de Agua", abrir_fuente_agua),
    ("👩‍🌾 Registrar Comunidad", abrir_comunidad),
    ("📊 Mostrar Resumen", mostrar_resumen),
    ("💬 Soporte Técnico", abrir_chat_soporte),
    ("🚪 Salir", salir)
]

for texto, comando in botones:
    tk.Button(
        ventana, 
        text=texto, 
        width=30, 
        height=2, 
        bg="#a8dadc", 
        fg="#1d3557", 
        font=("Arial", 10, "bold"), 
        command=comando
    ).pack(pady=5)

ventana.mainloop()
