# Declaração de Classe
class Gafanhoto:
    """
Essa classe cria um Gafanhoto, que é uma pessoa que tem nome e idade.

Para criar uma nova pessoa, use variável = Gafanhoto(nome, idade)
    """
    def __init__(self, nome = '', idade = 0): 
        self.nome = nome
        self.idade = idade

    # Métodos de Instância
    def aniversario(self):
        self.idade = self.idade + 1

    # Outro método
    def __str__(self):
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade.'

    def __getstate__(self):
        return f'Estado: Nome = {self.nome} e idade = {self.idade}.'
    # O estado é o conjunto de valores que faz parte de um objeto.


# Declaração de Objetos
g1 = Gafanhoto('Maria', 17) 
g1.aniversario()
print(g1.__doc__)
print(g1)
print(g1.__dict__) #Atributo
print(g1.__getstate__()) #Método, porque tem parênteses
print(g1.__class__)
