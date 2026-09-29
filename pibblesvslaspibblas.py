print("Bienvenido, Pibble♡")
print("Ingresa tu nombre y elige tu bando para comenzar el debate")

print("-----PIBBLES GAME------")
print("1. Iniciar juego")
print("2. Cerrar juego")

opcion = input("Elige una opción: ")

if opcion == "1":

    nombre = input("\nIngresa tu nombre: ")

    print("\nElige tu equipo:")
    print("1. Pibbles")
    print("2. Pibblas")

    equipo = input("Elige un equipo: ")

    if equipo == "1":
        equipo = "Pibbles"
        print("Elegiste Pibbles")

    elif equipo == "2":
        equipo = "Pibblas"
        print("Elegiste Pibblas")

    else:
        print("Opción no válida")
        exit()

    print(f"\n¡Bienvenido {nombre}!")
    print(f"Tu equipo es: {equipo}")

    puntos = 0
    jugadores = 3

    print("\n----- COMIENZA EL DEBATE -----")

    for turno in range(1, 4):

        print(f"\nTurno {turno}")
        print("Pregunta de cultura general:")

        print("¿Cuál es el planeta más grande del sistema solar?")
        respuesta = input("Tu respuesta: ")

        if respuesta.lower() == "jupiter" or respuesta.lower() == "júpiter":

            print("¡Respuesta acertada! +1 punto")
            puntos += 1

            print(f"Puntos de {equipo}: {puntos}")

            apoyo = input("¿Quieres usar el botón de apoyo? (s/n): ")

            if apoyo.lower() == "s":
                print("¡Usaste el botón de apoyo!")
                puntos += 1
                print(f"Puntos de {equipo}: {puntos}")

        else:

            print("Respuesta incorrecta.")
            jugadores -= 1

            print("Jugador eliminado.")
            print(f"Jugadores restantes: {jugadores}")

        if jugadores == 0:
            print("\n¡Tu equipo se quedó sin jugadores!")
            break

    print("\n----- FIN DEL DEBATE -----")
    print(f"Equipo: {equipo}")
    print(f"Puntos finales: {puntos}")

    if puntos >= 3:
        print(f"¡{equipo} GANA!")
        print("Recibes monedas de recompensa 🦴")

    else:
        print("El equipo rival gana.")

elif opcion == "2":
    print("Juego cerrado")

else:
    print("Opción no válida")