# Faça um programa que jogue par ou ímpar com o computador. O jogo só
# será interrompido quando o jogador perder, mostrando o total de
# vitórias consecutivas que ele conquistou no final do jogo.


from random import randint
cont = 0
while True:
    pc = randint(0, 11)
    tipo = ' '
    jogador = int(input('Qual o seu número? '))
    total = pc + jogador
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).upper()[0].strip() 
    print(f'Eu joguei {pc} e você {jogador}. Deu {total}.')
    if tipo == 'P':
        if total % 2 == 0:
            print(f'{total} é par. Você venceu!')
            cont += 1
        else:
            print(f'{total} é ímpar. Você perdeu!')
            print('GAME OVER...')
            break
    elif tipo == 'I':
        if total % 2 == 0:
            print(f'{total} é par. Você perdeu!')
            print('GAME OVER...')
            break
        else:
            print(f'{total} é ímpar. Você venceu!')
            cont += 1
    print('Vamos jogar novamente?')
print(f'Você venceu {cont} jogadas.')   
        
    


