# Crie um programa que tenha uma tupla totalmente preenchida com uma
# contagem por extenso, de zero até vinte. Seu programa deverá ler um 
# número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
    'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito',
    'dezenove', 'vinte')
while True:
    posicao = int(input('Digite um número entre 0 e 20: '))
    if 0 <= posicao <= 20:
        print(f'Você digitou o número {n[posicao]}.')
        resposta = str(input('Você deseja continuar? [S/N]: ').strip()[0].upper())
        if resposta == 'N':
            break
    else:
        print('Número inválido. Tente Novamente.')
print('Fim do programa!')