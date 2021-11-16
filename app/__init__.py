from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Flask Config and declaration
app = Flask(__name__)
app.config.from_pyfile('config.py')

# Flask SQLAlchemy and Marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Flask JWT Extended
jwt = JWTManager(app)

# Migrate database
from models.endereco import Estado, Cidade, Bairro, Logradouro, Endereco
from models.pessoa import Academia, Pessoa, Aluno, Professor
from models.treino import Treino, Tipo_musculo, Musculo, Ficha, Ficha_exercicio, Exercicio, Serie, Token
migrate = Migrate(app, db)
migrate.init_app(app, db)