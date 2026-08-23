# Crie um programa que leia nome e duas notas de vários alunos e guarde
# tudo em uma lista composta. No final, mostre um boletim contendo
# a média de cada um e permita que o usuário possa mostrar as notas
# de cada aluno individualmente.

# MINHA RESOLUÇÃO

'''lista = list()
dados = list()

while True:
    nome = str(input('Informe o nome: '))
    lista.append(nome)
    nota1 = float(input('Informe a primeira nota: '))
    lista.append(nota1)
    nota2 = float(input('Informe a segunda nota: '))
    lista.append(nota2)
    media = (nota1 + nota2) / 2
    lista.append(media)
    dados.append(lista[:])
    lista.clear()
    opcao = str(input('Você deseja continuar? [S/N] '))
    if opcao in 'Nn':
        break   
print('-=' * 30)
print('BOLETIM DO ALUNO'.center(60))
print('-=' * 30)
print(f"{'Nº':<4}{'NOME':<10}{'MÉDIA':>8}")
for n, b in enumerate(dados):
    print(f'{n:<4}{dados[n][0]:<10}{dados[n][3]:>8}')  
while True:
    aluno = int(input('Mostrar as notas de qual aluno? [999 para encerrar] '))
    if aluno == 999:
        break
    if aluno <= len(lista) - 1:
        print(f'As notas do(a) aluno(a) {dados[aluno][0]} foram {dados[aluno][1]} e {dados[aluno][2]}.')
    else:
        print('Opção inválida')
    print()
print('FIM DO PROGRAMA')'''

# RESOLUÇÃO DE GUANABARA

lista = list()
while True:
    nome = str(input('Informe o nome: '))
    nota1 = float(input('Informe a primeira nota: '))
    nota2 = float(input('Informe a segunda nota: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    opcao = str(input('Quer continuar? [S/N]: '))
    if opcao in 'Nn':
        break
print('-=' * 30)
print(f'{'Nº':<4}{'NOME':<10}{'MÉDIA':>8}')
print('-' * 30)
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if aluno == 999:
        print('FINALIZANDO...')
        break
    if aluno <= len(lista) - 1:
        print(f'Notas de {lista[aluno][0]} são {lista[aluno][1]}')




