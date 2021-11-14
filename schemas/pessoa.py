from app import ma
from models.pessoa import Academia, Pessoa, Professor, Aluno

class AcademiaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Academia
        include_fk = True

    id = ma.auto_field()
    nome = ma.auto_field()
    cnpj = ma.auto_field()
    quant_aluno = ma.auto_field()
    id_endereco = ma.auto_field()

class PessoaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Pessoa

    id = ma.auto_field()
    nome = ma.auto_field()
    email = ma.auto_field()
    cpf = ma.auto_field()
    data_nasc = ma.auto_field()
    id_endereco = ma.auto_field()
    id_academia = ma.auto_field()
    status = ma.auto_field()

class AlunoSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Aluno
        include_fk = True

    id = ma.auto_field()
    id_pessoa = ma.auto_field()
    inicio = ma.auto_field()
    meta = ma.auto_field()
    objetivo = ma.auto_field()

class ProfessorSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Professor
        include_fk = True

    id = ma.auto_field()
    id_pessoa = ma.auto_field()
