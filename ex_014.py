# Escreva um programa que converta uma temperatura
# digitando em graus Celsius e converta para Fahrenheit.

tempC = float(input('Digite a temperatura em Celsius: '))
tempF = tempC * 1.8 + 32

print(f'A temperatura {tempC}ºC convertida em Fahrenheit fica {tempF}ºF.')