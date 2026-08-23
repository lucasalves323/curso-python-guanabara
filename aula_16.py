lanche = 'Hamburguer', 'Suco', 'Pizza', 'Pudim'
# Tuplas são imutáveis

# print(lanche[:2])

for comida in lanche:
   print(f'Eu vou comer {lanche}.') # Nessa eu não preciso de posição.

for posicao, comida in enumerate(lanche):
   print(f'Eu vou comer {comida} na posição {posicao}.')
print('Comi pra caramba!')

for c in range(0, len(lanche)):
   print(f'Eu vou comer {lanche[c]} na posição {c}')
print('Comi pra caramba!')

# print(sorted(lanche)) # ordem alfabética
pessoa = ('Lucas', 35, 'M', 60)
print(pessoa)
del(pessoa)
a = (2, 8, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(len(c))
print(c.count(5))
print(c.index(8))
print(c.index(5, 1)) #deslocamento de posição
