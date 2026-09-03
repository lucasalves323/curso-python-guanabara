from rich import print
from rich.panel import Panel

class Churrasco:
    consumo_padrao = 0.4
    precokg = 82.40
    
    def __init__(self, titulo, qtd):
        self.titulo = titulo
        self.qtd = qtd

    def __str__(self):
        return f'Esse é {self.titulo} com {self.qtd} pessoas participantes.'

    def calcular_qtd_carne(self):
        return self.qtd * Churrasco.consumo_padrao

    def calcular_custo_total(self):
        return self.calcular_qtd_carne() * Churrasco.precokg

    def valor_pessoa(self):
        return (self.calcular_custo_total() / self.qtd)

    def analisar(self):
        conteudo = f'Analisando [bold green]{self.titulo}[/] com [bold blue]{self.qtd}[/] convidados.'
        conteudo += f'\nCada participante comerá {Churrasco.consumo_padrao}Kg e cada Kg custa R${Churrasco.precokg}.'

        conteudo += f'\nRecomendo comprar [bold red]{self.calcular_qtd_carne():.2f}Kg[/] de carne.'
        conteudo += f'\nO custo total será de [bold white]R${self.calcular_custo_total():.2f}[/].'
        conteudo += f'\nCada pessoa pagará [bold yellow]R${self.valor_pessoa():.2f}[/] para participar.'

        painel = Panel(conteudo, title=self.titulo)
        print(painel)

c1 = Churrasco('Churras dos Amigos', qtd= 15)
c1.analisar()

c2 = Churrasco('Confra fim de Ano', qtd= 80,)
c2.analisar()