from app import ma
from models.treino import Tipo_musculo, Musculo, Ficha, Exercicio, Ficha_exercicio, Serie, Treino

class Tipo_musculoSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Tipo_musculo
        include_fk = True

    id = ma.auto_field()
    nome = ma.auto_field()

class MusculoSchema(ma.SQLAlchemyAutoSchema):
    pass

class FichaSchema(ma.SQLAlchemyAutoSchema):
    pass

class ExercicioSchema(ma.SQLAlchemyAutoSchema):
    pass

class Ficha_exercicioSchema(ma.SQLAlchemyAutoSchema):
    pass

class SerieSchema(ma.SQLAlchemyAutoSchema):
    pass

class TreinoSchema(ma.SQLAlchemyAutoSchema):
    pass
