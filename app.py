from flask import Flask, Response, request
import mariadb
from dbcreds import *
import sys
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
    return jsonify('Animal added'), 201

if len(sys.argv) > 1:
    mode = sys.argv[1]
else:
    print('Missing required arguments')
    exit

if mode == 'testing':
    from flask_cors import CORS
    CORS(app)
    app.run(debug=True)
elif mode == 'production':
    import bjoern
    bjoern.run(app, '0.0.0.0', 5005)
else :
    print('Mode must be in testing/production')
    exit()