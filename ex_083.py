# Crie um programa onde o usuário digite uma expressão qualquer que use
# parênteses. Seu aplicativo deverá analisar se a expressão passada está
# com os parênteses abertos e fechados na ordem correta.
expressao = str(input('Digite a expressão: '))
cont = 0


if expressao[0] == ')' or expressao[-1] == '(':
    print('Expressão inválida1!')
else:
    for c in expressao:
        if c == '(':
            cont += 1
        elif c == ')':
            cont -= 1
    if cont == 0:
        print('Expressão válida!')
    else:
        print('Expressão inválida2!')
        