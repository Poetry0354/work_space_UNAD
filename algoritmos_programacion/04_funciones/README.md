# ⚙️ 04 - Funciones

**Fase Original:** `ejercicio_grupo3_tarea4` (Ejercicio 4)

## 📝 Descripción
Esta carpeta contiene ejercicios especializados en el **desarrollo y uso de funciones** como unidades modulares de código. Se enfoca en la creación de funciones que reciben parámetros, procesan datos y retornan resultados, aplicando conceptos de programación modular y reutilización de código.

## 🎯 Conceptos Tratados
- **Definición de funciones** con `def`
- **Parámetros y argumentos** de entrada
- **Valores de retorno** con `return`
- **Programación modular** y reutilización
- **Validación de datos** dentro de funciones
- **Documentación de funciones** (docstrings)
- **Lógica de clasificación** y categorización
- **Estructuras condicionales** dentro de funciones

## 📁 Ejercicios Incluidos

### `ejercicio4.py` - **Sistema de Clasificación de Diabetes**
- **Objetivo:** Crear función para clasificar pacientes según niveles de glucosa
- **Conceptos:** Función con parámetro, condicionales múltiples, clasificación médica
- **Parámetro:** `nivel_glucosa` (float)
- **Retorno:** Clasificación médica (string)

#### 🏥 Criterios de Clasificación Médica:
| Nivel de Glucosa | Criterio Médico |
|------------------|-----------------|
| ≤ 75 ml | **Hipoglucemia** |
| 76-104 ml | **Normal** |
| 105-126 ml | **Prediabetes** |
| > 126 ml | **Diabetes** |

#### 🔧 Funciones Implementadas:
- **`solicitar_nivel_glucosa()`**: Validación de entrada de datos
- **`clasificar_diabetes(nivel_glucosa)`**: Función principal de clasificación
- **`mostrar_resultado(nivel, clasificacion)`**: Presentación formateada de resultados
- **`main()`**: Función principal que controla el flujo del programa

## 🏥 Caso de Uso: Sistema Médico
El ejercicio simula un **sistema de diagnóstico automatizado** que:
- Recibe datos del paciente (nivel de glucosa)
- Aplica criterios médicos establecidos
- Clasifica automáticamente el estado del paciente
- Presenta resultados de manera clara y profesional

## 🏆 Objetivos de Aprendizaje
Al completar este ejercicio, el estudiante debe ser capaz de:
1. **Diseñar funciones** con propósitos específicos
2. **Implementar parámetros** y valores de retorno
3. **Aplicar lógica de clasificación** compleja
4. **Validar datos** de entrada eficientemente
5. **Documentar funciones** con docstrings
6. **Estructurar programas** de manera modular
7. **Manejar múltiples condiciones** de forma organizada
8. **Crear interfaces** de usuario funcionales

## 🎓 Principios de Programación Aplicados
- **DRY** (Don't Repeat Yourself) - Evitar código duplicado
- **SRP** (Single Responsibility Principle) - Una función, un propósito
- **Modularidad** - Código organizado en componentes reutilizables
- **Legibilidad** - Código auto-documentado y fácil de entender

## 🔧 Habilidades Desarrolladas
- **Pensamiento modular** para dividir problemas complejos
- **Diseño de interfaces** de función claras
- **Implementación de lógica** de clasificación
- **Validación robusta** de entrada de datos
- **Documentación técnica** de código

## 💡 Aplicaciones Reales
Este tipo de programación funcional es fundamental en:
- **Sistemas médicos** de diagnóstico
- **Aplicaciones de clasificación** automática
- **Sistemas de validación** de datos
- **APIs** y servicios web
- **Bibliotecas** de código reutilizable

---
*Ejercicio 4 del Grupo 3 - Curso de Algoritmos y Programación - UNAD*