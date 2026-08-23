# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('Mateus', 'Marcos', 'Lucas', 'Joao', 'Atos', 'Romanos', 'Corintios')
'''vogais = ('aeiou')


for p in range(0, len(palavras)):
    print(f'\nNa palavra {palavras[p].upper()} temos as vogais: ', end='')
    for letra in palavras[p]:
        if letra.lower() in vogais:
            print(letra, end=', ')'''

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos as vogais: ', end='')
    for vogais in p:
        if vogais.lower() in 'aeiou':
            print(vogais, end=' ')

# O primeiro 'for' vai analisar cada nome da lista {palavras}. Já o 
# segundo 'for' vai analisar dentro do primeiro nome da lista. Então
# dentro dessa primeira palavra eu analisei se tem as vogais 'aeiou'.


    