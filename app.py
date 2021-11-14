from app import app
from flask import jsonify, request
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from models.pessoa import Pessoa, db
from schemas.pessoa import PessoaSchema

@app.route("/registry_user", methods=["POST"])
def registry():
    nome = request.json.get("nome", None)
    senha = request.json.get("senha", None)
    email = request.json.get("email", None)
    cpf = request.json.get("cpf", None)
    data_nasc = request.json.get("data_nasc", None)

    user = Pessoa(nome, email, senha, cpf, data_nasc)
    db.session.add(user)
    db.session.commit()

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

@app.route("/profile", methods=["GET"])
@jwt_required()
def profile():
    # Access the identity of the current user with get_jwt_identity
    email = get_jwt_identity()
    user = PessoaSchema()
    return user.dump(Pessoa(email=email)), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5001")