import sqlite3

def conectar_db():
    return sqlite3.connect("juego.db")

def registrar_resultado_partida(jugador1, puntuacion1, jugador2, puntuacion2):
    conn = conectar_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO jugadores (nombre, puntuacion) 
        VALUES (?, ?)
        ON CONFLICT(nombre) 
        DO UPDATE SET puntuacion = ?
    """, (jugador1, puntuacion1, puntuacion1))
    
    cursor.execute("""
        INSERT INTO jugadores (nombre, puntuacion) 
        VALUES (?, ?)
        ON CONFLICT(nombre) 
        DO UPDATE SET puntuacion = ?
    """, (jugador2, puntuacion2, puntuacion2))
    
    conn.commit()
    conn.close()

def insertar_nueva_conexion(grafo, origen, destino, peso):
    if origen not in grafo.grafo:
        grafo.agregar_ubicacion(origen)
    if destino not in grafo.grafo:
        grafo.agregar_ubicacion(destino)
    
    grafo.agregar_ruta(origen, destino, peso)
    print(f"Nueva conexión de {origen} a {destino} con peso {peso} agregada.")
