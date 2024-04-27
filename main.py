# chat conversation
import json
import pymysql
import requests
import http.client
import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

from itertools import cycle

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/", methods=["POST"])
@cross_origin()
def function(self):
    load_dotenv()
    DB_HOST = os.getenv("DB_HOST")
    DB_USER = os.getenv("DB_USER")
    DB_PASS = os.getenv("DB_PASS")
    DB_DDBB = os.getenv("DB_DDBB")
    #try:
    connection = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        database=DB_DDBB)
    cursor = connection.cursor()

    print("conexión exitosa")

    sql = '''
        update ZRZ2.blogs set
            titulo = "'''+str(request.json['titulo'])+'''",
            autor = "'''+str(request.json['autor'])+'''",
            tags = "'''+str(request.json['tags'])+'''",
            estado = "'''+str(request.json['estado'])+'''",
            texto = "'''+str(request.json['texto'])+'''",
            imagen = "'''+str(request.json['imagen'])+'''",
            fecha_publicacion = "'''+str(request.json['fecha_publicacion'])+'''",
            profesion_autor = "'''+str(request.json['profesion_autor'])+'''"
        WHERE id = %s;
    '''
    cursor.execute(sql, request.json['id'])
    connection.commit()
    retorno = {
        "detalle":"success!!"
        }
    return retorno

    #except Exception as e:
    #    print('Error: '+ str(e))
    #    retorno = {           
    #        "detalle":"algo falló", 
    #        "validacion":False
    #    }
    #    return retorno

if __name__ == "__main__":
    app.run(debug=True, port=8002, ssl_context='adhoc')