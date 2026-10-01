"""
Encapsulamento + interação entre dois objetos

Crie uma classe Carteira com _saldo protegido e @property de leitura. Implemente um método transferir(self, destino, valor) que subtrai o valor da própria carteira e soma na carteira de destino (outro objeto Carteira). Bloqueie a transferência se o saldo for insuficiente. Isso pratica o mesmo padrão de "self afeta outro objeto" que apareceu no atacar().
"""

class Carteira:
    def __init__(self, titular, saldo=0):
        self._titular = titular
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    def transferir(self, destino, valor):
        if valor > self._saldo:
            print(f'{self._titular} não tem saldo suficiente para transferir R${valor:.2f}.')
        else:
            self._saldo -= valor
            destino._saldo += valor
            print(f'{self._titular} transferiu R${valor:.2f} para {destino._titular}.')

c1 = Carteira('Lucas', 500)
c2 = Carteira('João', 100)

c1.transferir(c2, 200)

print(c1.saldo)
print(c2.saldo)

c1.transferir(c2, 500)


    

    