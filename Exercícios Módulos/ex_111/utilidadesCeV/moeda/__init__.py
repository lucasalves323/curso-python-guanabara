def aumentar(preço = 0, taxa = 0, formato = False):
    res = preço + (preço * taxa/100)
    return res if formato is False else moeda(res)

def diminuir(preço = 0, taxa = 0, formato = False):
    res = preço - (preço * taxa/100)
    return res if formato is False else moeda(res)

def dobro(preço = 0, formato = False):
    res = preço * 2
    return res if not formato else moeda(res)

def metade(preço = 0, formato = False):
    res = preço / 2
    return res if not formato else moeda(res)

def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:>8.2f}'.replace('.', ',')

def resumo(preço = 0, aumento = 0, redução = 0):
   
    print('=' * 34)
    print('RESUMO DO VALOR'.center(34))
    print('=' * 34)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(preço, aumento, True)}')
    print(f'{redução}% de redução: \t{diminuir(preço, redução, True)}')
    print('=' * 34)