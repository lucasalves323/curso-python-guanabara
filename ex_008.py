# Escreva um programa que leia um valor em metros
# e o exiba convertido em centímetros e milímetros.

n = float(input('Digite uma medida em metros: '))
dm = n * 10
cm = n * 100
mm = n * 1000
dam = n / 10
hm = n / 100
km = n / 1000

print(f'A medida digitada foi "{n:.2f}".')
print(f'Em centímetros é "{cm} cm".')
print(f'Em milímetros é "{mm} mm".')
print(f'Em decímetro é "{dm} dm".')
print(f'Em decâmetro é "{dam} dam".')
print(f'Em hectômetro é "{hm} hm".')
print(f'Em quilômetro é "{km} km".')
