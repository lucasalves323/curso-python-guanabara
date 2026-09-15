from abc import ABC, abstractclassmethod

class Pessoa(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1

    @abstractclassmethod
    def estudar(self):
        pass

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f'O aluno {self.nome} acabou de fazer matrícula')

    def estudar(self):
        print(f'O aluno {self.nome} está estudando {self.curso} na turma {self.turma}')

class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.esp = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f'O professor {self.nome} concluiu sua aula.')

    def estudar(self):
        print(f'O professor {self.nome} está estudando no {self.nivel} de {self.esp}')

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f'{self.nome} bateu o ponto.')

    def estudar(self):
        print(f'{self.nome} tem se capacitado na função de {self.cargo} para atuar melhor no setor da {self.setor}')