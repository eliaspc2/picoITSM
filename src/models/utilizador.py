class Utilizador:
    def __init__(self, username, password, perfil, ativo=1, id_tecnico=None):
        self.username = username
        self.password = password
        self.perfil = perfil
        self.ativo = ativo
        self.id_tecnico = id_tecnico
