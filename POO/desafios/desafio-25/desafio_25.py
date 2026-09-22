from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, distancia):
        super().__init__()
        self.distancia = distancia
        self.frete = 0 

    @abstractmethod
    def calc_frete(self):
        pass

class Moto(Transporte):
    def __init__(self, distancia, fator=0.50):
        super().__init__(distancia)
        self.fator = fator

    def calc_frete(self):
        self.frete = self.distancia * self.fator 
        return self.frete

class Caminhao(Transporte):
    def __init__(self, distancia, fator=1.20):
        super().__init__(distancia)
        self.fator = fator

    def calc_frete(self):
        if self.distancia >= 50:
            self.frete = self.distancia * self.fator
            return self.frete
        else:
            return None

class Drone(Transporte):
    def __init__(self, distancia, fator=9.5):
        super().__init__(distancia)
        self.fator = fator

    def calc_frete(self):
        if self.distancia <= 10:
            self.frete = self.distancia * self.fator
            return self.frete
        else:
            return None

