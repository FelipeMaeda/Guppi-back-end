from app import ma
from models.endereco import Estado, Cidade, Bairro, Logradouro, Endereco

class EstadoSchema(ma.SQLAlchemyAutoSchema):
    pass

class CidadeSchema(ma.SQLAlchemyAutoSchema):
    pass

class BairroSchema(ma.SQLAlchemyAutoSchema):
    pass

class LogradouroSchema(ma.SQLAlchemyAutoSchema):
    pass

class EnderecoSchema(ma.SQLAlchemyAutoSchema):
    pass
