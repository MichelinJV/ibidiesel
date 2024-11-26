from flask import Blueprint, redirect, render_template, request, send_file, url_for
from flask_login import login_required
from models import Produtos
from database import db
import io
from sqlalchemy import or_
from utils import admin_required


bp_produtos = Blueprint("produtos", __name__, template_folder= "templates")

@bp_produtos.route('/create', methods=['GET', 'POST'])
@login_required  
@admin_required
def create():
    if request.method == 'GET':
        return render_template('produtos_create.html')
    if request.method == 'POST':
        referencia = request.form.get('referencia')
        valor = request.form.get('valor')        
        descricao = request.form.get('descricao')
        aplicacao = request.form.get('aplicacao')

        file = request.files['image']
        if file and file.filename:
         foto=file.read()

        p = Produtos(referencia, valor, descricao, aplicacao, foto)
        db.session.add(p)
        db.session.commit()

        
        return render_template('confirmacao.html')
    
@bp_produtos.route('/read', methods=['GET','POST'])
def read():
    resultado_produtos = []
    if request.method == 'GET':
        produtos = Produtos.query.all()
        return render_template('produtos_read.html', produtos = produtos)
    if request.method == 'POST':
        pesquisa = request.form['pesquisa']
        resultado_produtos = Produtos.query.filter(
            or_(
                Produtos.referencia.contains(pesquisa),
                Produtos.descricao.contains(pesquisa),
                Produtos.aplicacao.contains(pesquisa),
            )
            ).all()               
        return render_template('produtos_read.html', produtos = resultado_produtos)  

@bp_produtos.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    p = Produtos.query.get(id)
    if request.method == 'GET':       
        return render_template('produtos_update.html', p = p)
    
    if request.method == 'POST':
        referencia = request.form.get('referencia')
        valor = request.form.get('valor')        
        descricao = request.form.get('descricao')
        aplicacao = request.form.get('aplicacao')        

        file = request.files['image']        
        foto = None
        if file and file.filename:
            foto = file.read()

        p.referencia = referencia
        p.valor = valor        
        p.descricao = descricao
        p.aplicacao = aplicacao   
        p.foto = foto      
        
        db.session.add(p)
        db.session.commit()

        return redirect(url_for('produtos.read'))
    
    return render_template('produtos_update.html', p = p)
        
    
@bp_produtos.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    p = Produtos.query.get(id)
    if request.method == 'GET':       
        return render_template('produtos_delete.html', p = p)
    
    if request.method == 'POST':
        db.session.delete(p)
        db.session.commit()

        
        return render_template('deletados.html')
    

@bp_produtos.route('/imagens/<int:id>')
def show_images(id):
    p = Produtos.query.get(id) 
    if p.foto:
        return send_file(io.BytesIO(p.foto), mimetype='image/png')       
    return 'Imagem não encontrada', 404


