import mysql.connector
from mysql.connector import Error

DB_CONFIG = {
    "user": "root",
    "password": "123456789@",
    "host": "localhost",
    "database": "Process",
}

def init_db():
    try:
        conn = mysql.connector.connect(
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"],
            host=DB_CONFIG["host"],
        )
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS `Process`;")
        cursor.close()
        conn.close()

        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ProcessScheduling (
                ProcessID VARCHAR(5) PRIMARY KEY,
                ArrivalTime INT,
                BurstTime INT,
                CompletionTime INT,
                TurnaroundTime INT,
                WaitingTime INT,
                ResponseTime INT
            )
        """)
        conn.commit()
        cursor.close()
        return conn
    except Error as err:
        raise RuntimeError(f"Database error: {err}") from err