# Crie um programa onde o usuário possa digitar vários valores numéricos
# e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não
# será adicionado. No final, serão exibidos tosos os valores únicos
# digitados, em ordem crescente.

valores = []

while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Número duplicado. Não vou adicionar...')
    resposta = str(input('Você quer continuar? [S/N] ').strip()[0].upper())
    if resposta == 'N':
        break
valores.sort()
print(f'Os valores digitados foram {valores}.')
print('FIM DO PROGRAMA!')