from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from controllers.clienteController import ClienteController
from controllers.produtoController import ProdutoController
from controllers.vendaController import VendaController

app = Flask(__name__)
app.secret_key = 'your_secret_key'

app.config['MYSQL_HOST'] = '177.190.74.69'
app.config['MYSQL_USER'] = 'trabtpc'
app.config['MYSQL_PASSWORD'] = 'trabtpc'
app.config['MYSQL_DB'] = 'tpc03'
app.config['MYSQL_PORT'] = 65004
mysql = MySQL(app)

cliente_controller = ClienteController(mysql)
produto_controller = ProdutoController(mysql)
venda_controller = VendaController(mysql)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clientes', methods=['GET', 'POST'])
def clientes():
    if request.method == 'POST':
        nome = request.form['nome']
        endereco = request.form['endereco']
        if cliente_controller.cadastrar(nome, endereco):
            flash('Cliente cadastrado com sucesso!', 'success')
        else:
            flash('Erro ao cadastrar cliente.', 'error')
        return redirect(url_for('clientes'))
    clientes = cliente_controller.listar()
    return render_template('clientes.html', clientes=clientes)

@app.route('/produtos', methods=['GET', 'POST'])
def produtos():
    if request.method == 'POST':
        nome = request.form['nome']
        preco = float(request.form['preco'])
        estoque = int(request.form['estoque'])
        if produto_controller.cadastrar(nome, preco, estoque):
            flash('Produto cadastrado com sucesso!', 'success')
        else:
            flash('Erro ao cadastrar produto.', 'error')
        return redirect(url_for('produtos'))
    produtos = produto_controller.listar()
    return render_template('produtos.html', produtos=produtos)

@app.route('/vendas', methods=['GET', 'POST'])
def vendas():
    if request.method == 'POST':
        codcliente = request.form['codcliente']
        data = request.form['data']
        itens = []
        for i in range(len(request.form.getlist('codproduto'))):
            itens.append({
                'codproduto': int(request.form.getlist('codproduto')[i]),
                'qtde': int(request.form.getlist('qtde')[i])
            })
        if venda_controller.efetuar_venda(codcliente, data, itens):
            flash('Venda efetuada com sucesso!', 'success')
        else:
            flash('Erro ao efetuar venda.', 'error')
        return redirect(url_for('vendas'))
    clientes = cliente_controller.listar()
    produtos = produto_controller.listar()
    return render_template('vendas.html', clientes=clientes, produtos=produtos)

if __name__ == '__main__':
    app.run(debug=True)