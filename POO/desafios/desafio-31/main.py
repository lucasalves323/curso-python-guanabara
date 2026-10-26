from desafio_31 import *

def main():
    
    r = Retangulo()
    try:
        r.base = 12
        r.altura = 7
        #r.medidas = (6, 10)

    except Exception as e:
        print(f'Ocorreu um erro do tipo {type(e).__name__}: {e}')
        return

    print(r.medidas)
     
if __name__ == '__main__':
    main()