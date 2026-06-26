"""
ALGORITMO VORAZ - Asignación de Doctores a Pacientes
Asigna el doctor disponible de la especialidad requerida al paciente
más grave primero (estrategia voraz).
Complejidad: O(n * m)
"""

def asignar_doctores_voraz(pacientes, doctores):
    """
    Asigna doctores a pacientes priorizando los más graves.
    
    Estrategia voraz: 
    - Ordena pacientes por gravedad (más grave primero)
    - Asigna el primer doctor disponible de la especialidad
    
    Args:
        pacientes (list): Lista de pacientes
        doctores (list): Lista de doctores
    
    Returns:
        tuple: (asignaciones, pacientes_sin_atender)
    """
    # Copiar para no modificar originales
    doctores_disponibles = [dict(d) for d in doctores]

    # ESTRATEGIA VORAZ: ordenar por gravedad (mayor primero)
    pacientes_ordenados = sorted(
        pacientes, key=lambda p: p["gravedad"], reverse=True
    )

    asignaciones = []
    sin_atender = []

    for paciente in pacientes_ordenados:
        asignado = False
        # Buscar doctor de la especialidad requerida
        for doctor in doctores_disponibles:
            if (doctor["disponible"] and 
                (doctor["especialidad"] == paciente["especialidad"] or 
                 doctor["especialidad"] == "General")):
                # Asignar (decisión voraz)
                asignaciones.append({
                    "paciente": paciente,
                    "doctor": doctor
                })
                doctor["disponible"] = False  # Doctor ocupado
                asignado = True
                break

        if not asignado:
            sin_atender.append(paciente)

    return asignaciones, sin_atender


def mostrar_asignaciones(asignaciones, sin_atender):
    """Muestra las asignaciones realizadas"""
    print("\n👨‍⚕️ ASIGNACIÓN DE DOCTORES (Algoritmo Voraz)")
    print("="*50)
    for a in asignaciones:
        p = a["paciente"]
        d = a["doctor"]
        print(f"✅ {p['nombre']:15} (Grav.{p['gravedad']}) → {d['nombre']} ({d['especialidad']})")

    if sin_atender:
        print(f"\n⚠️  Pacientes en espera ({len(sin_atender)}):")
        for p in sin_atender:
            print(f"   ⏳ {p['nombre']} - Necesita: {p['especialidad']}")