from datetime import datetime
from app import app
from flask import jsonify, request
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from models.pessoa import Pessoa, Aluno, Professor, db
from models.treino import Treino, Ficha, Ficha_exercicio, Serie
from schemas.pessoa import PessoaSchema
from schemas.treino import TreinoSchema
from werkzeug.security import generate_password_hash

@app.route("/cadastrar/usuario", methods=["POST"])
@jwt_required()
def cadastrar_usuario():
    email = get_jwt_identity()
    user = Pessoa.query.filter_by(email=email).first()
    teacher = Professor.query.filter_by(id_pessoa=user.id).first()
    if not teacher:
        return jsonify(error="Please select a Student User."), 412
    # Vars to commit
    nome = request.json.get("nome", None)
    senha = generate_password_hash(request.json.get("senha", None))
    email = request.json.get("email", None)
    cpf = request.json.get("cpf", None)
    data_nasc = request.json.get("data_nasc", None)
    usuario = request.json.get("usuario", None)

    # Insert User Table
    user = Pessoa(nome=nome, email=email, senha=senha, cpf=cpf, data_nasc=data_nasc)

    # Insert Aluno or Professor table
    if usuario == "aluno":
        # Vars
        inicio = request.json.get("inicio", None)
        meta = request.json.get("meta", None)
        objetivo = request.json.get("objetivo", None)

        # Insert User
        try:
            db.session.add(user)
            db.session.commit()
        except:
            return jsonify(error="Data existing or wrong."), 409
        # Insert Aluno
        aluno = Aluno(id_pessoa=user.id, inicio=inicio, meta=meta, objetivo=objetivo)
        db.session.add(aluno)
    elif usuario == "professor":
        # Insert User
        try:
            db.session.add(user)
            db.session.commit()
        except:
            return jsonify(error="Data existing or wrong."), 409
        # Insert Professor
        professor = Professor(id_pessoa=user.id)
        db.session.add(professor)
    else:
        return jsonify(error="Please chose a correct user type."), 403

    return jsonify(user_created=email), 200

@app.route("/cadastrar/musculo", methods=["POST"])
def cadastrar_musculo():
    pass

@app.route("/cadastrar/ficha", methods=["POST"])
def cadastrar_ficha():
    pass

@app.route("/cadastrar/exercicio", methods=["POST"])
def cadastrar_exercicio():
    pass

@app.route("/cadastrar/treino", methods=["POST"])
@jwt_required()
def cadastrar_treino():
    email = get_jwt_identity()
    trainner = Professor()
    trainner.check_professor(email)

    return "ok"

@app.route("/login", methods=["POST"])
def login():
    email = request.json.get("email", None)
    senha = request.json.get("senha", None)

    user = Pessoa.query.filter_by(email=email).first()
    if not user or not user.verify_password(senha):
        return jsonify({"msg": "Usuário ou senha inválida."}), 401

    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token)

@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    # Access the identity of the current user with get_jwt_identity
    email = get_jwt_identity()
    return jsonify(logged_in_as=email), 200

@app.route("/perfil", methods=["GET"])
@jwt_required()
def perfil():
    # Access the identity of the current user with get_jwt_identity
    email = get_jwt_identity()
    user_schema = PessoaSchema()
    user = Pessoa.query.filter_by(email=email).first()
    return user_schema.dump(user), 200

@app.route("/treino", methods=["GET"])
@jwt_required()
def treino():
    email = get_jwt_identity()
    user = Pessoa.query.filter_by(email=email).first()
    student = Aluno.query.filter_by(id_pessoa=user.id).first()
    if not student:
        return jsonify(error="Please select a Student User."), 412
    training_schema = TreinoSchema()
    training = Treino.query.filter_by(id_aluno=student.id)
    return training_schema.dump(training), 200

@app.route("/about", methods=["GET"])
def sobre():
    return jsonify(
        mestres="Danilo Urtado,"
                "Diego Vieira,"
                "Felipe Maeda,"
                "Jose Souza,"
                "Lucas Cassiano,"
                "Vitor R. Jorge",
        projeto="backend=https://github.com/FelipeMaeda/Guppi-back-end, frontend=https://github.com/TecnoJhow/AppGuppi"
    ), 200

@app.route("/treinamento/salvar", methods=["GET"])
def treinamento_salvar():
    nm_maquina = request.args.get('nm_maquina')
    repeticoes = request.args.get('repeticoes')
    sensor_giroscopio = request.args.get('sensor_giroscopio')
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    serie = Serie(nm_maquina=nm_maquina, repeticoes=repeticoes, sensorgiroscopio=sensor_giroscopio, data=now)
    db.session.add(serie)
    db.session.commit()
    return "ok", 200

@app.route("/token/maquina", methods=["GET"])
@jwt_required()
def token_maquina():
    email = get_jwt_identity()
    user = Pessoa.query.filter_by(email=email).first()
    student = Aluno.query.filter_by(id_pessoa=user.id).first()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5001")