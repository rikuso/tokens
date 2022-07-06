# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 23:27:13 2022

@author: Daniel
"""

from flask import Flask
import os
from flask  import request
from jose import jwt
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World Token!"

@app.route("/crear-token")
def crear():
    
    id_usuario = request.args.get("id")
    rolId = request.args.get("rolId") 
    try:
        secret = os.environ.get("JWT_SECRET_KEY")
        token = jwt.encode({'id': id_usuario, 'rolId':rolId}, secret, algorithm='HS256')
        return {'token':token}
    except Exception as e:
        return {"response": "KO", "toke":""}
    else:
        print("Sin Hash")
        return "has error"
    
@app.route("/verificar-token")
def validar():
    
    token = request.args.get("token")
    rol = request.args.get("rol") 
    try:
        secret = os.environ.get("JWT_SECRET_KEY")
        token = jwt.decode(token, secret , algorithms=['HS256'])
        return 'ok'
    except Exception as e:
        return "ko"

if __name__ == "__main__":
    app.run(host="localhost",port=5001)