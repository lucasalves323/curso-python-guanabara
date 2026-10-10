from classes_ex008 import *

def main():
    c1 = ContaBancaria(111, 'Maria', 5_000)
    c1.depositar(1_000)
    c1._titular = "Pedro"

    print(c1)


if __name__ == "__main__":
    main()