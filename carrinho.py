from flask import Blueprint, render_template, session, redirect, url_for, flash
from models import Produtos, Estoque, db, Carrinho, ItemVenda
from flask_login import login_required, current_user

bp_carrinho = Blueprint('carrinho', __name__)

@bp_carrinho.route('/')
@login_required
def carrinho_view():   
    carrinho_item = ItemVenda.query.filter_by(user_id=current_user.id).all()
    itens = []
    total = 0

    for item in carrinho_item:
        if item is not None:
            produto = Produtos.query.get(item.produto_id)
            if produto is not None:
                id_venda = item.id
                quantidade = item.quantidade
                subtotal = produto.valor * quantidade
                total += subtotal
                itens.append({'id_venda': id_venda, 'produto': produto, 'quantidade': quantidade})
                
            else:
                return render_template('carrinho.html', itens=itens, total=total, nome=current_user.nome)

    return render_template('carrinho.html', itens=itens, total=total, nome=current_user.nome)

@bp_carrinho.route('/finalizar', methods=['POST'])
@login_required
def finalizar_compra():    

    itens_venda = ItemVenda.query.filter_by(user_id=current_user.id).all()    
    
    
    try:
        for item in itens_venda:
            produto = Produtos.query.get(item.produto_id)
            estoque = Estoque.query.filter_by(produto_id=item.produto_id).first()
            estoque.quantidade -= item.quantidade
            db.session.delete(item) 
            db.session.commit()
                

            c = Carrinho(item.quantidade,item.quantidade*produto.valor,item.produto_id,current_user.id)        
            db.session.add(c)                         
                                           
            db.session.commit()                              
            
            
        session.pop('carrinho_itens', None)  # Limpar o carrinho após a compra
        return render_template('finalizada.html')
        
    except Exception as e:
        db.session.rollback()
        flash(f'Ocorreu um erro: {str(e)}', 'error')
        return render_template('credenciaisinvalidas.html', errro='Ops... algo deu errado.')

    return redirect(url_for('home'))


@bp_carrinho.route('/remover/<int:id_venda><int:produto_id>', methods=['POST'])
def remover_item(id_venda, produto_id):
    
    item = ItemVenda.query.filter_by(id=id_venda, user_id=current_user.id, produto_id = produto_id).first()   
    carrinho = session.get('carrinho_itens', [])
    
    carrinho = [i for i in carrinho if i['id'] != produto_id]
  
    session['carrinho_itens'] = carrinho
    session.modified = True 

    db.session.delete(item)
    db.session.commit()
    
    return redirect(url_for('carrinho.carrinho_view'))
