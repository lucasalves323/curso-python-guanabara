from desafio_32 import *
from rich import print, inspect

def main():
    pass

cc = ContaBancaria(122, 'Lucas', 1000, 'guanabara')
cc.sacar(500)
print('Tentando mudar o nome')
cc.nome = 'Maricota'


print(cc)

#inspect(cc, methods=True, private=True)



if __name__ == '__main__':
    main()