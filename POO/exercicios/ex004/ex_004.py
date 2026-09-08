from rich import print, inspect

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f'O aluno {self.nome} acabou de fazer matrícula.')

class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.esp = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f'O professor {self.nome} concluiu sua aula.')

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f'{self.nome} bateu o ponto.')

a1 = Aluno('José', 17, 'Informática', 'T01')
#a1.fazer_aniversario()
a1.fazer_matricula()

#inspect(a1, methods=True)

p1 = Professor('Samuel', 37, 'Biologia', 'Mestrado')
#p1.fazer_aniversario()
p1.dar_aula()
#inspect(p1, methods=True)

f1 = Funcionario('Joana', 24, 'Recepcionista', 'Recepção')
f1.bater_ponto()