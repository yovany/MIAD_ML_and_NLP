#!/usr/bin/python
from flask import Flask
from flask_restplus import Api, Resource, fields
import joblib
from predice_precio_model_deployment import predice_precio

# Definición aplicación Flask
app = Flask(__name__)

# Definición API Flask
api = Api(
    app,
    version='1.0',
    title='API de Predicción de Precios de Autos',
    description='API de Predicción de Precios de Autos')

ns = api.namespace('predict',
     description='Regresión de Precio de Auto')

# Definición argumentos o parámetros de la API
parser = api.parser()

parser.add_argument(
    'Year',
    type=int,
    required=True,
    help='Año del modelo',
    location='args')

parser.add_argument(
    'Mileage',
    type=int,
    required=True,
    help='Millas recorridas',
    location='args')

parser.add_argument(
    'State',
    type=str,
    required=True,
    help='Estado de procedencia',
    location='args')

parser.add_argument(
    'Make',
    type=str,
    required=True,
    help='Marca de la ensambladora de auto',
    location='args')

parser.add_argument(
    'Model',
    type=str,
    required=True,
    help='Sub marca del auto',
    location='args')

resource_fields = api.model('Resource', {
    'result': fields.String,
})

@ns.route('/')
class PhishingApi(Resource):

    @api.doc(parser=parser)
    @api.marshal_with(resource_fields)
    def get(self):
        args = parser.parse_args()
        print(args)
        return {
         "result": predice_precio(args['Year'],args['Mileage'],args['State'],args['Make'],args['Model'])
        }, 200

app.run(debug=True, use_reloader=False, host='0.0.0.0', port=8888)
