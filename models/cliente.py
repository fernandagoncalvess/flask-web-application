class Cliente:
    def __init__(self, codcliente, nome, endereco):
        self._codcliente = codcliente
        self._nome = nome
        self._endereco = endereco

    @property
    def codcliente(self):
        return self._codcliente

    @codcliente.setter
    def codcliente(self, value):
        self._codcliente = value

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, value):
        self._endereco = value