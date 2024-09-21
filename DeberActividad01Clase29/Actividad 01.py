estudiantes = []

def menu():
    print("\nBienvenido al Sistema de Registro de Matrículas")
    print("1. Registrar nuevo estudiante")
    print("2. Mostrar estudiantes registrados")
    print("3. Actualizar información de un estudiante")
    print("4. Eliminar un estudiante")
    print("5. Salir")
    opcion = input("Elige una opción (1/2/3/4/5): ")
    return opcion

def registrar_estudiante():
    nombre = input("Ingresa el nombre del estudiante: ")
    edad = int(input("Ingresa la edad del estudiante: "))
    estudiante = {'nombre': nombre, 'edad': edad}
    estudiantes.append(estudiante)
    print(f"Estudiante {nombre} registrado con éxito.")
    
def mostrar_estudiantes():
    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.")
    else:
        print("Lista de estudiantes registrados:")
        for i, estudiante in enumerate(estudiantes, start=1):
            print(f"{i}. Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}")

def actualizar_estudiante():
    mostrar_estudiantes()
    if len(estudiantes) == 0:
        print("No hay estudiantes para actualizar.")
        return
    
    try:
        indice = int(input("Ingresa el número del estudiante que deseas actualizar: ")) - 1
        if 0 <= indice < len(estudiantes):
            estudiante = estudiantes[indice]
            print(f"Estudiante seleccionado: {estudiante['nombre']}")
            nuevo_nombre = input("Ingresa el nuevo nombre (o presiona Enter para no cambiarlo): ")
            nueva_edad = input("Ingresa la nueva edad (o presiona Enter para no cambiarla): ")

            if nuevo_nombre:
                estudiante['nombre'] = nuevo_nombre
            if nueva_edad:
                estudiante['edad'] = int(nueva_edad)

            print(f"Estudiante actualizado con éxito: {estudiante['nombre']}")
        else:
            print("Número de estudiante no válido.")
    except ValueError:
        print("Entrada inválida. Asegúrate de ingresar un número.")
    
def eliminar_estudiante():
    mostrar_estudiantes()
    if len(estudiantes) == 0:
        print("No hay estudiantes para eliminar.")
        return
    
    try:
        indice = int(input("Ingresa el número del estudiante que deseas eliminar: ")) - 1
        if 0 <= indice < len(estudiantes):
            estudiante = estudiantes.pop(indice)
            print(f"Estudiante {estudiante['nombre']} eliminado con éxito.")
        else:
            print("Número de estudiante no válido.")
    except ValueError:
        print("Entrada inválida. Asegúrate de ingresar un número.")
    
def main():
    while True:
        opcion = menu()
        if opcion == '1':
            registrar_estudiante()
        elif opcion == '2':
            mostrar_estudiantes()
        elif opcion == '3':
            actualizar_estudiante()
        elif opcion == '4':
            eliminar_estudiante()
        elif opcion == '5':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

main()