import sqlite3

def conectar_db():
    return sqlite3.connect("juego.db")

def obtener_top_10_jugadores():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT nombre, puntuacion FROM jugadores 
        ORDER BY puntuacion DESC LIMIT 10
    """)
    top_10 = cursor.fetchall()
    conn.close()
    return top_10

def verificar_inventario(jugador, inventarios):
    if jugador in inventarios:
        for item, descripcion in inventarios[jugador].inventario.items():
            print(f"{item}: {descripcion}")
    else:
        print("Este jugador no tiene inventario.")

def listar_partidas_por_fecha(arbol_partidas, fecha_inicio, fecha_fin):
    partidas = arbol_partidas.listar_partidas()
    for partida in partidas:
        fecha_partida = partida['fecha']
        if fecha_inicio <= fecha_partida <= fecha_fin:
            print(partida)
