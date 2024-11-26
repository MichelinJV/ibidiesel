import io
from database import db
from flask import Blueprint, render_template, request, redirect, send_file, session, url_for, flash
from models import Produtos, Estoque, ItemVenda
from flask_login import login_required, current_user

bp_vendas = Blueprint('vendas', __name__)


@bp_vendas.route('/venda/<int:produto_id>', methods=['GET', 'POST'])
@login_required
def venda(produto_id):
    produto = Produtos.query.get(produto_id)
    estoque = Estoque.query.filter_by(produto_id=produto_id).first()

    if request.method == 'POST':
        quantidade = int(request.form['quantidade'])             
        
        
        i = ItemVenda(current_user.id, produto.id, quantidade)
        db.session.add(i)
        db.session.commit()
        
        return redirect(url_for('carrinho.carrinho_view'))

    return render_template('venda.html', produto=produto, estoque=estoque, nome=current_user.nome)

@bp_vendas.route('/imagem/<int:produto_id>')
def imagem_produto(produto_id):
    produto = Produtos.query.get(produto_id)
    if produto.foto:
        return send_file(io.BytesIO(produto.foto), mimetype='image/png')       
    return 'Imagem não encontrada', 404

   
    
    