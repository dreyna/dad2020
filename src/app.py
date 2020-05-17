from flask import Flask, jsonify, request,make_response
from flask_restful import Resource, Api, reqparse
from sqlalchemy import create_engine
from json import dumps
from UsuarioDAO import Usuario
user = Usuario()
app = Flask(__name__)

@app.route('/', methods=['GET'])
def listar():
    return jsonify({'mensaje':'Bienvenidos a Flask'})
@app.route('/listar', methods=['GET'])
def users():
    try:
        rows = user.readAll()
        respuesta = jsonify(rows)
        respuesta.status_code=200
        return respuesta
    except Exception as e:
        print(e)


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
    