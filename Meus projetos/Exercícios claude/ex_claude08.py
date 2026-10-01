"""
Atributo de classe + estado compartilhado

Crie uma classe Jogador com um atributo de classe total_jogadores = 0. Toda vez que um novo Jogador for criado (__init__), incremente esse contador. Crie uma forma de consultar quantos jogadores já foram criados no total, mesmo que alguns já tenham "saído do jogo". Isso reforça a diferença entre atributo de instância e de classe, mas aplicado a algo que acumula entre todos os objetos.
"""

class Jogador:
    total_jogadores = 0

    def __init__(self, nome):
        self.nome = nome
        Jogador.total_jogadores += 1

    def consultar(self):
        return Jogador.total_jogadores

j = Jogador('Lucas')
j = Jogador('Pedro')
j = Jogador('Silas')
j = Jogador('João')

print(j.consultar())
