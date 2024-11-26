from flask import Blueprint, redirect, render_template, request, send_file, url_for
from flask_login import login_required
from models import Estoque
from database import db
import io
from sqlalchemy import or_

from utils import admin_required

bp_estoque = Blueprint("estoque", __name__, template_folder= "templates")


@bp_estoque.route('/create', methods=['GET', 'POST'])
@login_required  
@admin_required
def create_estoque():
    if request.method == 'GET':
        return render_template('estoque_create.html')
    if request.method == 'POST':
        produto_id = request.form.get('produto_id') 
        referencia = request.form.get('referencia')
        quantidade = request.form.get('quantidade')          
                
        e = Estoque(produto_id, referencia, quantidade)
        db.session.add(e)
        db.session.commit()

        return render_template('confirmacao.html')
    
@bp_estoque.route('/read', methods=['GET', 'POST'])
def read_estoque():
    resultado_estoque = []
    if request.method == 'GET':
        estoque = Estoque.query.all()
        return render_template('estoque_read.html', estoque = estoque)
    if request.method == 'POST':        
        pesquisa = request.form['pesquisa']       
        resultado_estoque = Estoque.query.filter(
            or_(
                Estoque.referencia.contains(pesquisa),
                Estoque.produto_id.contains(pesquisa)                
            )
            ).all()       
        return render_template('estoque_read.html', estoque = resultado_estoque)  

@bp_estoque.route('/update/<int:id>', methods=['GET', 'POST'])
def update_estoque(id):
    e = Estoque.query.get(id)
    if request.method == 'GET':       
        return render_template('estoque_update.html', e = e)
    
    if request.method == 'POST':
        produto_id = request.form.get('produto_id') 
        referencia = request.form.get('referencia')
        quantidade = request.form.get('quantidade')            

        e.produto_id = produto_id
        e.referencia = referencia
        e.quantidade = quantidade        
         
        db.session.add(e)
        db.session.commit()

        return redirect(url_for('estoque.read_estoque'))
    
    return render_template('estoque_update.html', e = e)
        
    
@bp_estoque.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    e = Estoque.query.get(id)
    if request.method == 'GET':       
        return render_template('estoque_delete.html', e = e)
    
    if request.method == 'POST':
        db.session.delete(e)
        db.session.commit()

        return render_template('deletados.html')    




