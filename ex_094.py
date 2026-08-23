# Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os
# dicionários em uma lista. No final, mostre: A) Quantas pessoas foram
# cadastradas, B) A média de idade, C) Uma lista com as mulheres,
# D) uma lista de pessoas com idade acima da média.

pessoas = {}
dados = []
idades = []
acima = []

while True:
    pessoas['Nome'] = str(input('Informe o nome: '))
    while True:
        pessoas['Sexo'] = str(input('Informe o sexo [M/F]: ')).upper()[0]
        if pessoas['Sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoas['Idade'] = int(input('Informe a idade: '))
    idades.append(pessoas['Idade'])
    dados.append(pessoas.copy())
    while True:
        opcao = str(input('Você deseja continuar? [S/N]: ')).upper()[0]
        if opcao in 'SN':
            break
        print('Erro! Digite apenas S ou N')
    if opcao == 'N':
        break
print('-=' * 30)
media = (sum(idades) / len(dados))
print(dados)

print(f'A) Foi cadastrado um total de {len(dados)} pessoas.')
print(f'B) A média das idades foi {media:.1f}.')
print('C) As mulheres cadastradas foram: ', end='')
for p in dados:
    if p['Sexo'] in 'Ff':
        print(f'{p['Nome']} ', end='')
print()
print('D) As pessoas que estão acima da média são: ')
for p in dados:
    if p['Idade'] >= media:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')

    
