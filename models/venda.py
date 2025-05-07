class Venda:
    def __init__(self, codvenda, data, valor_total, codcliente):
        self._codvenda = codvenda
        self._data = data
        self._valor_total = valor_total
        self._codcliente = codcliente

    @property
    def codvenda(self):
        return self._codvenda

    @codvenda.setter
    def codvenda(self, value):
        self._codvenda = value

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def valor_total(self):
        return self._valor_total

    @valor_total.setter
    def valor_total(self, value):
        self._valor_total = value

    @property
    def codcliente(self):
        return self._codcliente

    @codcliente.setter
    def codcliente(self, value):
        self._codcliente = value
