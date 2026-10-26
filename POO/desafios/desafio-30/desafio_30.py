from hashlib import sha256

class Credencial():
    def __init__(self):
        self.__hash = None

    def __gerar_hash(self, chave):
        return sha256(chave.encode('utf-8')).hexdigest()

    @property
    def senha(self):
        return self.__hash

    @senha.setter
    def senha(self, codigo):
        if not isinstance(codigo, str) or not codigo.strip():
            raise ValueError('A senha precisa de um texto não vazio!')
        self.__hash = self.__gerar_hash(codigo)

    def validar(self, codigo):
       if not isinstance(codigo, str) or self.__hash is None:
           return False
       return self.__gerar_hash(codigo) == self.__hash

