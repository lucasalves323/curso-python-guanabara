"""
Crie uma classe base Funcionario com nome e salario_base, e um método calcular_pagamento() que retorna o salário base. Depois crie duas subclasses:

Gerente, que recebe um bônus fixo de 20% sobre o salário base
Vendedor, que recebe salário base + comissão (baseada em vendas realizadas, passadas no construtor)

Cada subclasse deve sobrescrever calcular_pagamento().
"""

class Funcionario:
    def __init__(self, nome, salario_base):
        self.nome = nome
        self._salario = salario_base

    def calcular_pagamento(self):
        return self._salario

class Gerente(Funcionario):
    def __init__(self, nome, salario_base, bonus = 0.2):
        super().__init__(nome, salario_base)
        self._bonus = bonus

    def calcular_pagamento(self):
        return self._salario + (self._salario * self._bonus)
        #print(f'{self.nome} é gerente e recebe R${novo_salario:.2f}')

class Vendedor(Funcionario):
    def __init__(self, nome, salario_base, comissao = 0):
        super().__init__(nome, salario_base)
        self._comissao = comissao

    def calcular_pagamento(self):
        return self._salario + self._comissao


f1 = Gerente('Lucas', 3500)
f1.calcular_pagamento()

f2 = Vendedor('João', 1800, 600)
f2.calcular_pagamento()

funcionarios = [f1, f2]
for f in funcionarios:
    print(f'{f.nome} recebe R${f.calcular_pagamento():.2f}.')

