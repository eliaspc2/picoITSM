class Utilizador:
    def __init__(self, username, password, perfil, ativo=1):
        self.username = username
        self.password = password
        self.perfil = perfil
        self.ativo = ativo
