"""
Crie uma hierarquia abstrata Monstro com nome, vida, e uma lista self.ataques = [] preenchida por cada subclasse concreta (Dragao, Goblin, Esqueleto). O método atacar(self, alvo) (concreto, na classe mãe) deve: escolher um ataque aleatório da lista, calcular um dano aleatório entre um mínimo e máximo (defina os limites como atributos de classe, iguais pra todos os monstros), aplicar esse dano no alvo.vida, e impedir que a vida fique negativa. Adicione um método abstrato habilidade_especial(self) que cada subclasse implementa de forma única (por exemplo, o Dragao cura vida, o Goblin rouba um pouco de vida do alvo, o Esqueleto ignora o próximo ataque). No main, simule uma batalha de 3 rodadas entre dois monstros diferentes, chamando atacar() e, a cada 2 rodadas, habilidade_especial().
"""

from abc import ABC, abstractmethod
import random

class Monstro(ABC):
    dano_minimo = 1
    dano_maximo = 100

    def __init__(self, nome, vida):
        super().__init__()
        self.nome = nome
        self.vida = vida
        self.ataques = []
        self.protegido = False

    def atacar(self, alvo):
        if self.vida > 0 and alvo.vida > 0:
            ataque = random.choice(self.ataques)
            dano = random.randint(self.dano_minimo, self.dano_maximo)
            
            print(f'{self.nome}({self.vida}) atacou {alvo.nome}({alvo.vida}) com {ataque} e causou {dano} de dano.')
            alvo.receber_dano(dano)
        else:
            print(f'O ataque {self.nome} -> {alvo.nome} não pode acontecer!')    

    def receber_dano(self, dano):
        if self.protegido:
            self.protegido = False
            print(f'{self.nome} ignorou o ataque.')
        else:
            self.vida -= dano
            if self.vida <= 0:
                self.vida = 0
                print(f'{self.nome} foi derrotado!')
            else:
                print(f'Após o ataque, {self.nome} ficou com {self.vida} de vida.')

    def usar_habilidade(self, alvo = None):
        if self.vida > 0:
            self.habilidade_especial(alvo)
        else:
            print(f'{self.nome} já foi derrotado!')    

    @abstractmethod
    def habilidade_especial(self, alvo):
        pass


class Dragao(Monstro):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.ataques = ['Fogo mortal', 'Rugido superssônico', 'Hálito maldito']

    def habilidade_especial(self, alvo = None):
        cura = random.randint(1, 50)
        self.vida += cura
        print(f'{self.nome} voou até as nuvens e se curou em {cura} pontos.')
        
    

class Goblin(Monstro):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.ataques = ['Saque surpresa', 'Chapéu místico', 'Moeda da morte']

    def habilidade_especial(self, alvo):
        roubo = random.randint(1, 50)
        self.vida += roubo
        print(f'{self.nome} roubou vida de {alvo.nome} e se curou em {roubo} pontos de vida.')
        alvo.receber_dano(roubo)
    
    

class Esqueleto(Monstro):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.ataques = ['Ossos mortais', 'Olhos da morte', 'Risada mortal']

    def habilidade_especial(self, alvo = None):
        self.protegido = True
        print(f'{self.nome} ativou a proteção.')


p1 = Dragao('Smaug', 300)
p2 = Goblin('Squee', 300)
p3 = Esqueleto('Skeleton', 300)

for rodada in range(1, 4):
    print(f'--- Rodada {rodada} ---')
    p1.atacar(p3)
    print()
    p3.atacar(p1)
    
    if rodada % 2 == 0:
        print()
        print(f'>> Habilidades Especiais <<')

        p1.usar_habilidade(p3)
        p3.usar_habilidade(p1)
    print()

print(f'Fim da batalha: {p1.nome} com {p1.vida} de vida, e {p3.nome} com {p3.vida} de vida.')
        
    
    