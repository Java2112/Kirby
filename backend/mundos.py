class Grafo:
    def __init__(self):
        self.grafo = {}

    def agregar_ubicacion(self, nombre):
        if nombre not in self.grafo:
            self.grafo[nombre] = []

    def agregar_ruta(self, origen, destino, peso):
        self.grafo[origen].append((destino, peso))
        self.grafo[destino].append((origen, peso)) 

    def mostrar_mundo(self):
        for ubicacion, rutas in self.grafo.items():
            print(f"{ubicacion}: {rutas}")

def gestionar_mundos(grafo_mundo):
    while True:
        print("\n--- Gestionar Mundos ---")
        print("1. Crear Ubicación")
        print("2. Agregar Ruta")
        print("3. Mostrar Mundo")
        print("4. Volver")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            ubicacion = input("Nombre de la ubicación: ")
            grafo_mundo.agregar_ubicacion(ubicacion)
            print(f"Ubicación {ubicacion} creada.")
        elif opcion == "2":
            origen = input("Ubicación de origen: ")
            destino = input("Ubicación de destino: ")
            peso = int(input("Peso (dificultad/tiempo) de la ruta: "))
            grafo_mundo.agregar_ruta(origen, destino, peso)
            print(f"Ruta agregada de {origen} a {destino} con peso {peso}.")
        elif opcion == "3":
            grafo_mundo.mostrar_mundo()
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")
