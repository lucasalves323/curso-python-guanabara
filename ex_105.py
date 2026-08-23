# Faça um programa que tenha uma função notas() que pode receber
# várias notas de alunos e vai retornar um dicionário com as
# seguintes informações: Quantidade de notas, A maior nota,
# A menor nota, A média da turma, A situação (opcional)


def notas(*valores, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param valores: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = {}
    r['Total'] = len(valores)
    r['Maior'] = max(valores)
    r['Menor'] = min(valores)
    r['Média'] = sum(valores) / len(valores)
    if sit:
        if r ['Média'] >= 9:
            r['Situação'] = 'EXCELENTE'
        elif r['Média'] >= 7:
            r['Situação'] = 'BOA'
        elif r['Média'] >= 5:
            r['Situação'] = 'RAZOÁVEL'
        else:
            r['Situação'] = 'RUIM'
    return r

# Programa Principal:
resp = notas(4.5, 9, 10, sit=True)
#print(resp)
help(notas)
