"""
ANÁLISIS DE COMPLEJIDAD - Medir tiempos de ejecución
"""

import time


def medir_tiempo(funcion, *args, **kwargs):
    """
    Mide el tiempo de ejecución de una función.
    
    Returns:
        tuple: (resultado, tiempo_en_segundos)
    """
    inicio = time.perf_counter()
    resultado = funcion(*args, **kwargs)
    fin = time.perf_counter()
    return resultado, (fin - inicio)


def analizar_algoritmos(pacientes, doctores):
    """Analiza el rendimiento de los algoritmos principales"""
    from algoritmos.voraces import asignar_doctores_voraz
    from algoritmos.divide_venceras import ordenar_por_prioridad
    from algoritmos.recursivo import triaje_recursivo

    print("\n⚡ ANÁLISIS DE COMPLEJIDAD")
    print("="*50)

    # Voraz
    _, t_voraz = medir_tiempo(asignar_doctores_voraz, pacientes, doctores)
    print(f"🟢 Asignación Voraz:    O(n*m)     | {t_voraz*1000:.4f} ms")

    # Divide y vencerás
    _, t_merge = medir_tiempo(ordenar_por_prioridad, pacientes)
    print(f"🔵 Ordenar (MergeSort): O(n log n) | {t_merge*1000:.4f} ms")

    # Recursivo
    _, t_triaje = medir_tiempo(triaje_recursivo, pacientes)
    print(f"🟣 Triaje Recursivo:    O(n)       | {t_triaje*1000:.4f} ms")