from rich import print
from rich import inspect

class Funcionario:
    # Atributos de classe
    empresa = "Curso em Vídeo"

    def __init__(self, nome, setor, cargo):
        #Atributos de Instância
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self):
        return f':handshake: Olá, eu sou [bold red]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa {Funcionario.empresa}.' # ou {self.__class__.empresa}

c1 = Funcionario('Maria', 'Administração', 'Diretora')
c2 = Funcionario('Pedro', 'TI', 'Programador')

print(c1.apresentacao())
print(c2.apresentacao())

# inspect(c1, methods=True)