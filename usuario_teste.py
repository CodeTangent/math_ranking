# Esse usuário é exlusivamente para testes iniciais de login
# Usar parâmetro de requisição para testes: GET
# Se quiser testar com POST usar linha comentada que deixei no código

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

credenciais_do_usuario = {"email": "user", "password": "123"}


@app.route("/login", methods=["POST"])
#@app.route("/login")
def login():
    dados_do_usuario = request.json

    if (
        dados_do_usuario.get["email"] == credenciais_do_usuario["email"] 
        and dados_do_usuario.get["password"] == credenciais_do_usuario["password"]
        
    ):
        return jsonify(True)
    return jsonify(False)

app.run(port=5500)
