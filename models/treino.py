from app import db

class Tipo_musculo(db.Model):
    __tablename__ = "tipo_musculo"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(120), unique=True, nullable=False)

class Musculo(db.Model):
    __tablename__ = "musculo"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(120), unique=True, nullable=False)
    id_tipo_musculo = db.Column(db.Integer, db.ForeignKey('tipo_musculo.id'), nullable=False)

class Ficha(db.Model):
    __tablename__ = "ficha"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(30), unique=True)

class Exercicio(db.Model):
    __tablename__ = "exercicio"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(60), unique=True)
#    gif = db.Column(db.String(250), unique=True)
    id_musculo = db.Column(db.Integer, db.ForeignKey('musculo.id'), nullable=False)

class Ficha_exercicio(db.Model):
    __tablename__ = "ficha_exercicio"
    id_ficha = db.Column(db.Integer, db.ForeignKey('ficha.id'), nullable=False)
    id_exercicio = db.Column(db.Integer, db.ForeignKey('exercicio.id'), nullable=False)
    carga = db.Column(db.Integer)
    serie = db.Column(db.Integer)
    repeticoes = db.Column(db.Integer)

class Serie(db.Model):
    __tablename__ = "serie"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    serie = db.Column(db.Integer)
    repeticoes = db.Column(db.Integer) # 1 = True, 0 = false.  3x15
    data = db.Column(db.DateTime)

class Treino(db.Model):
    __tablename__ = "treino"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    id_aluno = db.Column(db.Integer, db.ForeignKey('aluno.id'), nullable=False)
    id_professor = db.Column(db.Integer, db.ForeignKey('professor.id'), nullable=False)
    id_ficha = db.Column(db.Integer, db.ForeignKey('ficha.id'), nullable=False)
    id_musculo = db.Column(db.Integer, db.ForeignKey('musculo.id'), nullable=False)
    id_serie = db.Column(db.Integer, db.ForeignKey('serie.id'), nullable=False)
    finalizada = db.Column(db.Boolean)