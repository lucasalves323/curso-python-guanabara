from abc import ABC, abstractmethod
from datetime import date

class Pessoa(ABC):
    def __init__(self, nome:str, nasc:int):
        self._nome = nome
        self._nascimento = None #não jogo aqui, pq vai ser validável.
        self.nascimento = nasc

    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, ano:int):
        if not isinstance(ano, int):
            raise TypeError('O ano precisa ser um número inteiro')
        if 1900 <= ano <= date.today().year:
            self._nascimento = ano
        else:
            raise ValueError(f'Ano {ano} é inválido')

    @property
    def idade(self):
        return date.today().year - self._nascimento

    @idade.setter
    def idade(self, valor):
        raise PermissionError('Você não pode alterar idade. Mude o ano de nascimento.')


class Aluno(Pessoa):

    cursos_oficiais = ['ADM', 'ADS', 'ENG', 'CONT']

    def __init__(self, nome, nasc, curso:str):
        super().__init__(nome, nasc)
        self._curso = None
        self.curso = curso

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, curso):
        if not isinstance(curso, str):
            raise TypeError('O curso deve ser um texto')
        curso = curso.strip().upper()
        if curso not in Aluno.cursos_oficiais:
            raise ValueError(f'O curso {curso} não está na lista de cursos oficiais.')
        self._curso = curso

    def add_curso(self, curso):
        if not isinstance(curso, str):
            raise TypeError('O curso deve ser um texto')
        curso = curso.strip().upper()
        if not 3 <= len(curso) <= 5:
            raise ValueError(f'Nome {curso} está fora do padrão para cursos.')
        if curso in Aluno.cursos_oficiais:
            raise ValueError(f'O curso {curso} já faz parte da lista.')
        Aluno.cursos_oficiais.append(curso)