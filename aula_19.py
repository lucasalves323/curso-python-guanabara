pessoas = {'nome': 'Lucas', 'sexo': 'M', 'idade': 35}
print(pessoas)
print(pessoas['idade'])
print(pessoas['nome'])
print(pessoas['sexo'])
print(f'{pessoas['nome']} tem {pessoas['idade']} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items()) #ele cria uma tupla para cada momento.

for k in pessoas.keys():
    print(k)
print('============')
for v in pessoas.values():
    print(v)
print('============')
for k, v in pessoas.items(): #esse 'items' substitui o 'enumarate'
    print(f'{k} = {v}.')

del pessoas['sexo']
print(pessoas.keys())
pessoas['nome'] = 'Priscilla'
print(pessoas['nome'])
pessoas['peso'] = 60.0
for k, v in pessoas.items():
    print(f'{k} = {v}')

# CRIANDO DICIONÁRIO DENTRO DE UMA LISTA
brasil = []
estado1 = {'UF': 'Pernambuco', 'SIGLA': 'PE'}
estado2 = {'UF': 'São Paulo', 'SIGLA': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(estado1)
print(estado2)
print(brasil) #Dentro da lista 'brasil' tem dois dicionários

print(brasil[0])
print(brasil[1])
print(brasil[0]['UF'])
print(brasil[1]['SIGLA'])

estado = dict()
brasil = list()

for c in range(0, 3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['SIGLA'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')

for e in brasil:
    for v in e.values():
        print(v, end=' ')