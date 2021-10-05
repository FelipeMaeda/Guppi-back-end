# class Academia(db.Model):
#     id_academia = db.Column(db.Integer, primary_key=True)
#     nome = db.Column(db.String(60), nullable=False)
#     cnpj = db.Column(db.String(14), nullable=False, unique=True)
#     quant_aluno = db.Column(db.Integer, nullable=True)
#     id_endereco = db.Column(db.Integer, db.ForeignKey('endereco.id_endereco'), nullable=False)
