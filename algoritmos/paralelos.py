"""
ALGORITMOS PARALELOS - Procesar múltiples hospitales simultáneamente
Usa multiprocessing para analizar varios hospitales a la vez.
"""

from multiprocessing import Pool
from algoritmos.voraces import asignar_doctores_voraz


def procesar_hospital(datos_hospital):
    """
    Procesa la asignación de un hospital.
    
    Args:
        datos_hospital (dict): {nombre, pacientes, doctores}
    
    Returns:
        dict: Estadísticas del hospital
    """
    nombre = datos_hospital["nombre"]
    pacientes = datos_hospital["pacientes"]
    doctores = datos_hospital["doctores"]

    asignaciones, sin_atender = asignar_doctores_voraz(pacientes, doctores)

    return {
        "hospital": nombre,
        "atendidos": len(asignaciones),
        "en_espera": len(sin_atender),
        "total": len(pacientes)
    }


def procesar_red_hospitales(hospitales):
    """
    Procesa una red de hospitales EN PARALELO.
    
    Args:
        hospitales (list): Lista de hospitales con sus datos
    
    Returns:
        list: Estadísticas de cada hospital
    """
    with Pool() as pool:
        resultados = pool.map(procesar_hospital, hospitales)
    return resultados


def mostrar_red(resultados):
    """Muestra estadísticas de la red hospitalaria"""
    print("\n🏥 RED HOSPITALARIA (Procesamiento Paralelo)")
    print("="*50)
    total_atendidos = 0
    for r in resultados:
        porcentaje = (r["atendidos"] / r["total"] * 100) if r["total"] else 0
        print(f"🏥 {r['hospital']:15} | Atendidos: {r['atendidos']}/{r['total']} ({porcentaje:.0f}%)")
        total_atendidos += r["atendidos"]
    print(f"\n📊 Total de pacientes atendidos en la red: {total_atendidos}")