# SEMANA 5
# Función para agregar un estudiante al registro
def agregar_estudiante(registro, nombre, edad, calificacion, esta_activo):
    estudiante = {
        'nombre': nombre,
        'edad': edad,
        'calificacion': calificacion,
        'esta_activo': esta_activo
    }
    registro.append(estudiante)

# Función para mostrar todos los estudiantes en el registro
def mostrar_estudiantes(registro):
    for estudiante in registro:
        estado = 'Activo' if estudiante['esta_activo'] else 'Inactivo'
        print(f"Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}, Calificación: {estudiante['calificacion']}, Estado: {estado}")

# Función principal
def main():
    registro_estudiantes = []
    
    # Agregar estudiantes al registro
    agregar_estudiante(registro_estudiantes, 'Juan Pérez', 20, 85.5, True)
    agregar_estudiante(registro_estudiantes, 'Ana Gómez', 22, 90.0, False)
    agregar_estudiante(registro_estudiantes, 'Luis Martínez', 19, 78.0, True)
    
    # Mostrar todos los estudiantes
    print("Registro de Estudiantes:")
    mostrar_estudiantes(registro_estudiantes)

# Ejecutar la función principal
if __name__ == "__main__":
    main()