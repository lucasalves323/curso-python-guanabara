# Faça um programa que mostre a tabuada de vários números, um de cada vez
# para cada valor digitado pelo usuário. O programa será interrompido
# quando o número solicidado for negativo.

print('=' * 19)
print('PROGRAMA DE TABUADA')
while True:
    n = int(input('Você quer ver a tabuada de que número? '))
    print('=' * 41)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {c * n}')
    print('=' * 41)
print('FIM DO PROGRAMA!')
