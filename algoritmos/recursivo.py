"""
RECURSIÓN - Sistema de Triaje de Emergencias
Clasifica pacientes por niveles de gravedad recursivamente.
Complejidad: O(n)
"""

def triaje_recursivo(pacientes, indice=0, niveles=None):
    """
    Clasifica recursivamente a los pacientes según su gravedad.
    
    Niveles de triaje:
    - CRÍTICO (8-10): Atención inmediata
    - URGENTE (5-7): Atención prioritaria
    - LEVE (1-4): Atención normal
    
    Args:
        pacientes (list): Lista de pacientes
        indice (int): Índice actual (recursión)
        niveles (dict): Acumulador de resultados
    
    Returns:
        dict: Pacientes clasificados por nivel
    """
    # Inicialización
    if niveles is None:
        niveles = {"CRÍTICO": [], "URGENTE": [], "LEVE": []}

    # CASO BASE: no hay más pacientes
    if indice >= len(pacientes):
        return niveles

    # CASO RECURSIVO: clasificar paciente actual
    paciente = pacientes[indice]
    gravedad = paciente["gravedad"]

    if gravedad >= 8:
        niveles["CRÍTICO"].append(paciente)
    elif gravedad >= 5:
        niveles["URGENTE"].append(paciente)
    else:
        niveles["LEVE"].append(paciente)

    # Llamada recursiva al siguiente paciente
    return triaje_recursivo(pacientes, indice + 1, niveles)


def mostrar_triaje(niveles):
    """Muestra el resultado del triaje"""
    print("\n🚨 SISTEMA DE TRIAJE (Clasificación recursiva)")
    print("="*50)
    iconos = {"CRÍTICO": "🔴", "URGENTE": "🟡", "LEVE": "🟢"}
    for nivel, pacientes in niveles.items():
        print(f"\n{iconos[nivel]} {nivel} ({len(pacientes)} pacientes):")
        for p in pacientes:
            print(f"   • {p['nombre']:15} | Gravedad: {p['gravedad']}/10 | {p['especialidad']}")