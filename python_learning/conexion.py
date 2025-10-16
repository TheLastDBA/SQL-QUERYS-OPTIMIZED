import mysql.connector

def crear_conexion():
    try:
        conn = mysql.connector.connect(
            host="10.1.2.250",
            port=3306,
            user="prueba",
            password="Tecnoglass*2025",
            database="tecnososft"
        )
        return conn
    except mysql.connector.Error as e:
        print("Error al conectar:", e)
        return None
