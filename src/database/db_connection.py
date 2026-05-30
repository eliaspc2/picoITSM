import sqlite3

class DatabaseConnection:

    @staticmethod
    def ligar_bd():
        return sqlite3.connect("database/picoitsm.db")

    @staticmethod
    def fechar_bd(conn):
        if conn:
            conn.close()