from models.cliente import Cliente

class ClienteController:
    def __init__(self, mysql):
        self.mysql = mysql

    def cadastrar(self, nome, endereco):
        try:
            cursor = self.mysql.connection.cursor()
            cursor.execute('INSERT INTO cliente (nome, endereco) VALUES (%s, %s)', (nome, endereco))
            self.mysql.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(e)
            return False

    def listar(self):
        cursor = self.mysql.connection.cursor()
        cursor.execute('SELECT codcliente, nome, endereco FROM cliente')
        clientes_data = cursor.fetchall()
        cursor.close()
        return [Cliente(cod, nome, endereco) for cod, nome, endereco in clientes_data]