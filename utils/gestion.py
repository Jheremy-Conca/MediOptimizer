"""
GESTIÓN INTERACTIVA - Registrar, listar y asignar manualmente
"""

from datos.hospital_data import ESPECIALIDADES


def registrar_paciente(pacientes):
    """Permite al usuario registrar un nuevo paciente"""
    print("\n➕ REGISTRAR NUEVO PACIENTE")
    print("-" * 40)

    nombre = input("👤 Nombre del paciente: ").strip()

    # Mostrar especialidades disponibles
    print("\n🏥 Especialidades disponibles:")
    for i, esp in enumerate(ESPECIALIDADES, 1):
        print(f"   {i}. {esp}")
    
    try:
        opcion = int(input("Elige especialidad (número): "))
        especialidad = ESPECIALIDADES[opcion - 1]
    except (ValueError, IndexError):
        print("⚠️  Opción inválida, se asignó 'General'")
        especialidad = "General"

    # Gravedad
    try:
        gravedad = int(input("🌡️  Gravedad (1-10): "))
        if not 1 <= gravedad <= 10:
            gravedad = 5
            print("⚠️  Valor fuera de rango, se asignó 5")
    except ValueError:
        gravedad = 5
        print("⚠️  Valor inválido, se asignó 5")

    # Generar ID automático
    nuevo_id = max([p["id"] for p in pacientes], default=100) + 1

    nuevo_paciente = {
        "id": nuevo_id,
        "nombre": nombre,
        "especialidad": especialidad,
        "gravedad": gravedad,
        "tiempo": 2
    }
    pacientes.append(nuevo_paciente)
    print(f"\n✅ Paciente '{nombre}' registrado con ID {nuevo_id}")


def registrar_doctor(doctores):
    """Permite al usuario registrar un nuevo doctor"""
    print("\n➕ REGISTRAR NUEVO DOCTOR")
    print("-" * 40)

    nombre = input("👨‍⚕️ Nombre del doctor: ").strip()

    print("\n🏥 Especialidades disponibles:")
    for i, esp in enumerate(ESPECIALIDADES, 1):
        print(f"   {i}. {esp}")
    
    try:
        opcion = int(input("Elige especialidad (número): "))
        especialidad = ESPECIALIDADES[opcion - 1]
    except (ValueError, IndexError):
        print("⚠️  Opción inválida, se asignó 'General'")
        especialidad = "General"

    nuevo_id = max([d["id"] for d in doctores], default=0) + 1

    nuevo_doctor = {
        "id": nuevo_id,
        "nombre": nombre,
        "especialidad": especialidad,
        "disponible": True
    }
    doctores.append(nuevo_doctor)
    print(f"\n✅ Doctor '{nombre}' registrado con ID {nuevo_id}")


def listar_pacientes(pacientes):
    """Muestra todos los pacientes registrados"""
    print("\n📋 LISTA DE PACIENTES")
    print("=" * 50)
    if not pacientes:
        print("   (No hay pacientes registrados)")
        return
    for p in pacientes:
        print(f"   ID {p['id']} | {p['nombre']:18} | {p['especialidad']:14} | Gravedad: {p['gravedad']}/10")


def listar_doctores(doctores):
    """Muestra todos los doctores registrados"""
    print("\n👨‍⚕️ LISTA DE DOCTORES")
    print("=" * 50)
    if not doctores:
        print("   (No hay doctores registrados)")
        return
    for d in doctores:
        estado = "🟢 Disponible" if d["disponible"] else "🔴 Ocupado"
        print(f"   ID {d['id']} | {d['nombre']:18} | {d['especialidad']:14} | {estado}")


def asignar_manual(pacientes, doctores):
    """Permite al usuario asignar MANUALMENTE un doctor a un paciente"""
    print("\n🔧 ASIGNACIÓN MANUAL")
    print("=" * 50)

    if not pacientes or not doctores:
        print("⚠️  Necesitas pacientes y doctores registrados")
        return

    # Mostrar pacientes
    listar_pacientes(pacientes)
    try:
        id_paciente = int(input("\n👉 ID del paciente a atender: "))
        paciente = next(p for p in pacientes if p["id"] == id_paciente)
    except (ValueError, StopIteration):
        print("❌ Paciente no encontrado")
        return

    # Mostrar doctores disponibles
    print("\n👨‍⚕️ Doctores disponibles:")
    disponibles = [d for d in doctores if d["disponible"]]
    if not disponibles:
        print("   ⚠️  No hay doctores disponibles")
        return
    for d in disponibles:
        # Marcar si coincide la especialidad
        coincide = "⭐" if d["especialidad"] == paciente["especialidad"] else "  "
        print(f"   {coincide} ID {d['id']} | {d['nombre']:18} | {d['especialidad']}")

    try:
        id_doctor = int(input("\n👉 ID del doctor a asignar: "))
        doctor = next(d for d in disponibles if d["id"] == id_doctor)
    except (ValueError, StopIteration):
        print("❌ Doctor no encontrado o no disponible")
        return

    # Advertencia si no coincide especialidad
    if doctor["especialidad"] != paciente["especialidad"] and doctor["especialidad"] != "General":
        print(f"\n⚠️  ADVERTENCIA: {doctor['nombre']} es {doctor['especialidad']}")
        print(f"   pero el paciente necesita {paciente['especialidad']}")
        confirmar = input("   ¿Asignar de todas formas? (s/n): ").lower()
        if confirmar != "s":
            print("❌ Asignación cancelada")
            return

    # Realizar asignación
    doctor["disponible"] = False
    print(f"\n✅ ASIGNACIÓN EXITOSA")
    print(f"   👤 Paciente: {paciente['nombre']} (Gravedad {paciente['gravedad']})")
    print(f"   👨‍⚕️ Doctor:   {doctor['nombre']} ({doctor['especialidad']})")


def liberar_doctor(doctores):
    """Libera a un doctor ocupado (terminó de atender)"""
    print("\n🔓 LIBERAR DOCTOR")
    print("=" * 50)
    ocupados = [d for d in doctores if not d["disponible"]]
    if not ocupados:
        print("   ✅ Todos los doctores están disponibles")
        return

    print("Doctores ocupados:")
    for d in ocupados:
        print(f"   ID {d['id']} | {d['nombre']} ({d['especialidad']})")

    try:
        id_doctor = int(input("\n👉 ID del doctor a liberar: "))
        doctor = next(d for d in ocupados if d["id"] == id_doctor)
        doctor["disponible"] = True
        print(f"✅ {doctor['nombre']} ahora está disponible")
    except (ValueError, StopIteration):
        print("❌ Doctor no encontrado")


def eliminar_paciente(pacientes):
    """Elimina un paciente (fue dado de alta)"""
    print("\n🏥 DAR DE ALTA A PACIENTE")
    print("=" * 50)
    listar_pacientes(pacientes)
    if not pacientes:
        return
    try:
        id_paciente = int(input("\n👉 ID del paciente a dar de alta: "))
        paciente = next(p for p in pacientes if p["id"] == id_paciente)
        pacientes.remove(paciente)
        print(f"✅ {paciente['nombre']} fue dado de alta")
    except (ValueError, StopIteration):
        print("❌ Paciente no encontrado")