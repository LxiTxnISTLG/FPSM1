estudiantes = {}

def agregar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    notas = []

    while True:
        entrada = input("Ingresa una nota (o escribe 'fin' para terminar): ")
        if entrada.lower() == 'fin':
            break
        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("La nota debe estar entre 0 y 10.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

    estudiantes[nombre] = notas

def mostrar_estudiantes():
    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.")
        return

    print("Estudiantes registrados:")
    for nombre, notas in estudiantes.items():
        print(f"{nombre}: {notas} (Promedio: {sum(notas)/len(notas) if len(notas) > 0 else 0})")

def promedio_general():
    total_notas = 0
    total_estudiantes = 0

    for notas in estudiantes.values():
        total_notas += sum(notas)
        total_estudiantes += len(notas)

    if total_estudiantes == 0:
        return 0

    return total_notas / total_estudiantes

def actualizar_calificaciones():
    nombre = input("Ingrese el nombre del estudiante a buscar: ")
    if nombre in estudiantes:
        print(f"Calificaciones actuales de {nombre}: {estudiantes[nombre]}")
        agregar_estudiante()
    else:
        print("Estudiante no encontrado.")

def main():
    while True:
        print("\nSistema de Registro")
        print("1). Agregar estudiante")
        print("2). Mostrar estudiantes")
        print("3). Promedio general")
        print("4). Actualizar calificaciones")
        print("5). Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_estudiante()
        elif opcion == "2":
            mostrar_estudiantes()
        elif opcion == "3":
            promedio = promedio_general()
            print(f"El promedio general de todas las calificaciones es: {promedio}")
        elif opcion == "4":
            actualizar_calificaciones()
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, por favor elige nuevamente.")

main()