class Produto:
    def __init__(self, codproduto, nome, preco, estoque):
        self._codproduto = codproduto
        self._nome = nome
        self._preco = preco
        self._estoque = estoque

    @property
    def codproduto(self):
        return self._codproduto

    @codproduto.setter
    def codproduto(self, value):
        self._codproduto = value

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, value):
        self._preco = value

    @property
    def estoque(self):
        return self._estoque

    @estoque.setter
    def estoque(self, value):
        self._estoque = value