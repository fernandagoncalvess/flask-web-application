class ItemVenda:
    def __init__(self, codvenda, codproduto, qtde, valor):
        self._codvenda = codvenda
        self._codproduto = codproduto
        self._qtde = qtde
        self._valor = valor

    @property
    def codvenda(self):
        return self._codvenda

    @codvenda.setter
    def codvenda(self, value):
        self._codvenda = value

    @property
    def codproduto(self):
        return self._codproduto

    @codproduto.setter
    def codproduto(self, value):
        self._codproduto = value

    @property
    def qtde(self):
        return self._qtde

    @qtde.setter
    def qtde(self, value):
        self._qtde = value

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, value):
        self._valor = value
