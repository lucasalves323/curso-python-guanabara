# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu índice de Massa Corporal (IMC) e mostre seu status,
# de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do peso
# - Entre 18,5 e 25: Peso ideal
# - 25 até 30: sobrepeso; 30 até 40: obesidade; acima de 40: obesidade mórbida

print('=' * 25)
print('\33[7;40mVAMOS CALCULAR SEU I.M.C.\33[m')
print('=' * 25)

peso = float(input('Informe o peso (Kg): '))
altura = float(input('Informe a altura (m): '))
imc = peso / altura ** 2

if imc < 18.5:
    print(f'Seu resultado foi {imc:.1f}. Você está \33[1;31mabaixo do peso\33[m!')
elif imc >= 18.5 and imc <= 25:
    print(f'Seu resultado foi {imc:.1f}. Você está no \33[1;34mpeso ideal\33[m.')
elif imc > 25 and imc <= 30:
    print(f'Seu resultado foi {imc:.1f}. Você está com \33[1;33msobrepeso\33[m.')
elif imc > 30 and imc <= 40:
    print(f'Seu resultado foi {imc:.1f}. Você está com \33[1;31mobesidade\33[m.')
else:
    print(f'Seu resultado foi {imc:.1f}. Você está com \33[1;31mobesidade mórbida\33[m.')