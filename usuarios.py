from flask import Blueprint, redirect, render_template, request, send_file, url_for
from sqlalchemy import or_
from utils import admin_required
from flask_login import login_required
from database import db
from models import Usuario
import io

bp_usuarios = Blueprint("usuarios", __name__, template_folder="templates")

@bp_usuarios.route('/create', methods=['GET', 'POST'])
def create():
  if request.method=='GET':
    return render_template('usuarios_create.html')
    
  if request.method=='POST':
    nome = request.form.get('nome')
    endereco = request.form.get('endereco')
    cidade = request.form.get('cidade')
    estado = request.form.get('estado')
    cep = request.form.get('cep')    
    cpf = request.form.get('cpf')
    cnpj = request.form.get('cnpj')   
    telefone = request.form.get('telefone')
    celular = request.form.get('celular')    
    email = request.form.get('email')
    senha = request.form.get('senha')
    confirma_senha = request.form.get('confirma_senha')

    
    u = Usuario(nome, endereco, cidade, estado, cep,  cpf, cnpj, telefone, celular, email, senha, confirma_senha)
    db.session.add(u)
    db.session.commit()

    return render_template('confirmacao.html')

 
@bp_usuarios.route('/recovery', methods= ['GET', 'POST'])
@login_required
@admin_required
def recovery():
  
  if request.method == 'GET':
    usuarios = Usuario.query.all()
    return render_template('usuarios_recovery.html', usuarios = usuarios)
  
  if request.method == 'POST':
    pesquisa = request.form['pesquisa']
    resultado_usuarios = Usuario.query.filter(
            or_(
                Usuario.nome.contains(pesquisa),
                Usuario.cpf.contains(pesquisa),
                Usuario.cnpj.contains(pesquisa),
                Usuario.cidade.contains(pesquisa),
                Usuario.endereco.contains(pesquisa),
                Usuario.telefone.contains(pesquisa),
                Usuario.celular.contains(pesquisa),
                Usuario.email.contains(pesquisa),
            )
            ).all()               
    return render_template('usuarios_recovery.html', usuarios = resultado_usuarios) 

  


@bp_usuarios.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
  u = Usuario.query.get(id)
  
  if request.method =='GET':
    return render_template('usuarios_update.html', u = u)

  if request.method=='POST':
    nome = request.form.get('nome')
    endereco = request.form.get('endereco')
    cidade = request.form.get('cidade')
    estado = request.form.get('estado')
    cep = request.form.get('cep')    
    cpf = request.form.get('cpf')
    cnpj = request.form.get('cnpj')
    telefone = request.form.get('telefone')
    celular = request.form.get('celular')    
    email = request.form.get('email')
    senha = request.form.get('senha')
    confirma_senha = request.form.get('confirma_senha')
    u.nome = nome
    u.endereco = endereco
    u.cidade = cidade
    u.estado = estado
    u.cep = cep    
    u.cpf = cpf
    u.cnpj = cnpj
    u.telefone = telefone
    u.celular = celular  
    u.email = email
    u.senha = senha
    u.confirma_senha = confirma_senha

    db.session.add(u)
    db.session.commit()
    
    return redirect(url_for('usuarios.recovery' ))



@bp_usuarios.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
  u = Usuario.query.get(id)
  if request.method=='GET':
    return render_template('usuarios_delete.html', u = u)
    
  if request.method=='POST':
     db.session.delete(u)
     db.session.commit()

     return render_template('deletados.html')
  