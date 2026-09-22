from desafio_25 import *

def main():
    dist = 20
    entrega = Caminhao(dist)

    frete = entrega.calc_frete()
    nome = type(entrega).__name__
    if frete is not None:
        print(f'Frete de {nome} para {dist}Km custa R${frete:.2f}')
    else:
        print(f'Frete de {nome} indisponível para essa distância.')

if __name__ == '__main__':
    main()
