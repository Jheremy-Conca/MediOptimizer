"""
=====================================================
   🏥 MediOptimizer (VERSIÓN INTERACTIVA)
   Sistema Inteligente de Gestión Hospitalaria
=====================================================
"""

from algoritmos.recursivo import triaje_recursivo, mostrar_triaje
from algoritmos.divide_venceras import ordenar_por_prioridad, mostrar_prioridad
from algoritmos.voraces import asignar_doctores_voraz, mostrar_asignaciones
from algoritmos.dinamica import distribuir_recursos, mostrar_recursos
from algoritmos.backtracking import asignar_turnos, mostrar_horario
from utils.analisis_complejidad import analizar_algoritmos
from utils.gestion import (
    registrar_paciente, registrar_doctor, listar_pacientes,
    listar_doctores, asignar_manual, liberar_doctor, eliminar_paciente
)
from datos.hospital_data import (
    DOCTORES, PACIENTES, RECURSOS, PRESUPUESTO, TURNOS, DIAS
)


def menu():
    print("\n" + "=" * 50)
    print("   🏥 MEDIOPTIMIZER - GESTIÓN HOSPITALARIA 🏥")
    print("=" * 50)
    print("--- 📝 GESTIÓN ---")
    print(" 1. ➕ Registrar paciente")
    print(" 2. ➕ Registrar doctor")
    print(" 3. 📋 Ver pacientes")
    print(" 4. 👨‍⚕️ Ver doctores")
    print(" 5. 🔧 Asignar doctor MANUALMENTE")
    print(" 6. 🔓 Liberar doctor (terminó atención)")
    print(" 7. 🏥 Dar de alta a paciente")
    print("--- 🤖 ALGORITMOS AUTOMÁTICOS ---")
    print(" 8. 🚨 Triaje automático (Recursión)")
    print(" 9. 📋 Ordenar por prioridad (Divide y Vencerás)")
    print("10. ⚡ Asignación automática (Voraz)")
    print("11. 💊 Distribuir recursos (Prog. Dinámica)")
    print("12. 📅 Generar turnos (Backtracking)")
    print("13. 📊 Análisis de complejidad")
    print(" 0. ❌ Salir")
    print("=" * 50)


def main():
    print("\n🏥 Bienvenido al Sistema de Gestión Hospitalaria")
    
    while True:
        menu()
        opcion = input("👉 Elige una opción: ").strip()

        # --- GESTIÓN INTERACTIVA ---
        if opcion == "1":
            registrar_paciente(PACIENTES)
        elif opcion == "2":
            registrar_doctor(DOCTORES)
        elif opcion == "3":
            listar_pacientes(PACIENTES)
        elif opcion == "4":
            listar_doctores(DOCTORES)
        elif opcion == "5":
            asignar_manual(PACIENTES, DOCTORES)
        elif opcion == "6":
            liberar_doctor(DOCTORES)
        elif opcion == "7":
            eliminar_paciente(PACIENTES)

        # --- ALGORITMOS AUTOMÁTICOS ---
        elif opcion == "8":
            niveles = triaje_recursivo(PACIENTES)
            mostrar_triaje(niveles)
        elif opcion == "9":
            ordenados = ordenar_por_prioridad(PACIENTES)
            mostrar_prioridad(ordenados)
        elif opcion == "10":
            # Reactivar doctores para la demo automática
            for d in DOCTORES:
                d["disponible"] = True
            asignaciones, sin_atender = asignar_doctores_voraz(PACIENTES, DOCTORES)
            mostrar_asignaciones(asignaciones, sin_atender)
        elif opcion == "11":
            beneficio, recursos = distribuir_recursos(PRESUPUESTO, RECURSOS)
            mostrar_recursos(beneficio, recursos, PRESUPUESTO)
        elif opcion == "12":
            horario = asignar_turnos(DOCTORES, DIAS, TURNOS)
            mostrar_horario(horario, DIAS, TURNOS)
        elif opcion == "13":
            analizar_algoritmos(PACIENTES, DOCTORES)

        elif opcion == "0":
            print("\n👋 ¡Gracias por usar MediOptimizer!")
            break
        else:
            print("⚠️  Opción no válida")

        input("\n⏎ Presiona ENTER para continuar...")


if __name__ == "__main__":
    main()