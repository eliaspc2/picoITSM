import sqlite3

def ligar_bd():
    return sqlite3.connect("database/picoitsm.db")
