from models.produto import Produto

class ProdutoController:
    def __init__(self, mysql):
        self.mysql = mysql

    def cadastrar(self, nome, preco, estoque):
        try:
            cursor = self.mysql.connection.cursor()
            cursor.execute('INSERT INTO produto (nome, preco, estoque) VALUES (%s, %s, %s)', (nome, preco, estoque))
            self.mysql.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(e)
            return False

    def listar(self):
        cursor = self.mysql.connection.cursor()
        cursor.execute('SELECT codproduto, nome, preco, estoque FROM produto')
        produtos_data = cursor.fetchall()
        cursor.close()
        return [Produto(cod, nome, preco, estoque) for cod, nome, preco, estoque in produtos_data]