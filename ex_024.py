# Crie um programa que leia o nome de uma cidade e diga se ela começa
# ou não com o nome "SANTO".

nome = str(input('Digite o nome da sua cidade: ')).strip().split()

print(f'O nome começa com a palavra Santo? {'SANTO' in nome[0].upper()}')



