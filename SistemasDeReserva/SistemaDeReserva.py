usuarios = []
reservas = []

def registrar_usuario():
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    if nombre_usuario in usuarios:
        print("El nombre de usuario ya está registrado. Intente con otro.")
    else:
        usuarios.append(nombre_usuario)
        print("Usuario registrado exitosamente.")

def reservar_viaje():
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    if nombre_usuario not in usuarios:
        print("Usuario no registrado. Por favor, regístrese primero.")
    else:
        destino = input("Ingrese el destino del viaje: ")
        fecha = input("Ingrese la fecha del viaje (dd/mm/aaaa): ")
        reserva = {"usuario": nombre_usuario, "destino": destino, "fecha": fecha}
        reservas.append(reserva)
        print("Reserva realizada con éxito.")

def ver_reservas():
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    reservas_usuario = [reserva for reserva in reservas if reserva["usuario"] == nombre_usuario]
    if reservas_usuario:
        print(f"Reservas de {nombre_usuario}:")
        for reserva in reservas_usuario:
            print(f"Destino: {reserva['destino']}, Fecha: {reserva['fecha']}")
    else:
        print("No tiene reservas registradas.")

def cancelar_reserva():
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    reservas_usuario = [reserva for reserva in reservas if reserva["usuario"] == nombre_usuario]
    if reservas_usuario:
        print(f"Reservas de {nombre_usuario}:")
        for idx, reserva in enumerate(reservas_usuario, start=1):
            print(f"{idx}. Destino: {reserva['destino']}, Fecha: {reserva['fecha']}")
        
        indice = int(input("Ingrese el número de la reserva que desea cancelar: "))
        reservas.remove(reservas_usuario[indice-1])
        print("Reserva cancelada exitosamente.")
    else:
        print("No tiene reservas registradas.")

def menu_principal():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Registrar un usuario")
        print("2. Reservar un viaje")
        print("3. Ver reservas")
        print("4. Cancelar una reserva")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            reservar_viaje()
        elif opcion == "3":
            ver_reservas()
        elif opcion == "4":
            cancelar_reserva()
            break
        else:
            print("¡Muchas gracias, vuelva pronto!")
            return False
       
menu_principal()