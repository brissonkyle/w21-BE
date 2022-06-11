from flask import Flask, Response, request
import mariadb
from dbcreds import *
import sys
from flask import jsonify
from helpers.db_helpers import run_query
# from helpers.db_helpers import run_query

app = Flask(__name__)


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
    run_query('SELECT * FROM animal')
    resp = []
    for animal in animal_list:
        an_obj : {}
        an_obj['animalId'] = animal[0]
        an_obj['animalName'] = animal[1]
        an_obj['imageUrl'] = animal[2]
        resp.append(an_obj)
    animal_list = ['bird']
    return jsonify(resp), 200


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
    run_query('INSERT INTO animal (name, imageUrl) VALUES (?,?)', [animalName, imageUrl])
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