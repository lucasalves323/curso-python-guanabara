# Implemente o seguinte diagrama de classes: Classe Polígono (abstrata), qtd_lados, sendo perimetro() e area() metodos abstratos. Subclasses Quadrado, lado(comprimento), Subclasse Circulo, raio.

from abc import ABC, abstractmethod

class Poligono(ABC):
    def __init__(self, qtd_lados = 0):
        self.qtd_lados = qtd_lados

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Quadrado(Poligono):
    def __init__(self, lado):
        super().__init__(4)
        self.lado = lado

    def perimetro(self):
        return self.lado * self.qtd_lados

    def area(self):
        return self.lado ** 2

class Circulo(Poligono):
    def __init__(self, raio, pi = 3.14):
        super().__init__()
        self.raio = raio
        self.pi = pi
        
    def perimetro(self):
        return 2 * self.pi * self.raio

    def area(self):
        return self.pi * (self.raio ** 2)
