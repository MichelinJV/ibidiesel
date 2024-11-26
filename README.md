# <h1>IBIDIESEL</h1>
<h2>Projeto web usando flask/pyhton de um e-commerce de peças e produtos para veículos a diesel.</h2>

<h3>Como rodar o projeto: </h3>

crie ambiente virtual:
py -3 -m venv venv

ative o ambiente virtual:
.\venv\Scripts\activate

instale flask:
 pip install flask

setar a variável de ambiente app do flask:
$env:FLASK_APP = "main"

instale as bibliotecas:

pip install FLASK-SQLAlchemy

pip install FLASK-Migrate

pip install FLASK-Script 

pip install flask-login
 
crie as migration do banco de dados:
flask db init

crie o banco de dados: 
flask db migrate 

cria as tabelas: 
flask db upgrade

rode o projeto:
flask run
