from datetime import datetime
from pathlib import Path


class Logger:
    CAMINHO_LOG = Path("logs/picoitsm.log")

    @staticmethod
    def registar(acao, entidade, detalhes=""):
        Logger.CAMINHO_LOG.parent.mkdir(exist_ok=True)

        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        linha = f"{data_hora} | {acao} | {entidade}"

        if detalhes:
            linha += f" | {detalhes}"

        with Logger.CAMINHO_LOG.open("a", encoding="utf-8") as ficheiro:
            ficheiro.write(linha + "\n")
