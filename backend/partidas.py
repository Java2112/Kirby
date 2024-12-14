import datetime

class Nodo:
    def __init__(self, fecha, partida):
        self.fecha = fecha
        self.partida = partida
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, fecha, partida):
        if not self.raiz:
            self.raiz = Nodo(fecha, partida)
        else:
            self._insertar(self.raiz, fecha, partida)

    def _insertar(self, nodo, fecha, partida):
        if fecha < nodo.fecha:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(fecha, partida)
            else:
                self._insertar(nodo.izquierda, fecha, partida)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(fecha, partida)
            else:
                self._insertar(nodo.derecha, fecha, partida)

    def listar_partidas(self):
        return self._listar_partidas(self.raiz)

    def _listar_partidas(self, nodo):
        if nodo:
            partidas = []
            partidas.extend(self._listar_partidas(nodo.izquierda))
            partidas.append(nodo.partida)
            partidas.extend(self._listar_partidas(nodo.derecha))
            return partidas
        return []

def gestionar_partidas(arbol_partidas):
    while True:
        print("\n--- Gestionar Partidas ---")
        print("1. Crear Partida")
        print("2. Ver Partidas")
        print("3. Volver")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            fecha = input("Fecha de la partida (YYYY-MM-DD): ")
            fecha = datetime.datetime.strptime(fecha, "%Y-%m-%d")
            jugador1 = input("Jugador 1: ")
            jugador2 = input("Jugador 2: ")
            ganador = input("Ganador: ")
            partida = f"Partida entre {jugador1} y {jugador2}, ganador: {ganador}"
            arbol_partidas.insertar(fecha, partida)
            print(f"Partida registrada: {partida}")
        elif opcion == "2":
            partidas = arbol_partidas.listar_partidas()
            for partida in partidas:
                print(partida)
        elif opcion == "3":
            break
        else:
            print("Opción no válida.")
