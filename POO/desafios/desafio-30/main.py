from desafio_30 import *
from rich import print, inspect


def main():
    c = Credencial()
    
    try:
        c.senha = input('Digite sua senha: ')
    except ValueError as erro:
        print(erro)
        return

    tentativa = input('Confirme a senha: ')
    if c.validar(tentativa):
        print('Senha confere!')
    else:
        print('Senha errada!')

    #inspect(c, methods=True, private=True )

if __name__ == '__main__':
    main()