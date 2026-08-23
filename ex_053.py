# Crie um programa que leia uma frase qualquer e diga se ela é um
# palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
# APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO
# ANOTARAM A DATA DA MARATONA.
'''
frase = str(input('Digite uma frase: ')).upper().strip()
nova_frase = frase.replace(' ', '')
indo = nova_frase[:]
voltando = nova_frase[::-1]

print(f'A frase {indo} ao contrário fica: {voltando}')

if indo == voltando:
    print('Isso é um palíndromo!')
else:
    print('Isso não é um palíndromo!')'''

# Fazendo o exercício com 'for':

frase = str(input('Digite uma frase: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('Isso não é um palíndromo!')


