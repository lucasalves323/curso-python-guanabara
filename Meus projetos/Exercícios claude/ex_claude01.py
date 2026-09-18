"""
Nível 1 — Revisão de classes e encapsulamento

Exercício 1: Crie uma classe ContaBancaria com atributos privados _saldo e _titular. Implemente métodos depositar(valor), sacar(valor) (não pode deixar saldo negativo) e mostrar_saldo(). Use @property para expor o saldo de forma somente leitura.
"""

class ContaBancaria:
    def __init__(self, saldo, titular):
        self._saldo = saldo
        self._titular = titular

    def depositar(self, valor = 0):
        deposito = valor
        self._saldo += deposito
        print(f'{self._titular} depositou R${deposito:.2f}. Seu saldo agora é R${self._saldo:.2f}.')

    def sacar(self, valor = 0):
        saque = valor
        if valor > self._saldo:
            print(f'Saldo insuficiente!')
        else:
            self._saldo -= saque
            print(f'{self._titular} sacou R${saque:.2f}. Seu saldo agora é R${self._saldo:.2f}')

    def mostrar_saldo(self):
        print(f'Seu saldo atual é R${self._saldo:.2f}')

    @property
    def saldo(self):
        return self._saldo


p1 = ContaBancaria(2000, 'Lucas')
p1.depositar(1000)
p1.sacar(1000)
p1.mostrar_saldo()
print(p1._saldo)

"""
conta = ContaBancaria(100, "Lucas")
print(conta.saldo)      # 100 — leitura funciona
conta.saldo = 9999      # deve dar AttributeError!
"""