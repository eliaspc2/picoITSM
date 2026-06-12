import sqlite3


class DatabaseConnection:

    @staticmethod
    def ligar_bd():
        conn = sqlite3.connect("database/picoitsm.db")
        conn.execute("PRAGMA foreign_keys = ON")
        return conn

    @staticmethod
    def fechar_bd(conn):
        if conn:
            conn.close()
