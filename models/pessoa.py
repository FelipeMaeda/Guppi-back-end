from app import db

class Academia(db.Model):
    __tablename__ = "academia"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(60), nullable=False)
    cnpj = db.Column(db.String(14), nullable=False, unique=True)
    quant_aluno = db.Column(db.Integer)
    id_endereco = db.Column(db.Integer, db.ForeignKey('endereco.id'), nullable=False)

class Pessoa(db.Model):
    __tablename__ = "pessoa"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(60), nullable=False, unique=True)
    senha = db.Column(db.String(300), nullable=False)
    cpf = db.Column(db.String(11), nullable=False, unique=True)
    data_nasc = db.Column(db.DateTime)
    id_endereco = db.Column(db.Integer, db.ForeignKey('endereco.id'), nullable=False)
    id_academia = db.Column(db.Integer, db.ForeignKey('academia.id'), nullable=False)
    status = db.Column(db.Boolean, nullable=False)

    # Authentication Flask JWT Extended
    def __init__(self, nome, email, senha, cpf, data_nasc):
        self.nome = nome
        self.email = email
        self.senha = generate_password_hash(senha)
        self.cpf = cpf
        self.data_nasc = data_nasc

    def verify_password(self, senha):
        return check_password_hash(self.senha, senha)

    def __repr__(self):
        return f"<User : {self.nome} >"

class Aluno(db.Model):
    __tablename__ = "aluno"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    id_pessoa = db.Column(db.Integer, db.ForeignKey('pessoa.id'), nullable=False)
    inicio = db.Column(db.DateTime)
    meta = db.Column(db.Float)
    objetivo = db.Column(db.String(15))

class Professor(db.Model):
    __tablename__ = "professor"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    id_pessoa = db.Column(db.Integer, db.ForeignKey('pessoa.id'), nullable=False)