# Faça um programa que leia nome e média de um aluno, guardando
# também a situação em um dicionário. No final, mostre o conteúdo
# da estrutura na tela.
# A FORMA QUE EU FIZ
'''aluno = {}
aluno['Nome'] = str(input('Digite o nome do aluno: '))
aluno['Média'] = float(input(f'Digite a média do aluno {aluno['Nome']}: '))
print('-=' * 30)
print(f' - O nome é igual a {aluno["Nome"]};')
print(f' - A média é igual a {aluno['Média']};')
if aluno['Média'] >= 7:
    print(f' - A situação é igual Aprovado')
elif aluno['Média'] >= 5:
    print(f' - A situação é em Recuperação')
else:
    print(f' - A situação é Reprovado')'''

# A FORMA QUE GUANABARA FEZ
aluno = {}
aluno['nome'] = str(input('Informe o nome do aluno: '))
aluno['média'] = float(input(f'Informe a média do aluno {aluno['nome']}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif aluno['média'] >= 5:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-=' * 30)
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')