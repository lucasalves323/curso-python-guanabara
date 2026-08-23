# Faça um programa que leia a largura e a altura de uma parede
# em metros. Calcule a sua área e a quantidade de tinta necessária
# para pintá-la. Sabendo que cada litro de tinta, pinta área de 2m².

largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura * altura
tinta = area / 2

print(f'Sua parede tem {altura}m de altura e {largura}m de largura.')
print(f'Isso dá {area}m².')
print(f'Para pintar {area}m² serão necessários: \n{tinta} litros de tinta.')