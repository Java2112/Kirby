class Inventario:
    def __init__(self):
        self.inventario = {}

    def agregar_item(self, nombre, descripcion):
        self.inventario[nombre] = descripcion

    def obtener_item(self, nombre):
        return self.inventario.get(nombre, "Item no encontrado.")

def gestionar_inventarios(inventarios):
    while True:
        print("\n--- Gestionar Inventarios ---")
        print("1. Agregar Ítem")
        print("2. Ver Inventario")
        print("3. Volver")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            jugador = input("Nombre del jugador: ")
            if jugador not in inventarios:
                inventarios[jugador] = Inventario()
            item = input("Nombre del ítem: ")
            descripcion = input("Descripción del ítem: ")
            inventarios[jugador].agregar_item(item, descripcion)
            print(f"Ítem {item} agregado al inventario de {jugador}.")
        elif opcion == "2":
            jugador = input("Nombre del jugador: ")
            if jugador in inventarios:
                for item, descripcion in inventarios[jugador].inventario.items():
                    print(f"{item}: {descripcion}")
            else:
                print("Este jugador no tiene inventario.")
        elif opcion == "3":
            break
        else:
            print("Opción no válida.")
