from desafio_23 import Quadrado, Circulo   

def main():
    q = Quadrado(20)
    print(f'O perímetro de um quadrado com {q.lado} de lado, é {q.perimetro()}')
    print(f'A área de um quadrado com {q.lado} de lado, é {q.area()}')

    c = Circulo(5)
    print(f'O perímetro de um círculo com {c.raio} de raio é {c.perimetro():.1f}')
    print(f'A area de um círculo com {c.raio} de raio é {c.area()}')

if __name__ == "__main__":
    main()