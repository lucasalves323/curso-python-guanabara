"""
Crie uma hierarquia Veiculo → Carro e Moto. Veiculo tem marca, modelo e um método ligar() que imprime "Ligando o veículo". Em Carro, sobrescreva ligar() para chamar o método da classe pai (super().ligar()) e depois imprimir algo específico de carro. Faça o mesmo em Moto.
"""

class Veiculo:
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo

    @property
    def marca(self):
        return self._marca

    @property
    def modelo(self):
        return self._modelo

    def ligar(self):
        print('Vrum... Vrum...')

class Carro(Veiculo):
    def ligar(self):
        super().ligar()
        print('Ligando o carro...')

class Moto(Veiculo):
    def ligar(self):
        super().ligar()
        print('Ligando a moto...')


v1 = Carro('Ford', 'Ka')
v1.ligar()

v2 = Moto('Honda', 'Bros')
v2.ligar()


veiculos = [v1, v2]
for v in veiculos:
    print(f'Este veículo é da marca {v.marca} do modelo {v.modelo}')