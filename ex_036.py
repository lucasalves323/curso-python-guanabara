# Escreva um programa para aprovar o empréstimo bancário para a compra de
# uma casa. Pergunte o valor da casa, o salário do comprador e em
# quantos anos ele vai pagar. A prestação mensal não pode exceder 30%
# do salário ou então o empréstimo será negado.
print('~' * 30)
print('Olá, senhor comprador...')
print('~' * 30)
valorCasa = float(input('Informe o valor da casa: R$ '))
salario = float(input('Informe o seu salário: R$ '))
tempo = int(input('Quanto anos de financiamento? '))
prestacao = valorCasa / (tempo * 12)
print(f'Para pagar uma casa de R$ {valorCasa:.2f}, a prestação será de R$ {prestacao:.2f}.')

if prestacao <= (salario * 0.30):
    print('Seu empréstimo foi \033[7;40mAPROVADO!\033[m') 
else:
    print('Esse valor excede 30% do seu salário.')
    print('Infelizmente seu financiamento foi negado!')