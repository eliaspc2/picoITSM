import sys
import tempfile
import unittest
from pathlib import Path

SRC_DIR = Path(__file__).resolve().parents[1]

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from utils.logger import Logger
from utils.security import SecurityUtils
from utils.validators import Validators


class TestSecurityUtils(unittest.TestCase):

    def test_password_pbkdf2_e_validada(self):
        password_hash = SecurityUtils.gerar_hash("segredo123")

        self.assertTrue(password_hash.startswith("pbkdf2_sha256$"))
        self.assertTrue(SecurityUtils.verificar_password("segredo123", password_hash))
        self.assertFalse(SecurityUtils.verificar_password("errada", password_hash))

    def test_password_sha256_antiga_continua_valida(self):
        password_hash_antigo = (
            "240be518fabd2724ddb6f04eeb1da596"
            "7448d7e831c08c8fa822809f74c720a9"
        )

        self.assertTrue(SecurityUtils.verificar_password("admin123", password_hash_antigo))


class TestLogger(unittest.TestCase):

    def test_logger_regista_utilizador_atual(self):
        caminho_original = Logger.CAMINHO_LOG
        utilizador_original = Logger.utilizador_atual

        with tempfile.TemporaryDirectory() as pasta:
            Logger.CAMINHO_LOG = Path(pasta) / "picoitsm.log"
            Logger.definir_utilizador((1, "admin", "ADMIN", 1, None))

            Logger.registar("CRIAR", "tickets", "id=1")

            conteudo = Logger.CAMINHO_LOG.read_text(encoding="utf-8")

        Logger.CAMINHO_LOG = caminho_original
        Logger.utilizador_atual = utilizador_original

        self.assertIn("admin | CRIAR | tickets | id=1", conteudo)


class TestValidators(unittest.TestCase):

    def test_validadores_principais(self):
        self.assertTrue(Validators.nao_vazio("texto"))
        self.assertFalse(Validators.nao_vazio("   "))
        self.assertTrue(Validators.email("geral@alpha.pt"))
        self.assertFalse(Validators.email("email-invalido"))
        self.assertTrue(Validators.prioridade("ALTA"))
        self.assertTrue(Validators.estado_ticket("EM_CURSO"))
        self.assertTrue(Validators.booleano_numero("1"))
        self.assertTrue(Validators.inteiro_positivo("10"))
        self.assertFalse(Validators.inteiro_positivo("0"))


if __name__ == "__main__":
    unittest.main()
