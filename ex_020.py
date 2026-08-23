# O mesmo professor do desafio 19 quer sortear a ordem
# de apresentação de trabalhos dos alunos. Faça um programa
# que leia o nome dos 4 alunos e mostre a ordem sorteada.

from random import shuffle

a1 = (input('Digite o nome do primeiro aluno: '))
a2 = (input('Digite o nome do segundo aluno: '))
a3 = (input('Digite o nome do terceiro aluno: '))
a4 = (input('Digite o nome do quarto aluno: '))

lista = [a1, a2, a3, a4]
shuffle(lista)

print(f'A sequência de apresentação do trabalho será {lista}')