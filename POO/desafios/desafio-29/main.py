from desafio_29 import *
from rich import print, inspect

def main():
    d = Diario()
    d.escrever('Hoje foi um bom dia')
    d.trocar_senha('CeV!@', 'nautico')

    print(d.ler('nautico'))        # ['Hoje foi um bom dia']

    try:
        d.ler('CeV!@')             # a senha antiga não vale mais
    except PermissionError as erro:
        print(erro)

    try:
        d.escrever(123)
    except ValueError as erro:
        print(erro)



if __name__ == '__main__':
    main()