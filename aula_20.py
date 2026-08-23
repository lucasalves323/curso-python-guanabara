def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')
    print('=' * 20)


soma(4, 5)
soma(8, 9)
soma(2, 1) 
soma(b=4, a=5)

# EMPACOTAMENTO
def contador(*num):   #o asterisco significa que eu não sei quantos parâmetros serão armazenados nessa def.
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')
    for v in num:
        print(f'{v} ', end='')
    print('FIM')

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

# DESEMPACOTAMENTO
def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

soma(5, 2)
soma(2, 9, 4)

# TRABALHANDO COM AS LISTAS
def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1

valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)