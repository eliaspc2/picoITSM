from datetime import datetime
from pathlib import Path


class Logger:
    CAMINHO_LOG = Path("logs/picoitsm.log")
    utilizador_atual = None

    @staticmethod
    def definir_utilizador(utilizador):
        Logger.utilizador_atual = utilizador

    @staticmethod
    def obter_nome_utilizador():
        if Logger.utilizador_atual:
            return Logger.utilizador_atual[1]

        return "SISTEMA"

    @staticmethod
    def registar(acao, entidade, detalhes=""):
        Logger.CAMINHO_LOG.parent.mkdir(exist_ok=True)

        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        utilizador = Logger.obter_nome_utilizador()
        linha = f"{data_hora} | {utilizador} | {acao} | {entidade}"

        if detalhes:
            linha += f" | {detalhes}"

        with Logger.CAMINHO_LOG.open("a", encoding="utf-8") as ficheiro:
            ficheiro.write(linha + "\n")
