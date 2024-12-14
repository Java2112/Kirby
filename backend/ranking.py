import sqlite3

def conectar_db():
    return sqlite3.connect("juego.db")

def crear_tabla_jugadores():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jugadores (
            nombre TEXT PRIMARY KEY,
            puntuacion INTEGER
        )
    """)
    conn.commit()
    conn.close()

def agregar_o_actualizar_jugador(nombre, puntuacion):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO jugadores (nombre, puntuacion) 
        VALUES (?, ?)
        ON CONFLICT(nombre) 
        DO UPDATE SET puntuacion = ?
    """, (nombre, puntuacion, puntuacion))
    conn.commit()
    conn.close()

def obtener_ranking():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT nombre, puntuacion FROM jugadores 
        ORDER BY puntuacion DESC LIMIT 10
    """)
    ranking = cursor.fetchall()
    conn.close()
    return ranking

def actualizar_ranking(jugador, puntuacion):
    agregar_o_actualizar_jugador(jugador, puntuacion)
    print("Ranking actualizado.")

def ver_ranking():
    ranking = obtener_ranking()
    print("\nRanking Global:")
    for idx, (nombre, puntuacion) in enumerate(ranking, start=1):
        print(f"{idx}. {nombre} - {puntuacion} puntos")

