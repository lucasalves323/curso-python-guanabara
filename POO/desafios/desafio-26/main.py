from desafio_26 import *
from rich import inspect

def main():
    f1 = Horista('Lucas', 12, 190)
    f1.calc_sal()
    f1.analisar_sal()

    f2 = Mensalista('João', 8500)  
    f2.calc_sal()
    f2.analisar_sal()

if __name__ == "__main__":
    main()