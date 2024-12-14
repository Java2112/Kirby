from jugadores import gestionar_jugadores
from mundos import gestionar_mundos, Grafo
from partidas import gestionar_partidas
from inventarios import gestionar_inventarios
from equipos import gestionar_equipos
from ranking import ver_ranking, actualizar_ranking
from consulta import obtener_top_10_jugadores, verificar_inventario, listar_partidas_por_fecha
from procedimiento import registrar_resultado_partida, insertar_nueva_conexion

def menu():
    jugadores = {}
    grafo_mundo = Grafo()
    inventarios = {}
    equipos = {}

    while True:
        print("\n--- Menú Principal ---")
        print("1. Gestionar Jugadores")
        print("2. Gestionar Mundos")
        print("3. Gestionar Partidas")
        print("4. Gestionar Inventarios")
        print("5. Gestionar Equipos")
        print("6. Ver Ranking Global")
        print("7. Consultas y Análisis")
        print("8. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            gestionar_jugadores(jugadores)
        elif opcion == "2":
            gestionar_mundos(grafo_mundo)
        elif opcion == "3":
            gestionar_partidas(arbol_partidas)
        elif opcion == "4":
            gestionar_inventarios(inventarios)
        elif opcion == "5":
            gestionar_equipos(equipos)
        elif opcion == "6":
            ver_ranking()
        elif opcion == "7":
            print("\nConsultas y Análisis:")
            print("1. Top 10 Jugadores")
            print("2. Ver Inventario de Jugador")
            print("3. Listar Partidas por Fecha")
            sub_opcion = input("Elige una opción: ")
            if sub_opcion == "1":
                top_10 = obtener_top_10_jugadores()
                for jugador, puntuacion in top_10:
                    print(f"{jugador} - {puntuacion} puntos")
            elif sub_opcion == "2":
                jugador = input("Nombre del jugador: ")
                verificar_inventario(jugador, inventarios)
            elif sub_opcion == "3":
                fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ")
                fecha_fin = input("Fecha de fin (YYYY-MM-DD): ")
                listar_partidas_por_fecha(arbol_partidas, fecha_inicio, fecha_fin)
        elif opcion == "8":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
