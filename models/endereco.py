from app import db

class Estado(db.Model):
    __tablename__ = "estado"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    UF = db.Column(db.String(2), nullable=False, unique=True)

class Cidade(db.Model):
    __tablename__ = "cidade"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(120), unique=True, nullable=False)
    id_estado = db.Column(db.Integer, db.ForeignKey('estado.id'), nullable=False)

class Bairro(db.Model):
    __tablename__ = "bairro"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(120), unique=True, nullable=False)
    id_cidade = db.Column(db.Integer, db.ForeignKey('cidade.id'), nullable=False)

class Logradouro(db.Model):
    __tablename__ = "logradouro"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(120), unique=True, nullable=False)
    complemento = db.Column(db.String(10))
    id_bairro = db.Column(db.Integer, db.ForeignKey('bairro.id'), nullable=False)

class Endereco(db.Model):
    __tablename__ = "endereco"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(120))
    id_logradouro = db.Column(db.Integer, db.ForeignKey('logradouro.id'), nullable=False)
