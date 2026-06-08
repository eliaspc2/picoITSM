import re


class Validators:

    @staticmethod
    def nao_vazio(valor):
        return valor is not None and valor.strip() != ""

    @staticmethod
    def email(valor):
        padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return re.match(padrao, valor) is not None

    @staticmethod
    def prioridade(valor):
        return valor.upper() in ["BAIXA", "MEDIA", "ALTA"]

    @staticmethod
    def estado_ticket(valor):
        return valor.upper() in ["ABERTO", "EM_CURSO", "FECHADO"]

    @staticmethod
    def booleano_numero(valor):
        return valor in ["0", "1"]

    @staticmethod
    def inteiro_positivo(valor):
        return valor.isdigit() and int(valor) > 0