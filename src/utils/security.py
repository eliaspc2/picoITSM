import hashlib

class SecurityUtils:
    @staticmethod
    
    def gerar_hash(password):
        return hashlib.sha256(password.encode()).hexdigest()