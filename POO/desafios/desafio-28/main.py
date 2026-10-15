from desafio_28 import *

def main():
    t = Termostato()
    try:
        t.temperatura = 17.3
        print(f'A temperatura atual é {t.ftemperatura}')
    except Exception as e:
        print(f'Houve um problema: {e}')

if __name__ == '__main__':
    main()