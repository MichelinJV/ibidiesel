from flask import Flask, redirect, render_template, request, abort, session, url_for
from database import db
from flask_migrate import Migrate
from produtos import bp_produtos
from estoque import bp_estoque
from login import bp_login
from pessoas import bp_pessoas
from usuarios import bp_usuarios
from carrinho import bp_carrinho
from vendas import bp_vendas
from models import Produtos, Estoque, Usuario
from sqlalchemy import or_
from flask_login import LoginManager, current_user, login_required


app =Flask(__name__)

app.secret_key = 'sua_chave_secreta' 
app.config['SECRET_KEY'] = 'chave_entrada'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///bancoprojeto.db"
app.config['SQLALCHEMY_TRACKMODIFICATIONS'] = False
app.register_blueprint(bp_produtos, url_prefix='/produtos')
app.register_blueprint(bp_estoque, url_prefix='/estoque')
app.register_blueprint(bp_login, url_prefix='/login')
app.register_blueprint(bp_pessoas, url_prefix='/pessoas')
app.register_blueprint(bp_usuarios, url_prefix='/usuarios' )
app.register_blueprint(bp_carrinho, url_prefix='/carrinho')
app.register_blueprint(bp_vendas, url_prefix='/venda')


migrate = Migrate(app, db)
db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'  


@login_manager.user_loader
def load_user(user_id):    
  
    user = Usuario.query.get(int(user_id))
    return user
    

@app.route('/', methods=['GET', 'POST'])
def home():     
        
        resultado_produtos = []
        resultado_estoque = []

        if request.method == 'GET':
            produtos = Produtos.query.all() 
            estoque = Estoque.query.all()
            return render_template('index.html', produtos = produtos, estoque = estoque)
    
        
        if request.method == 'POST':
            pesquisa = request.form['pesquisa']
            resultado_produtos = Produtos.query.filter(
                or_(
                    Produtos.referencia.contains(pesquisa),
                    Produtos.descricao.contains(pesquisa),
                    Produtos.aplicacao.contains(pesquisa),
                )
                ).all()                    
            resultado_estoque = Estoque.query.filter(Estoque.referencia.contains(pesquisa)).all()
            return render_template('index.html', produtos = resultado_produtos, estoque = resultado_estoque)  


@app.route('/bemvindo')
@login_required
def bemvindo():
       
    identificador = current_user.nome    
    return render_template('bemvindo.html', identificador=identificador)
    

@login_manager.unauthorized_handler
def unauthorized():    
    return redirect(url_for('login.logar'))


    
if __name__ == '__main__':
    app.run(debug=True)