# Crie um programa que leia duas notas de um aluno e calcule sua média
# mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2

if media >= 7.0:
    print(f'A primeira nota foi \33[4m{n1:.1f}\33[m, e a segunda nota foi \33[4m{n2:.1f}\33[m,')
    print(f'A média foi \33[4m{media:.1f}\33[m. O aluno foi \33[1;34mAPROVADO!\33[m')
elif media >= 5.0 and media <= 6.9:
    print(f'A primeira nota foi \33[4m{n1:.1f}\33[m, e a segunda nota foi \33[4m{n2:.1f}\33[m,')
    print(f'A média foi \33[4m{media:.1f}\33[m. O aluno está em \33[1;33mRECUPERAÇÃO!\33[m')
else:
    print(f'A primeira nota foi \33[4m{n1:.1f}\33[m, e a segunda nota foi \33[4m{n2:.1f}\33[m,')
    print(f'A média foi \33[4m{media:.1f}\33[m. O aluno foi \33[1;31mREPROVADO!\33[m')