from rich import print, inspect
from classes_ex004 import Aluno, Professor, Funcionario

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