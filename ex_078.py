# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas
# respectivas posições na lista.
valores = []
maior = 0
menor = 0
for c in range(0, 5):
    valores.append(int(input(f'Informe o {c + 1}º valor: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print(f'Você digitou os valores {valores}')
print(f'O maior valor foi {maior}, nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i + 1}, ', end='')
print()
print(f'O menor valor foi {menor}, nas posições ', end='')
for posicao, valor in enumerate(valores):
    if valor == menor:
        print(f'{posicao + 1}, ', end='')
print()
print('FIM!')

#print(f'O maior número informado foi {max(valores)}. \nEle está na posição {valores.index(max(valores)) + 1}')
#print(f'O menor número informado foi {min(valores)}. \nEle está na posição {valores.index(min(valores)) + 1}')

