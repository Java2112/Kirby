def crear_jugador(jugadores, nombre, nivel, puntuacion):
    jugadores[nombre] = {'nivel': nivel, 'puntuacion': puntuacion}
    print(f"Jugador {nombre} creado.")

def ver_jugadores(jugadores):
    if jugadores:
        for nombre, datos in jugadores.items():
            print(f"{nombre}: Nivel {datos['nivel']}, Puntuación {datos['puntuacion']}")
    else:
        print("No hay jugadores registrados.")

def eliminar_jugador(jugadores, nombre):
    if nombre in jugadores:
        del jugadores[nombre]
        print(f"Jugador {nombre} eliminado.")
    else:
        print("Jugador no encontrado.")

def gestionar_jugadores(jugadores):
    while True:
        print("\n--- Gestionar Jugadores ---")
        print("1. Crear Jugador")
        print("2. Ver Jugadores")
        print("3. Eliminar Jugador")
        print("4. Volver")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre del jugador: ")
            nivel = int(input("Nivel del jugador: "))
            puntuacion = int(input("Puntuación del jugador: "))
            crear_jugador(jugadores, nombre, nivel, puntuacion)
        elif opcion == "2":
            ver_jugadores(jugadores)
        elif opcion == "3":
            nombre = input("Nombre del jugador a eliminar: ")
            eliminar_jugador(jugadores, nombre)
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")
