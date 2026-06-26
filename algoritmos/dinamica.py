"""
PROGRAMACIÓN DINÁMICA - Distribución Óptima de Recursos Médicos
Problema de la Mochila aplicado: maximizar el beneficio (vidas salvadas)
con un presupuesto limitado.
Complejidad: O(n * presupuesto)
"""

def distribuir_recursos(presupuesto, recursos):
    """
    Distribuye recursos médicos para MAXIMIZAR el beneficio
    sin exceder el presupuesto (Programación Dinámica - Mochila 0/1).
    
    Args:
        presupuesto (int): Presupuesto disponible
        recursos (list): Lista de recursos con costo y beneficio
    
    Returns:
        tuple: (beneficio_maximo, recursos_seleccionados)
    """
    n = len(recursos)
    # Tabla DP: dp[i][w] = máximo beneficio con i recursos y presupuesto w
    dp = [[0] * (presupuesto + 1) for _ in range(n + 1)]

    # Llenar la tabla
    for i in range(1, n + 1):
        costo = recursos[i - 1]["costo"]
        beneficio = recursos[i - 1]["beneficio"]
        for w in range(presupuesto + 1):
            if costo <= w:
                dp[i][w] = max(
                    dp[i - 1][w],                       # No adquirir
                    beneficio + dp[i - 1][w - costo]    # Adquirir
                )
            else:
                dp[i][w] = dp[i - 1][w]

    # Reconstruir qué recursos se seleccionaron
    seleccionados = []
    w = presupuesto
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            seleccionados.append(recursos[i - 1])
            w -= recursos[i - 1]["costo"]

    return dp[n][presupuesto], seleccionados


def mostrar_recursos(beneficio_max, seleccionados, presupuesto):
    """Muestra la distribución óptima de recursos"""
    print("\n💊 DISTRIBUCIÓN ÓPTIMA DE RECURSOS (Prog. Dinámica)")
    print("="*50)
    print(f"💰 Presupuesto disponible: {presupuesto} unidades")
    print(f"🎯 Beneficio máximo (impacto): {beneficio_max} puntos")
    print("\n📦 Recursos a adquirir:")
    costo_total = 0
    for r in seleccionados:
        print(f"   ✓ {r['nombre']:20} | Costo: {r['costo']} | Beneficio: {r['beneficio']}")
        costo_total += r["costo"]
    print(f"\n   💵 Presupuesto usado: {costo_total}/{presupuesto}")