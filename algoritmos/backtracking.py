"""
BACKTRACKING - Asignación de Turnos sin Conflictos
Asigna turnos a doctores garantizando que:
- Cada turno tenga un doctor
- Ningún doctor trabaje dos turnos el mismo día
Complejidad: O(d^t) en el peor caso
"""

def asignar_turnos(doctores, dias, turnos):
    """
    Asigna doctores a turnos usando Backtracking.
    Garantiza que ningún doctor tenga dos turnos el mismo día.
    
    Args:
        doctores (list): Lista de doctores
        dias (list): Lista de días
        turnos (list): Lista de turnos por día
    
    Returns:
        dict o None: Horario asignado o None si no hay solución
    """
    # Horario: {(día, turno): doctor}
    horario = {}
    # Control: qué doctor trabaja qué día
    doctor_dia = {}  # {(doctor_id, día): True}

    # Lista de todas las casillas a llenar
    casillas = [(dia, turno) for dia in dias for turno in turnos]

    def backtrack(indice):
        # CASO BASE: todas las casillas asignadas
        if indice == len(casillas):
            return True

        dia, turno = casillas[indice]

        # Probar cada doctor
        for doctor in doctores:
            doc_id = doctor["id"]
            # RESTRICCIÓN: el doctor no debe trabajar ya ese día
            if (doc_id, dia) not in doctor_dia:
                # Asignar (intentar)
                horario[(dia, turno)] = doctor
                doctor_dia[(doc_id, dia)] = True

                # Recursión: intentar siguiente casilla
                if backtrack(indice + 1):
                    return True

                # BACKTRACK: deshacer si no funcionó
                del horario[(dia, turno)]
                del doctor_dia[(doc_id, dia)]

        return False  # No se pudo asignar

    if backtrack(0):
        return horario
    return None


def mostrar_horario(horario, dias, turnos):
    """Muestra el horario de turnos asignado"""
    print("\n📅 HORARIO DE TURNOS (Backtracking)")
    print("="*50)
    if horario is None:
        print("❌ No se encontró una asignación válida")
        return

    # Encabezado
    print(f"{'TURNO':<10}", end="")
    for dia in dias:
        print(f"{dia:<15}", end="")
    print()
    print("-"*50)

    # Filas por turno
    for turno in turnos:
        print(f"{turno:<10}", end="")
        for dia in dias:
            doctor = horario.get((dia, turno))
            nombre = doctor["nombre"] if doctor else "---"
            print(f"{nombre:<15}", end="")
        print()