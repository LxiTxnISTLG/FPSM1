from random import randint

def actualizar_puntaje(puntaje, valor_dado):
    if valor_dado == 1:
        return 0
    else:
        return puntaje + valor_dado

def mostrar_marcador(puntaje_jugador, puntaje_computadora):
    print()
    print("#" * 20)
    print(f"Puntaje del Jugador: {puntaje_jugador}")
    print(f"Puntaje de la Computadora: {puntaje_computadora}")
    print("#" * 20)
    print()

mensaje_bienvenida = """
          ¡Bienvenido a 'Pig dice', un juego de dados!
   
    En este juego, un usuario y un oponente computadora
    lanzan un dado de 6 caras en cada ronda. Si el valor
    del dado es 1, el jugador que lanzó el 1 pierde
    todos sus puntos. De lo contrario, el jugador obtiene el
    valor del dado sumado a sus puntos. ¡El primer
    jugador en alcanzar 30 puntos gana!
"""
print(mensaje_bienvenida)

nombre_usuario = input("¿Cómo te llamas?: ")

puntaje_jugador = 0
puntaje_computadora = 0


while True:
    input(f"Presiona 'Enter' para lanzar el dado, {nombre_usuario}!\n")

    valor_dado_jugador = randint(1, 6)
    print(f"{nombre_usuario} lanzó un {valor_dado_jugador}")

    valor_dado_computadora = randint(1, 6)
    print(f"La computadora lanzó un {valor_dado_computadora}")

    puntaje_jugador = actualizar_puntaje(puntaje_jugador, valor_dado_jugador)
    puntaje_computadora = actualizar_puntaje(puntaje_computadora, valor_dado_computadora)

    mostrar_marcador(puntaje_jugador, puntaje_computadora)

    if puntaje_jugador >= 30:
        print(f"¡{nombre_usuario} gana!")
        break
    elif puntaje_computadora >= 30:
        print("¡La computadora gana!")
        break
