class VendaController:
    def __init__(self, mysql):
        self.mysql = mysql

    def efetuar_venda(self, codcliente, data, itens):
        print(f"Iniciando efetuar_venda: codcliente={codcliente}, data={data}, itens={itens}")
        if not itens:
            print("Erro: Nenhum item fornecido para a venda.")
            return False

        try:
            cursor = self.mysql.connection.cursor()
            valor_total = 0
            for item in itens:
                print(f"Processando item: codproduto={item['codproduto']}, qtde={item['qtde']}")
                if item['qtde'] <= 0:
                    print(f"Erro: Quantidade inválida para codproduto={item['codproduto']}")
                    raise Exception("Quantidade deve ser maior que zero.")

                
                cursor.execute('SELECT preco, estoque FROM produto WHERE codproduto = %s', (item['codproduto'],))
                resultado = cursor.fetchone()
                if not resultado:
                    print(f"Erro: Produto {item['codproduto']} não encontrado.")
                    raise Exception(f"Produto {item['codproduto']} não encontrado.")
                
                preco, estoque = resultado
                if int(estoque) < item['qtde']:
                    print(f"Erro: Estoque insuficiente para codproduto={item['codproduto']}. Estoque disponível: {estoque}, solicitado: {item['qtde']}")
                    raise Exception(f"Estoque insuficiente para o produto {item['codproduto']}. Disponível: {estoque}, solicitado: {item['qtde']}")

                item['valor'] = float(preco) 
                valor_total += item['valor'] * item['qtde']
                print(f"Item processado: valor={item['valor']}, subtotal={item['valor'] * item['qtde']}")

            print(f"Valor total da venda: {valor_total}")
           
            cursor.execute('INSERT INTO venda (data, valor_total, codcliente) VALUES (%s, %s, %s)',
                          (data, valor_total, codcliente))
            codvenda = cursor.lastrowid
            print(f"Venda inserida: codvenda={codvenda}")

            for item in itens:
                cursor.execute('INSERT INTO itemvenda (codvenda, codproduto, qtde, valor) VALUES (%s, %s, %s, %s)',
                              (codvenda, item['codproduto'], item['qtde'], item['valor']))
            
                cursor.execute('UPDATE produto SET estoque = estoque - %s WHERE codproduto = %s',
                              (item['qtde'], item['codproduto']))
                print(f"Item inserido e estoque atualizado: codvenda={codvenda}, codproduto={item['codproduto']}, qtde={item['qtde']}")

            self.mysql.connection.commit()
            cursor.close()
            print("Venda concluída com sucesso.")
            return True
        except Exception as e:
            print(f"Erro ao efetuar venda: {str(e)}")
            self.mysql.connection.rollback()
            return False