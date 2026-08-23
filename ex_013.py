# Faça um algorítimo que leia o salário de um funcionário
# e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite o valor do salário: '))
aumento = (salario * 0.15)

print(f'O funcionário que ganhava um salário de R${salario:.2f}, com 15% de aumento ganhará R${salario + aumento:.2f}.')
