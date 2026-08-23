# Crie um programa que tenha uma função chamada voto() que vai receber
# como parâmetro o ano de nascimento de uma pessoa, retornando um valor
# literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO
# nas eleições.
'''from datetime import date
def voto(n=0):
    idade = date.today().year - n
    if idade >= 18:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO!')
    elif idade >= 16:
        print(f'Com {idade} anos: VOTO OPICIONAL!')
    else:
        print(f'Com {idade} anos: VOTO NEGADO!')

voto(int(input('Em que ano você nasceu? ')))'''

def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO!'
    elif idade <= 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPICIONAL!'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO!'

print(voto(int(input('Em que ano você nasceu? '))))
