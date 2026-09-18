"""
Usando o módulo abc, crie uma classe abstrata FormaGeometrica com um método abstrato calcular_area(). Crie as classes concretas Retangulo, Circulo e Triangulo, cada uma implementando calcular_area() do seu jeito. Tente instanciar FormaGeometrica() diretamente e veja o que acontece.
"""
from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod    
    def calcular_area(self):
        pass

class Retangulo(FormaGeometrica):
    def __init__(self, base, altura):
        super().__init__()
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

class Circulo(FormaGeometrica):
    def __init__(self,raio = 0, pi = 3.14):
        super().__init__()
        self.pi = pi
        self.raio = raio

    def calcular_area(self):
        return self.pi * (self.raio ** 2)

class Triangulo(FormaGeometrica):
    def __init__(self, base, altura):
        super().__init__()
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2



r = Retangulo(2, 4)
print(r.calcular_area())

c = Circulo(3)
print(c.calcular_area())

t = Triangulo(4, 4)
print(t.calcular_area())

forma = FormaGeometrica()