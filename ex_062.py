# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar
# mais alguns termos. O programa encerrará quando ele disser que quer
# mostrar 0 termos.

pt = int(input('Informe o valor do primeiro termo da PA: '))
r = int(input('Informe o valor da razão da PA: '))
cont = 1
termos = 0
mais = 10
while mais != 0:
    termos = termos + mais
    while cont <= termos:
        print(f'{pt},', end=' ')
        pt += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {cont} termos!')
    