from flask import Blueprint, redirect, render_template, request, send_file, url_for

from database import db
from models import Usuario
import io

bp_pessoas = Blueprint("pessoas", __name__, template_folder= "templates")

@bp_pessoas.route('/pessoafisica_create', methods=['GET', 'POST'])
def create_fisica():
    if request.method == 'GET':
        return render_template('pessoafisica_create.html')
    if request.method=='POST':
        nome = request.form.get('nome')
        endereco = request.form.get('endereco')
        cidade = request.form.get('cidade')
        estado = request.form.get('estado')
        cep = request.form.get('cep')
        data_nascimento = request.form.get('data_nascimento')
        cpf = request.form.get('cpf')
        rg = request.form.get('rg')
        telefone = request.form.get('telefone')
        celular = request.form.get('celular')
        celular2 = request.form.get('celular2')
        email = request.form.get('email')
        senha = request.form.get('senha')
        confirma_senha = request.form.get('confirma_senha')

    
        u = Usuario(nome, endereco, cidade, estado, cep, data_nascimento, cpf, rg, telefone, celular, celular2, email, senha, confirma_senha)
        db.session.add(u)
        db.session.commit()
        return redirect(url_for('usuarios.recovery' ))
    
@bp_pessoas.route('/pessoafisica_read', methods= ['GET'])
def read_fisica():
  usuarios = Usuario.query.all()
  
  return render_template('pessoafisica_read.html', usuarios = usuarios)
  


@bp_pessoas.route('/pessoafisica_update/<int:id>', methods=['GET', 'POST'])
def update_fisica(id):
  u = Usuario.query.get(id)
  
  if request.method =='GET':
    return render_template('pessoafisica_update.html', u = u)

  if request.method=='POST':
    nome = request.form.get('nome')
    endereco = request.form.get('endereco')
    cidade = request.form.get('cidade')
    estado = request.form.get('estado')
    cep = request.form.get('cep')
    data_nascimento = request.form.get('data_nascimento')
    cpf = request.form.get('cpf')
    rg = request.form.get('rg')
    telefone = request.form.get('telefone')
    celular = request.form.get('celular')
    celular2 = request.form.get('celular2')
    email = request.form.get('email')
    senha = request.form.get('senha')
    confirma_senha = request.form.get('confirma_senha')
    u.nome = nome
    u.endereco = endereco
    u.cidade = cidade
    u.estado = estado
    u.cep = cep
    u.data_nascimento = data_nascimento
    u.cpf = cpf
    u.rg = rg
    u.telefone = telefone
    u.celular = celular
    u.celular2 = celular2
    u.email = email
    u.senha = senha
    u.confirma_senha = confirma_senha

    db.session.add(u)
    db.session.commit()
    
    return redirect(url_for('pessoas.pessoafisica_read' ))



@bp_pessoas.route('/pessoafisica_delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
  u = Usuario.query.get(id)
  if request.method=='GET':
    return render_template('usuarios_delete.html', u = u)
    
  if request.method=='POST':
     db.session.delete(u)
     db.session.commit()
     return 'Dados excluídos com sucesso'
  


@bp_pessoas.route('/pessoajuridica_create', methods=['GET', 'POST'])
def create_juridica():
    if request.method == 'GET':
        return render_template('pessoajuridica_create.html')
    
         
    
