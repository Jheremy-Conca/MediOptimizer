# 🏥 MediOptimizer
### Sistema Inteligente de Gestión Hospitalaria

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Estado](https://img.shields.io/badge/Estado-Completado-28a745?style=for-the-badge)
![Curso](https://img.shields.io/badge/Curso-Análisis%20de%20Algoritmos-orange?style=for-the-badge)
![UPN](https://img.shields.io/badge/UPN-Ingeniería-red?style=for-the-badge)
![Licencia](https://img.shields.io/badge/Licencia-MIT-informational?style=for-the-badge)

*Optimización de recursos hospitalarios mediante 8 estrategias algorítmicas fundamentales*

</div>

---

## 📌 Tabla de Contenidos

- [Descripción](#-descripción)
- [Objetivos](#-objetivos)
- [Algoritmos Implementados](#-algoritmos-implementados)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Requisitos](#-requisitos)
- [Instalación y Uso](#-instalación-y-uso)
- [Funcionalidades](#-funcionalidades)
- [Demostración](#-demostración)
- [Tecnologías](#-tecnologías)
- [Autor](#-autor)

---

## 📋 Descripción

**MediOptimizer** es un sistema inteligente que resuelve problemas reales de gestión hospitalaria, desarrollado para el curso de **Análisis de Algoritmos y Estrategias de Programación** de la *Universidad Privada del Norte*.

El sistema aplica **8 técnicas algorítmicas** sobre un entorno hospitalario simulado, abarcando desde el triaje de pacientes críticos hasta la distribución óptima de recursos médicos y el procesamiento paralelo de redes de hospitales.

> 💡 **Impacto:** Cada algoritmo responde a un problema concreto del mundo real en el ámbito de la salud, demostrando cómo la teoría algorítmica se traduce en soluciones de alto valor social.

---

## 🎯 Objetivos

| # | Objetivo | Técnica Aplicada |
|---|----------|-----------------|
| 1 | Clasificar pacientes según gravedad (triaje) | Recursión |
| 2 | Localizar pacientes eficientemente | Búsqueda Binaria |
| 3 | Ordenar lista de atención por prioridad | Divide y Vencerás |
| 4 | Asignar doctores disponibles al instante | Algoritmos Voraces |
| 5 | Generar turnos sin conflictos de horario | Backtracking |
| 6 | Distribuir medicamentos de forma óptima | Programación Dinámica |
| 7 | Estimar tiempos de espera con incertidumbre | Monte Carlo |
| 8 | Procesar múltiples hospitales en paralelo | Algoritmos Paralelos |

---

## 🧠 Algoritmos Implementados

### 1. 🔁 Recursión — Triaje de Emergencias
Clasifica automáticamente a los pacientes en niveles de prioridad (crítico, urgente, normal) recorriendo la lista de forma recursiva según sus síntomas y signos vitales.
- **Complejidad:** O(n)
- **Archivo:** `algoritmos/recursivo.py`

---

### 2. 🔍 Búsqueda Binaria — Localización de Pacientes
Permite encontrar un paciente en la base de datos ordenada en tiempo logarítmico, ideal para hospitales con alta rotación de pacientes.
- **Complejidad:** O(log n)
- **Archivo:** `algoritmos/busqueda.py`

---

### 3. ⚔️ Divide y Vencerás — Ordenamiento por Prioridad
Implementa **Merge Sort** para ordenar la cola de atención completa según nivel de gravedad, garantizando que los casos más críticos sean atendidos primero.
- **Complejidad:** O(n log n)
- **Archivo:** `algoritmos/divide_venceras.py`

---

### 4. 💚 Algoritmos Voraces — Asignación de Doctores
Asigna al médico disponible más adecuado para cada paciente de forma inmediata, maximizando la ocupación del personal médico sin retrocesos.
- **Complejidad:** O(n·m)
- **Archivo:** `algoritmos/voraces.py`

---

### 5. 🗓️ Backtracking — Generación de Turnos
Genera horarios de guardia sin solapamientos ni conflictos, explorando combinaciones de asignación y retrocediendo cuando detecta incompatibilidades.
- **Complejidad:** O(d^t)
- **Archivo:** `algoritmos/backtracking.py`

---

### 6. 💊 Programación Dinámica — Distribución de Recursos
Resuelve el problema de la **mochila 0/1** para distribuir medicamentos y equipos limitados entre pacientes, maximizando el beneficio clínico total.
- **Complejidad:** O(n·W)
- **Archivo:** `algoritmos/dinamica.py`

---

### 7. 🎲 Algoritmos Probabilísticos — Simulación Monte Carlo
Simula miles de escenarios de atención para estimar con alta precisión los tiempos de espera esperados bajo condiciones de incertidumbre real.
- **Complejidad:** O(s·n)
- **Archivo:** `algoritmos/probabilistico.py`

---

### 8. ⚡ Algoritmos Paralelos — Red de Hospitales
Procesa simultáneamente múltiples hospitales en paralelo usando `multiprocessing`, reduciendo drásticamente el tiempo total de análisis de la red.
- **Complejidad:** Depende del hardware
- **Archivo:** `algoritmos/paralelos.py`

---

## 📁 Estructura del Proyecto

```
MediOptimizer/
│
├── main.py                         # Programa principal — menú interactivo
│
├── algoritmos/
│   ├── recursivo.py                # Triaje de emergencias (Recursión)
│   ├── busqueda.py                 # Búsqueda binaria y lineal
│   ├── divide_venceras.py          # Ordenamiento Merge Sort
│   ├── voraces.py                  # Asignación greedy de doctores
│   ├── backtracking.py             # Generación de turnos sin conflictos
│   ├── dinamica.py                 # Distribución de recursos (Mochila 0/1)
│   ├── probabilistico.py           # Simulación Monte Carlo
│   └── paralelos.py                # Procesamiento paralelo — red hospitalaria
│
├── utils/
│   ├── analisis_complejidad.py     # Medición y comparación de tiempos
│   └── gestion.py                  # Módulo de gestión interactiva
│
├── datos/
│   └── hospital_data.py            # Datos de prueba del hospital
│
└── README.md
```

---

## ⚙️ Requisitos

- **Python** 3.8 o superior
- **Sin dependencias externas** — solo módulos de la biblioteca estándar

```
multiprocessing   random   time   copy   math
```

---

## 🚀 Instalación y Uso

### 1. Clonar el repositorio

```bash
git clone https://github.com/Jheremy-Conca/MediOptimizer.git
```

### 2. Entrar a la carpeta

```bash
cd MediOptimizer
```

### 3. Ejecutar el programa

```bash
python main.py
```

---

## 🎮 Funcionalidades

### 📝 Gestión Interactiva

| Opción | Acción |
|--------|--------|
| ➕ | Registrar paciente nuevo |
| ➕ | Registrar doctor |
| 📋 | Listar pacientes / doctores |
| 🔧 | Asignar doctor manualmente |
| 🔓 | Liberar doctor |
| 🏥 | Dar de alta a paciente |

### 🤖 Algoritmos Automáticos

| Opción | Algoritmo |
|--------|-----------|
| 🚨 | Triaje automático (Recursión) |
| 📋 | Ordenar por prioridad (Merge Sort) |
| ⚡ | Asignación automática de doctores (Voraz) |
| 💊 | Distribución de recursos (Dinámica) |
| 📅 | Generar turnos (Backtracking) |
| 🔍 | Buscar paciente (Búsqueda Binaria) |
| 🎲 | Simulación de tiempos (Monte Carlo) |
| 📊 | Análisis de complejidad comparativo |

---

## 📸 Demostración

```
==================================================
     🏥  MEDIOPTIMIZER - GESTIÓN HOSPITALARIA  🏥
==================================================

  --- 📝 GESTIÓN MANUAL ---
  1.  ➕  Registrar paciente
  2.  ➕  Registrar doctor
  3.  📋  Listar pacientes
  4.  📋  Listar doctores
  5.  🔧  Asignar doctor manualmente
  6.  🔓  Liberar doctor
  7.  🏥  Dar de alta a paciente

  --- 🤖 ALGORITMOS AUTOMÁTICOS ---
  8.  🚨  Triaje automático        (Recursión)
  9.  📋  Ordenar por prioridad    (Divide y Vencerás)
  10. ⚡  Asignar doctores         (Voraz)
  11. 💊  Distribuir recursos      (Programación Dinámica)
  12. 📅  Generar turnos           (Backtracking)
  13. 🔍  Buscar paciente          (Búsqueda Binaria)
  14. 🎲  Simular tiempos          (Monte Carlo)
  15. ⚡  Red de hospitales        (Paralelos)
  16. 📊  Análisis de complejidad

  0.  🚪  Salir

==================================================
Seleccione una opción:
```

---

## 🛠️ Tecnologías

| Componente | Detalle |
|------------|---------|
| **Lenguaje** | Python 3.8+ |
| **Paralelismo** | `multiprocessing` (stdlib) |
| **Simulación** | `random` (stdlib) |
| **Medición** | `time` (stdlib) |
| **IDE recomendado** | VS Code / PyCharm |

---



<div align="center">

⭐ **Si este proyecto te fue útil, dale una estrella al repositorio** ⭐

</div>
