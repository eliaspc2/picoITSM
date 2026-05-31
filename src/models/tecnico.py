# src/models/tecnico.py

class Tecnico:
    def __init__(self, nome, email, disponivel=1, ativo=1):
        self.nome = nome
        self.email = email
        self.disponivel = disponivel
        self.ativo = ativo