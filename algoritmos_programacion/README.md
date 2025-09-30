# 📚 Algoritmos y Programación - Guía Técnica

**Curso:** Algoritmos y Programación  
**Programa:** Tecnología en Desarrollo de Software - ECBTI  
**Institución:** Universidad Nacional Abierta y a Distancia (UNAD)

## 📖 Guía de Estudio

Esta es la **guía técnica detallada** del curso, organizada por niveles de complejidad progresiva. Cada nivel incluye ejercicios específicos con documentación completa de conceptos y objetivos de aprendizaje.

## 🗂️ Estructura de Niveles

### 📁 **Organización por Complejidad Creciente:**

```
📚 algoritmos_programacion/
├── 🔰 01_fundamentos/          # Variables, I/O, operaciones básicas
├── 🔀 02_condicionales/        # if-else, lógica de decisión
├── 🔄 03_ciclos_y_listas/      # for, while, estructuras de datos
└── ⚙️ 04_funciones/            # Programación modular y funciones
```

> **💡 Tip de Estudio:** Sigue el orden numérico. Cada nivel construye sobre los conceptos del anterior.

## 🎯 Progresión Técnica de Aprendizaje

| Nivel | Conceptos Clave | Ejercicios | Complejidad |
|-------|----------------|------------|-------------|
| **🔰 01** | Variables, I/O, operaciones matemáticas | 4 archivos | ⭐ Básico |
| **🔀 02** | if-else, validación, operadores lógicos | 4 archivos | ⭐⭐ Intermedio |
| **🔄 03** | for, while, listas, diccionarios, sistemas | 3 archivos | ⭐⭐⭐ Avanzado |
| **⚙️ 04** | Funciones, parámetros, modularización | 1 archivo | ⭐⭐⭐⭐ Experto |

## 💼 Casos de Estudio Empresariales

### 🛒 **E-commerce y Retail**
- **Black Friday Byte** (03_ciclos): Sistema de ventas con descuentos por categoría
- **Sports Store** (02_condicionales): Gestión de promociones por días

### 🍽️ **Industria de Servicios**  
- **Restaurante Doña Pancha** (03_ciclos): Sistema integral de propinas y facturación
- **Encuestas Netflix** (03_ciclos): Análisis estadístico de comportamiento

### 🏥 **Sector Salud**
- **Clasificador de Diabetes** (04_funciones): Diagnóstico automatizado por glucosa

### 📊 **Análisis de Datos**
- **Gastos Mensuales** (01_fundamentos): Cálculo de promedios y totales
- **Encuestas** (03_ciclos): Recolección y procesamiento estadístico

## 🔧 Tecnologías y Conceptos Implementados

### **Nivel Básico** 🔰
```python
# Variables y tipos de datos
nombre = "Samuel"           # string
edad = 25                   # int  
promedio = 85.5            # float

# Entrada y salida
valor = input("Ingresa un número: ")
print(f"El resultado es: {resultado}")
```

### **Nivel Intermedio** 🔀
```python
# Estructuras condicionales
if condicion:
    # Acción si verdadero
elif otra_condicion:
    # Acción alternativa
else:
    # Acción por defecto

# Validación de datos
while not entrada.isdigit():
    entrada = input("Ingresa un número válido: ")
```

### **Nivel Avanzado** 🔄
```python
# Ciclos y estructuras de datos
for i in range(25):  # Ciclo FOR con rango definido
    # Procesamiento de datos

while continuar:     # Ciclo WHILE con condición dinámica
    # Lógica de negocio
    
# Listas y diccionarios
datos = []
resumen = {'total': 0, 'promedio': 0}
```

### **Nivel Experto** ⚙️
```python
# Funciones modulares
def clasificar_glucosa(nivel):
    """Clasifica nivel de glucosa según criterios médicos"""
    if nivel <= 75:
        return "Hipoglucemia"
    elif nivel < 105:
        return "Normal"
    # ... más lógica
    
# Llamada a función
resultado = clasificar_glucosa(90)
```

## 📊 Mapeo de Fases Originales

| Fase Original del Curso | Nueva Organización | Enfoque Temático |
|------------------------|-------------------|------------------|
| `ejercicios_grupo_4` | **01_fundamentos** | Variables, operaciones básicas |
| `ejercicios_grupo4_tarea3` | **02_condicionales** | Decisiones y validación |
| `ejercicio_grupo3_tarea4` | **03_ciclos_y_listas + 04_funciones** | Estructuras avanzadas |

## 🎓 Objetivos de Aprendizaje por Nivel

Al completar cada nivel, deberías dominar:

### 🔰 **01_fundamentos**
- ✅ Declarar variables de diferentes tipos
- ✅ Realizar operaciones matemáticas
- ✅ Manejar entrada/salida de datos
- ✅ Estructurar código básico

### 🔀 **02_condicionales**  
- ✅ Implementar lógica de decisión
- ✅ Validar entrada de usuarios
- ✅ Usar operadores de comparación
- ✅ Aplicar reglas de negocio

### 🔄 **03_ciclos_y_listas**
- ✅ Controlar flujo con ciclos
- ✅ Manipular listas y diccionarios
- ✅ Implementar acumuladores
- ✅ Crear sistemas complejos

### ⚙️ **04_funciones**
- ✅ Diseñar funciones modulares
- ✅ Manejar parámetros y retornos
- ✅ Documentar código profesionalmente
- ✅ Aplicar principios de reutilización

## 🚀 Cómo Estudiar con Este Material

1. **📖 Lee el README** de cada nivel antes de ver el código
2. **💻 Ejecuta los ejemplos** y experimenta con diferentes valores  
3. **🔍 Analiza la lógica** paso a paso en cada ejercicio
4. **✏️ Modifica el código** para entender su funcionamiento
5. **🎯 Practica** creando ejercicios similares

---

*💡 **Recuerda:** La programación se aprende practicando. ¡No tengas miedo de experimentar y hacer errores!*