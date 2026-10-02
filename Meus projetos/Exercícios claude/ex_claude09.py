"""
Crie uma classe abstrata Animal com um atributo self.sons = [] (vazio) definido no __init__ da mãe. Cada subclasse (Cachorro, Gato, Passaro) deve preencher self.sons com uma lista própria de sons (igual você fez com golpes em Guerreiro/Mago). Crie um método concreto emitir_som(self) na classe mãe que escolhe aleatoriamente um som da lista e imprime. Adicione um método abstrato se_mover(self) que cada subclasse implementa do seu jeito.
"""
from abc import ABC, abstractmethod
import random

class Animal(ABC):
    def __init__(self):
        super().__init__()
        self.sons = []

    def emitir_som(self):
        return f'O {self.__class__.__name__} fez {random.choice(self.sons)}'

    @abstractmethod
    def se_mover(self):
        pass

class Cachorro(Animal):
    def __init__(self):
        super().__init__()
        self.sons = ['Au au!', 'Rrrrrr', 'Ruf ruf']

    def se_mover(self):
        return f'O cachorro moveu-se rapidamente ao alvo.'

class Gato(Animal):
    def __init__(self):
        super().__init__()
        self.sons = ['Miau', 'Miaaaau', 'Grrrrr']

    def se_mover(self):
        return f'O gato moveu-se sorrateiramente pelo chão.'

class Passaro(Animal):
    def __init__(self):
        super().__init__()
        self.sons = ['Piiii', 'Bem-te-vi', 'Fiiiii']

    def se_mover(self):
        return f'O pássaro voou rapidamente entre as árvores'


c = Cachorro()
print(c.emitir_som())   # O Cachorro fez Au au! (ou outro som, aleatório)
print(c.se_mover())      # O cachorro moveu-se rapidamente ao alvo.

g = Gato()
print(g.emitir_som())
print(g.se_mover())

animais = [Cachorro(), Gato(), Passaro()]
for a in animais:
    print(a.emitir_som())
    print(a.se_mover())