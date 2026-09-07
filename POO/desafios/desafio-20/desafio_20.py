from rich import print
from rich.panel import Panel 

class Gamer:

    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = []

    def add_favoritos(self, game):
        self.favoritos.append(game)
        self.favoritos = sorted(self.favoritos, key=str.lower) # essa linha é apenas para ordenar os itens
        
    def dados(self):
        conteudo = f'Nome real: [on blue] {self.nome} [/] '
        conteudo += f'\nJogos favoridos:'
        for n, game in enumerate(self.favoritos):
            conteudo += f'\n:video_game: [blue]{game}[/]'       
        painel = Panel(conteudo, title=f'Jogador <{self.nick}>', width=40)
        print(painel)

j1 = Gamer('Fabricio da Silva', 'detonator2025')
j1.add_favoritos('Sonic')
j1.add_favoritos('Fortnite')
j1.add_favoritos('God of War')
j1.add_favoritos('Mario Bros')
j1.dados()

j2 = Gamer('Lucas Alves', 'Tiringa')
j2.add_favoritos('Counter Strike 2')
j2.add_favoritos('Red Dead Rendemption 2')
j2.add_favoritos('Call of Duty')
j2.add_favoritos('League of Legends')
j2.dados()