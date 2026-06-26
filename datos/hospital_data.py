"""
Datos del hospital - Ahora se pueden MODIFICAR en tiempo real
"""

# Listas que el usuario irá llenando
DOCTORES = [
    {"id": 1, "nombre": "Dr. García",   "especialidad": "Cardiología",   "disponible": True},
    {"id": 2, "nombre": "Dra. López",   "especialidad": "Pediatría",     "disponible": True},
    {"id": 3, "nombre": "Dr. Martínez", "especialidad": "Traumatología", "disponible": True},
]

PACIENTES = [
    {"id": 101, "nombre": "Juan Pérez", "especialidad": "Cardiología", "gravedad": 9, "tiempo": 3},
    {"id": 102, "nombre": "Ana Soto",   "especialidad": "Pediatría",   "gravedad": 5, "tiempo": 2},
]

# Especialidades disponibles
ESPECIALIDADES = ["Cardiología", "Pediatría", "Traumatología", "General", "Neurología"]

# Recursos (se mantienen para el ejercicio de PD)
RECURSOS = [
    {"nombre": "Ventilador",        "costo": 5, "beneficio": 90},
    {"nombre": "Monitor cardíaco",  "costo": 3, "beneficio": 60},
    {"nombre": "Desfibrilador",     "costo": 4, "beneficio": 80},
    {"nombre": "Camas UCI",         "costo": 6, "beneficio": 95},
    {"nombre": "Equipo Rayos X",    "costo": 2, "beneficio": 40},
]

PRESUPUESTO = 12
TURNOS = ["Mañana", "Tarde", "Noche"]
DIAS = ["Lunes", "Martes", "Miércoles"]