# ibidiesel
Projeto web usando flask/pyhton de um e-commerce de peças e produtos para veículos a diesel.

Como rodar o projeto: 

crie ambiente virtual:
py -3 -m venv venv

ative o ambiente virtual:
.\venv\Scripts\activate

instale flask
 pip install flask

setar a variável de ambiente app do flask
$env:FLASK_APP = "main"

instale gerenciador os bibliotecas
pip install FLASK-SQLAlchemy

pip install FLASK-Migrate

pip install FLASK-Script 

pip install flask-login
 
crie as migration do banco de dados
flask db init

crie o banco de dados 
flask db migrate 

cria as tabelas 
flask db upgrade

rode o projeto
flask run
