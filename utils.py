from flask import abort, redirect, url_for
from flask_login import  current_user

def admin_required(f):
    """Verifica se o usuário está logado e é admin."""
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.cpf=='11111111111':
            return redirect(url_for('login.logar'))
        return f(*args, **kwargs)
    return decorated_function