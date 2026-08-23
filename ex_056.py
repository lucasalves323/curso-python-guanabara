# Desenvolva um prgrama que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual o nome
# do homem mais velho e quantas mulheres têm menos de 20 anos.
somaIdade = 0
maiorIdadeHomem = 0
nomeMaisVelho = ''
totalMulher20 = 0
for c in range(1, 5):
    print('~' * 24)
    print(f'INFORMAÇÕES DA {c}ª PESSOA')
    print('~' * 24)
    nome = str(input('Informe o nome: ')).strip()
    idade = int(input('Informe a idade: '))
    sexo = str(input('Informe o sexo [M/F]: ')).strip()
    somaIdade += idade
    if c == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeMaisVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeMaisVelho = nome
    if sexo in 'Ff' and idade < 20:
        totalMulher20 += 1
print(f'A média de idade do grupo é de {somaIdade / 4} anos.')
print(f'O homem mais velho se chama {nomeMaisVelho} e tem {maiorIdadeHomem} anos.')
print(f'O número de mulheres com menos de 20 anos é {totalMulher20}.')