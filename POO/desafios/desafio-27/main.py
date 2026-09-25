from desafio_27 import *
from rich import inspect

def main():
    p1 = Guerreiro('Elliot', 1000)
    p2 = Mago('Elfo', 1000)
    p1.atacar(p2, 300)
    p2.atacar(p1, 250)
    p2.curar()
    p1.curar()
    inspect(p1)
    


if __name__ == '__main__':
    main()