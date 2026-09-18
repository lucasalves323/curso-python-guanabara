"""
Crie uma classe Produto com nome, preco e estoque. Implemente um método aplicar_desconto(percentual) que altera o preço, e um método especial __str__ para exibir o produto de forma legível (ex: "Produto: Caneta - R$ 2.50 - Estoque: 100").
"""
class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self._preco = preco
        self._estoque = estoque

    def __str__(self):
        return f'Produto: {self.nome} - R$ {self._preco:.2f} - Estoque: {self._estoque}'

    def aplicar_desconto(self, percentual = 0):
        desconto = percentual / 100
        preco_original = self._preco
        if 0 <= percentual <= 100:
            self._preco -= (desconto * self._preco)
            print(f'O produto {self.nome} custava R${preco_original:.2f}, mas com desconto de {percentual}%, custará R${self._preco:.2f}')
        else:
            print(f'Percentual de desconto inválido!')

    @property
    def preco(self):
        return self._preco


p = Produto("Caneta", 10.00, 50)
print(p)  # Produto: Caneta - R$ 10.00 - Estoque: 50
p.aplicar_desconto(10)
print(p)  # Produto: Caneta - R$ 8.00 - Estoque: 50
print(p.preco)