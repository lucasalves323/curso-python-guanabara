from rich import print

class Caneta:
    def __init__(self, cor = 'white'):
        match cor.lower().strip():
            case 'azul':
                escolha = '[blue]'
            case 'vermelho' | 'vermelha':
                escolha = '[red]'
            case 'verde':
                escolha = '[green]'
            case 'amarelo':
                escolha = '[yellow]'

        self.cor = escolha
        self.tampada = True

    def escrever(self, frase):
        if self.tampada:
            print(f'A {self.cor}caneta[/] está tampada!')
        else:
            print(f'{self.cor}{frase}[/]')


    def pular_linha(self, qtd = 1):
        print('\n' * qtd)

    def tampar(self):
        self.tampada = True

    def destampar(self):
        self.tampada = False


c1 = Caneta('verde')
c2 = Caneta('vermelha')
c3 = Caneta('azul')

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever('Testando')
c2.escrever('Outra cor')
c3.escrever('Tudo ok')