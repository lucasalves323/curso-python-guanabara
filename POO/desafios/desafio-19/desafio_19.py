from rich import print
from time import sleep

class Livro:

    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.total_paginas = paginas
        self.pag_atual = 1

        print(f':open_book: Você acabou de abrir o livro "{self.titulo}" que tem {self.total_paginas} no total. Você agora está na página {self.pag_atual}.')

    def avancar_paginas(self, qtd = 1):  
        cont = 0
        for pg in range(0, qtd, 1):
            if not self.fim_do_livro():
                self.pag_atual += 1
                sleep(0.3)
                print(f'Pág{self.pag_atual} :arrow_forward: ', end='')
                cont += 1
        print(f'Você avançou {cont} páginas e agora você está na página {self.pag_atual}.')
        if self.fim_do_livro():
            print(f':closed_book: Você chegou ao final do livro "{self.titulo}"')  

    def fim_do_livro(self) -> bool:
        if self.pag_atual == self.total_paginas:
            return True
        else:
            return False

        #return True self.pag_atual == self.total_paginas else False

l1 = Livro('Alegria em Deus', 20)
l1.avancar_paginas(10)
l1.avancar_paginas(5)
l1.avancar_paginas(10)