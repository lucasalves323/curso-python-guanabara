# MODULARIZAÇÃO
# FOCO: DIVIDIR UM PROGRAMA GRANDE
# FOCO: AUMENTAR A LEGIBILIDADE
# FOCO: FACILITAR A MANUTENÇÃO

from uteis import numeros

num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}.')
print(f'O dobro de {num} é {numeros.dobro(num)}')
print(f'O triplo de {num} é {numeros.triplo(num)}')

'''from uteis import fatorial, dobro, triplo

num = int(input('Digite um valor: '))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}.')
print(f'O dobro de {num} é {dobro(num)}')
print(f'O triplo de {num} é {triplo(num)}')'''

# PACOTES, OU BIBLIOTECAS
# Quando tem muitas funções dentro de um módulo, juntamos vários
# módulos separando por assuntos. Isso chamamos de Pacotes ou Bibliotecas

