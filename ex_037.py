# Escreva um programa em Python que leia um número inteiro qualquer
# e peça para o usiário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

n = int(input('\33[7;40m Digite um número inteiro:\33[m '))
print('''Escolha uma das bases para conversão:
[ \33[1;31m1\33[m ] converter para \33[1;31mBINÁRIO.\33[m
[ \33[1;32m2\33[m ] converter para \33[1;32mOCTAL.\33[m
[ \33[1;33m3\33[m ] converter para \33[1;33mHEXADECIMAL.\33[m''')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print(f'{n} convertido para \33[1;31mBINÁRIO\33[m é igual a {bin(n).removeprefix('0b')}.')
elif opcao == 2:
    print(f'{n} convertido para \33[1;32mOCTAL\33[m é igual a {oct(n).removeprefix('0o')}.')
elif opcao == 3:
    print(f'{n} convertido para \33[1;33mHEXADECIMAL\33[m é igual a {hex(n).removeprefix('0x')}.')
else:
    print('Opção inválida!')