from flask import Blueprint, flash, redirect, render_template, request, session, url_for
import io
from models import Usuario
from flask_login import  LoginManager, login_user, login_required, logout_user

bp_login = Blueprint("login", __name__, template_folder= "templates")

@bp_login.route("/logar",  methods=['GET', 'POST'])
def logar():
    if request.method == 'GET':
        return render_template('login.html')
    
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']       
                               
          
        user = Usuario.query.filter_by(email=email).first()
        
        
        if user and user.senha == senha:
            login_user(user)            
            return redirect(url_for('bemvindo'))
        else:
            return render_template('credenciaisinvalidas.html')
    return render_template('login.html')


@bp_login.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login.logar'))


