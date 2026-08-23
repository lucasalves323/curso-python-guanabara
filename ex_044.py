# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/pix: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

valor = float(input('Informe o valor do produto: R$ '))
print('''Escolha uma das opções:
[ \33[1;31m1\33[m ] Pagamento \33[1;31mà vista ou pix\33[m.
[ \33[1;32m2\33[m ] Pagamento \33[1;32mà vista no cartão\33[m.
[ \33[1;33m3\33[m ] Pagamento \33[1;33mem até 2x no cartão\33[m.
[ \33[1;34m4\33[m ] Pagamento \33[1;34mem 3x ou mais no cartão\33[m.''')

opcao = int(input('Sua opção: '))

if opcao == 1:
    print(f'Você recebeu 10% de desconto. Seu produto de R$ {valor:.2f} ficou por R$ {valor - valor * 0.1:.2f}.')
elif opcao == 2:
    print(f'Você recebeu 5% de desconto. Seu produto de R$ {valor:.2f} ficou por R$ {valor - valor * 0.05:.2f}.')
elif opcao == 3:
    print(f'Nessa condição de pagamento não há desconto.')
    print(f'Seu produto permanecerá custando R$ {valor:.2f},')
    print(f'e você pagará 2 parcelas de {valor / 2:.2f}.')
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    print(f'Nessa condição de pagamento seu produto custará {valor + valor * 0.2:.2f}')
    print(f'E você pagará {parcelas} de {valor / parcelas:.2f}.')
else:
    print('Opção inválida! Tente novamente!')