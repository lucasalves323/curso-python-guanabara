from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel
import random

class Personagem(ABC):

    def __init__(self, nome, vida):
        super().__init__()
        self.nome = nome
        self.vida = vida
        self.golpes = []

    def atacar(self, alvo, forca=50):
        if self.vida > 0 and alvo.vida > 0:
            golpe = random.choice(self.golpes)
            print(f'[blue]{self.nome}[/]({self.vida}) atacou [green]{alvo.nome}[/]({alvo.vida}) com um [red]{golpe}[/] de força {forca}')
            alvo.receber_dano(forca)
        else:
            print(f'O ataque {self.nome} -> {alvo.nome} não pode acontecer')

    def receber_dano(self, dano):
        fator = random.randint(0, dano)
        self.vida -= fator
        if self.vida < 0:
            self.vida = 0
        print(f'[blue]{self.nome}[/] recebeu um [red]dano de {fator}[/]')

    @abstractmethod
    def curar(self):
        pass

class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Pulo giratório', 'Soco de aço', 'Espada perfurante']

    def curar(self):
        fator = random.randint(0, 100)
        self.vida += fator
        print(f'[blue]{self.nome}[/] enrolou uma atadura nos ferimentos e [green]recuperou {fator} pontos de vida[/]')

class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Bola de fogo', 'Onda de poder', 'Veneno letal']
        

    def curar(self):
        fator = random.randint(0, 100)
        self.vida += fator
        print(f'[blue]{self.nome}[/] usou magia verde e [green]se curou em {fator} pontos de vida[/].')