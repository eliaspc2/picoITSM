# src/models/ticket.py

class Ticket:
    def __init__(self, titulo, descricao, prioridade, id_cliente, id_competencia, id_tecnico=None, estado="ABERTO"):
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.estado = estado
        self.id_cliente = id_cliente
        self.id_competencia = id_competencia
        self.id_tecnico = id_tecnico