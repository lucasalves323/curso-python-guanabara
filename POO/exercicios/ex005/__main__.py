from rich import print, inspect
from classes_ex005 import Pessoa, Aluno, Professor, Funcionario

def main():

    a1 = Aluno('José', 17, 'Informática', 'T01')
    a1.fazer_aniversario()
    a1.fazer_matricula()
    a1.estudar()

    #inspect(a1, methods=True)

    p1 = Professor('Samuel', 37, 'Biologia', 'Mestrado')
    p1.fazer_aniversario()
    p1.dar_aula()
    p1.estudar()
    #inspect(p1, methods=True)

    f1 = Funcionario('Joana', 24, 'Recepcionista', 'Recepção')
    f1.fazer_aniversario()
    f1.bater_ponto()
    f1.estudar()

if __name__ == '__main__':
    main()