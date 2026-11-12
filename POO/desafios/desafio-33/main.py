from desafio_33 import *
from rich import print, inspect


def main():
    a = Aluno('Ana', 2000, 'ADS')    # deve funcionar
    a.curso = 'ENG'                  # deve funcionar
    try:
        a.curso = 'XYZ'
    except ValueError as e:
        print(e)  

if __name__ == '__main__':
    main()