# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora
# a possibilidade da digitação de um número de tipo inválido. Aproveite
# e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(numero):
    while True:    
        try:
            num = int(input(numero))
        except Exception as erro:
            print('\033[0;30;41mInfelizmente encontramos um erro!\033[m')
            print(f'O erro encontrado foi {erro.__class__}')
            print('Digite um número inteiro válido!')
        except (KeyboardInterrupt):
            print('\033[0;30;41mEntrada de dados interrompida pelo usuário.\033[m')
        else:
            return num
        print()

def leiaFloat(valor):
    while True:
        try:
            num = float(input(valor))
        except Exception as erro:
            print('\033[0;30;41mInfelizmente encontramos um erro!\033[m')
            print(f'O erro encontrado foi {erro.__class__}')
            print('Digite um número real válido!')
        except (KeyboardInterrupt):
            print('\033[0;30;41mEntrada de dados interrompida pelo usuário.\033[m')
        else:
            return num
        print()
    

n = leiaInt('Digite um número Inteiro: ')
v = leiaFloat('Digite um valor Real: ')
print()
print(f'O valor inteiro digitado foi {n} e o valor real foi {v}')
