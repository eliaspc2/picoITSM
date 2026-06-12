import hashlib
import os


class SecurityUtils:
    ITERACOES = 120000

    @staticmethod
    def gerar_hash(password):
        salt = os.urandom(16).hex()
        password_hash = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode(),
            bytes.fromhex(salt),
            SecurityUtils.ITERACOES
        ).hex()

        return f"pbkdf2_sha256${SecurityUtils.ITERACOES}${salt}${password_hash}"

    @staticmethod
    def verificar_password(password, password_hash):
        if password_hash.startswith("pbkdf2_sha256$"):
            partes = password_hash.split("$")

            if len(partes) != 4:
                return False

            _, iteracoes, salt, hash_guardado = partes
            hash_calculado = hashlib.pbkdf2_hmac(
                "sha256",
                password.encode(),
                bytes.fromhex(salt),
                int(iteracoes)
            ).hex()

            return hash_calculado == hash_guardado

        hash_antigo = hashlib.sha256(password.encode()).hexdigest()
        return hash_antigo == password_hash
