from flask import Flask, Response, request
import mariadb
from dbcreds import *
from flask import jsonify
from helpers.db_helpers import run_query

app = Flask(__name__)
conn = None
cursor = None

conn = mariadb.connect(
                    user=user,
                    password=password,
                    host=host,
                    port=port,
                    database=database
                    )

@app.get('/api/animals')
def animals_get():
    # TODO : DB SELECT
    animal_list = []
    return jsonify(animal_list), 200


@app.post('/api/animals')
def animals_post():
    user_response = request.json
    animalName = user_response.get('animalName')
    imageUrl = user_response.get('imageUrl')
    if not animalName:
        return jsonify('Missing required arguments animalName'), 422
    if not imageUrl:
        return jsonify('Missing required argument imageUrl'), 422
    # TODO : ERROR CHECK THE VALUES FOR THE ARGUMENTS 
    # TODO : DB WRITE
