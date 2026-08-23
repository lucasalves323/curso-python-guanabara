# escreva um programa que leia a velocidade de um carro. Se ele 
# ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi
# multado. A multa vai custar R$ 7,00 por caada Km acima do limite.

velocidade = int(input('Qual a velocidade do carro? '))


if velocidade > 80:
    print('MULTADO! Você excedeu o limite de 80Km/h.')
    print(f'A multa vai custar R$ {(velocidade - 80) * 7:.2f}!')
print('Siga com segurança. Boa viagem!')