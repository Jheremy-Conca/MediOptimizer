"""
DIVIDE Y VENCERÁS - Ordenar pacientes por prioridad (gravedad)
Usa Merge Sort para ordenar por nivel de gravedad descendente.
Complejidad: O(n log n)
"""

def ordenar_por_prioridad(pacientes):
    """
    Ordena los pacientes por gravedad (mayor a menor) usando Merge Sort.
    Los más graves se atienden primero.
    """
    if len(pacientes) <= 1:
        return pacientes

    # DIVIDIR
    medio = len(pacientes) // 2
    izquierda = ordenar_por_prioridad(pacientes[:medio])
    derecha = ordenar_por_prioridad(pacientes[medio:])

    # COMBINAR (vencer)
    return _merge(izquierda, derecha)


def _merge(izq, der):
    """Combina dos listas ordenadas por gravedad (descendente)"""
    resultado = []
    i = j = 0

    while i < len(izq) and j < len(der):
        # Mayor gravedad primero
        if izq[i]["gravedad"] >= der[j]["gravedad"]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1

    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    return resultado


def mostrar_prioridad(pacientes_ordenados):
    """Muestra los pacientes ordenados por prioridad"""
    print("\n📋 LISTA DE ATENCIÓN POR PRIORIDAD")
    print("="*50)
    for i, p in enumerate(pacientes_ordenados, 1):
        barra = "█" * p["gravedad"]
        print(f"{i}. {p['nombre']:15} [{barra:<10}] {p['gravedad']}/10")