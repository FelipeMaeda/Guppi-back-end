class Estado(db.Model):
    id_estado = db.Column(db.Integer, primary_key=True)
    UF = db.Column(db.String(2), unique=True, nullable=False)

# class Cidade(db.Model):
#     id_cidade = db.Column(db.Integer, primary_key=True)
#     nome = db.Column(db.String(120)
#     unique = True, nullable = False)
#     id_estado = db.Column(db.Integer, db.ForeignKey('estado.id_estado'), nullable=False)
#
# class Bairro(db.Model):
#     id_bairro = db.Column(db.Integer, primary_key=True)
#     nome = db.Column(db.String(120), unique=False, nullable=False)
#     id_cidade = db.Column(db.Integer, db.ForeignKey(cidade.id_cidade), nullable=False)
#
# class Logradouro(db.Model):
#     id_logradouro = db.Column(db.Integer, primary_key=True)
#     nome = db.Column(db.String(200), nullable=False, unique=False)
#     complemento = db.Column(db.String(10), nullable=True, unique=False)
#     id_bairro = db.Column(db.Integer, db.ForeignKey(bairro.id_bairro), nullable=False)
#
# class Endereco(db.Model):
#     id_endereco = db.Column(db.Integer, primary_key=True)
#     nome = db.Column(db.String(40), nullable=False, unique=False)
#     id_logradouro = db.Column(db.Integer, db.ForeignKey(logradouro.id_logradouro), nullable=False)
#
