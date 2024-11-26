from database import db
from flask_login import UserMixin

class Produtos(db.Model):
    __tablename__ = "produtos"
    id = db.Column(db.Integer, primary_key = True)
    referencia = db.Column(db.Integer)
    valor = db.Column(db.Numeric(10,2))    
    descricao = db.Column(db.String(255))
    aplicacao = db.Column(db.String(255))
    foto = db.Column(db.LargeBinary)
    

    def __init__(self, referencia, valor, descricao, aplicacao, foto):
        self.referencia = referencia
        self.valor = valor        
        self.descricao = descricao
        self.aplicacao = aplicacao
        self.foto = foto

    def __repr__(self):
        return "Número de Referência do Produto: {}.format(self.referencia)"
    

class Estoque(db.Model):
    __tablename__ = "estoque"
    id = db.Column(db.Integer, primary_key = True)
    referencia = db.Column(db.Integer)        
    quantidade = db.Column(db.Integer)
    produto_id = db.Column(db.Integer, db.ForeignKey('produtos.id'))
    categoria = db.relationship('Produtos', backref=db.backref('estoque', lazy=True))   
    
    
    def __init__(self, produto_id, referencia, quantidade):
        self.produto_id = produto_id  
        self.referencia = referencia
        self.quantidade = quantidade             
        

    def __repr__(self):
        return "Número de Referência do Produto: {} Quantidade no estoque: {}.format(self.referencia, self.quantidade)" 
    

class Usuario(UserMixin, db.Model):
    __tablename__ = "usuario"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    endereco = db.Column(db.String(100))
    cidade = db.Column(db.String(100))
    estado = db.Column(db.String(100))
    cep = db.Column(db.String(100))    
    cpf = db.Column(db.String(20), nullable=True)
    cnpj = db.Column(db.String(20), nullable=True)   
    telefone = db.Column(db.String(100), nullable=True)
    celular = db.Column(db.String(100))    
    email = db.Column(db.String(100), unique=True, nullable=False)    
    senha = db.Column(db.String(100))
    confirma_senha = db.Column(db.String(100))   
    


    def __init__(self, nome, endereco, cidade, estado, cep, cpf, cnpj, telefone, celular, email, senha, confirma_senha):
      self.nome = nome
      self.endereco = endereco
      self.cidade = cidade
      self.estado = estado
      self.cep = cep      
      self.cpf = cpf
      self.cnpj = cnpj
      self.telefone = telefone
      self.celular = celular      
      self.email = email
      self.senha = senha
      self.confirma_senha = confirma_senha       
        

    @property
    def is_active(self):
     return True

    @property
    def is_authenticated(self):
     return True  

    def __repr__(self):
      return "Usuario: {}".format(self.nome) 

   
    

class Carrinho(UserMixin,db.Model):
  __tablename__ = "carrinho"
  id = db.Column(db.Integer, primary_key=True)
  quantidade = db.Column(db.Integer, nullable=False)
  preco_total = db.Column(db.Float, nullable=False)
  produto_id = db.Column(db.Integer, db.ForeignKey('produtos.id'), nullable=False)
  us_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)  
  produto = db.relationship('Produtos', backref=db.backref('carrinho', lazy=True))

  def __init__(self, quantidade, preco_total, produto_id, us_id):
    self.quantidade = quantidade
    self.preco_total = preco_total
    self.produto_id = produto_id
    self.us_id = us_id

  @property
  def is_active(self):
    return True

  @property
  def is_authenticated(self):
    return True  
       

class ItemVenda(UserMixin, db.Model):
    __tablename__ = "itemvenda"
    id = db.Column(db.Integer, primary_key=True)  
    user_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)  
    produto_id = db.Column(db.Integer, db.ForeignKey('produtos.id'), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)    

    def __init__(self, user_id, produto_id, quantidade): 
      self.user_id = user_id     
      self.produto_id = produto_id
      self.quantidade = quantidade
     
    
    @property
    def is_active(self):
     return True

    @property
    def is_authenticated(self):
     return True  
       

 
