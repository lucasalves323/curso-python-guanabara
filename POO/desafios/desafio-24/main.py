from desafio_24 import *

def main():
    bebidas = [Cafe(), Cha(), Leite()]

    for bebida in bebidas:
        bebida.preparar()
        print()

if __name__ == "__main__":
    main()