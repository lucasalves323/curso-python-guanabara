class Diario():
    def __init__(self, senhamestra = 'CeV!@'):
        self.__segredos = []
        self.__senha = senhamestra.strip()

    def escrever(self, msg):
        if not isinstance(msg, str) or not msg.strip():
            raise ValueError('O segredo precisa ser um texto não vazio.')
        self.__segredos.append(msg)

    def ler(self, senha = None):
        if senha != self.__senha:
            raise PermissionError('Senha inválida! Você não pode ler o meu diário!')
        return list(self.__segredos)

    def trocar_senha(self, senha_atual, nova_senha):
        if senha_atual != self.__senha:
            raise PermissionError('Senha atual incorreta!')
        self.__senha = nova_senha.strip()

    @property
    def senha(self):
        raise PermissionError('Ninguém tem permissão de ver a senha')