import sqlite3

class DatabaseConnection:

    def ligar_bd():
        return sqlite3.connect("database/picoitsm.db")

    def fechar_bd(conn):
        if conn:
            conn.close()