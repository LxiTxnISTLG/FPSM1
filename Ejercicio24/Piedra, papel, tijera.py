from random import randint

opciones = ["piedra", "papel", "tijera"]

while True:
    valor_aleatorio = randint(0, 2)
    juego_computador = opciones[valor_aleatorio]

    juego_usuario = input("¿Qué eliges? piedra, papel, tijera: ").lower()

    if juego_usuario not in opciones:
        print("Opción no válida. Por favor elige piedra, papel o tijera.")
        continue

    print(f"Tú eliges: {juego_usuario}")
    print(f"Computadora elige: {juego_computador}")

    if juego_usuario == juego_computador:
        print("¡Es un empate!")
    elif (juego_usuario == "piedra" and juego_computador == "tijera") or \
         (juego_usuario == "papel" and juego_computador == "piedra") or \
         (juego_usuario == "tijera" and juego_computador == "papel"):
        print(f"¡Ganaste! {juego_usuario} vence a {juego_computador}")
    else:
        print(f"¡Perdiste! {juego_computador} vence a {juego_usuario}")

    jugar_de_nuevo = input("¿Quieres jugar de nuevo? (sí/no): ").lower()
    if jugar_de_nuevo != "sí":
        print("¡Gracias por jugar! Hasta la próxima.")
        break
