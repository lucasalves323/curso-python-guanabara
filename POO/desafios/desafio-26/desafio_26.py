from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel

class Funcionario(ABC):
    salario_minimo = 1_612
    desconto_inss = 7.5

    def __init__(self, nome = None):
        self.nome = nome 
        self.bruto = 0
        self.liquido = 0

    @abstractmethod
    def calc_sal(self):
        pass

    def analisar_sal(self):
        base = self.liquido / Funcionario.salario_minimo
        mensagem = f'O salário de [blue]{self.nome}[/] ({self.__class__.__name__}) é de R${self.liquido:.2f} e corresponde a [red]{base:.1f}[/] salários mínimos.'
        painel = Panel(f'{mensagem}', title='Análise de Salário', width=50)
        print(painel)

class Horista(Funcionario):
    def __init__(self, nome=None, valor_hora=7.37, qtd_horas=220):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trab = qtd_horas
        self.bruto = self.valor_hora * self.horas_trab

    def calc_sal(self):
        self.liquido = self.bruto - (self.bruto * Funcionario.desconto_inss / 100) 

class Mensalista(Funcionario):
    def __init__(self, nome=None, salario=Funcionario.salario_minimo):
        super().__init__(nome)
        self.bruto = salario

    def calc_sal(self):
        self.liquido = self.bruto - (self.bruto * Funcionario.desconto_inss / 100)