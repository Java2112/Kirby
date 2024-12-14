class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.jugadores = []

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)

    def calcular_estadisticas(self):
        total_puntuacion = sum(jugador['puntuacion'] for jugador in self.jugadores)
        total_nivel = sum(jugador['nivel'] for jugador in self.jugadores)
        promedio_puntuacion = total_puntuacion / len(self.jugadores)
        promedio_nivel = total_nivel / len(self.jugadores)
        return promedio_puntuacion, promedio_nivel

def gestionar_equipos(equipos):
    while True:
        print("\n--- Gestionar Equipos ---")
        print("1. Crear Equipo")
        print("2. Agregar Jugador al Equipo")
        print("3. Ver Equipos")
        print("4. Volver")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre del equipo: ")
            equipos[nombre] = Equipo(nombre)
            print(f"Equipo {nombre} creado.")
        elif opcion == "2":
            equipo = input("Nombre del equipo: ")
            if equipo in equipos:
                jugador = input("Nombre del jugador: ")
                puntuacion = int(input("Puntuación del jugador: "))
                nivel = int(input("Nivel del jugador: "))
                equipos[equipo].agregar_jugador({'nombre': jugador, 'puntuacion': puntuacion, 'nivel': nivel})
                print(f"Jugador {jugador} agregado al equipo {equipo}.")
            else:
                print("Equipo no encontrado.")
        elif opcion == "3":
            for equipo, equipo_obj in equipos.items():
                promedio_puntuacion, promedio_nivel = equipo_obj.calcular_estadisticas()
                print(f"Equipo {equipo} - Promedio Puntuación: {promedio_puntuacion}, Promedio Nivel: {promedio_nivel}")
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")
