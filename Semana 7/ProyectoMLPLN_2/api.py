import joblib
import werkzeug
# from werkzeug.utils import cached_property

import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
import flask_restful 
from flask import Flask


try:
    from flask_restplus import Api, Resource, fields, marshal
except ImportError:
    import werkzeug
    werkzeug.cached_property = werkzeug.utils.cached_property
    from flask_restplus import Resource, Api, fields, marshal

from predice_generos import predice_GENEROS

# Definición aplicación Flask
app = Flask(__name__)

# Definición API Flask
api = Api(
    app, 
    version='1.0', 
    title='API de Predicción de Generos de Peliculas',
    description='API de Predicción de Generos de Peliculas')

ns = api.namespace('predict', 
     description='Predición de Generos de Peliculas')

# Definición argumentos o parámetros de la API
parser = api.parser()



parser.add_argument(
    'Plot', 
    type=str, 
    required=True, 
    help='', 
    location='args')


resource_fields = api.model('Resource', {
    'p_Action': fields.String,
    'p_Adventure' : fields.String,
    'p_Animation' : fields.String,
    'p_Biography' : fields.String,
    'p_Comedy' : fields.String,
    'p_Crime' : fields.String,
    'p_Documentary' : fields.String,
    'p_Drama' : fields.String,
    'p_Family' : fields.String,
    'p_Fantasy' : fields.String,       
    'p_Film-Noir' : fields.String,
    'p_History' : fields.String,
    'p_Horror' : fields.String,
    'p_Music' : fields.String,
    'p_Mystery' : fields.String,
    'p_News' : fields.String,
    'p_Romance' : fields.String,
    'p_Sci-Fi' : fields.String,
    'p_Short' : fields.String,
    'p_Sport' : fields.String,
    'p_Thriller' : fields.String,
    'p_War' : fields.String,
    'p_Western' : fields.String
    })

# Definición de la clase para disponibilización
@ns.route('/')
class GenerosApi(Resource):

    @api.doc(parser=parser)
    @api.marshal_with(resource_fields)
    def get(self):
        args = parser.parse_args()
        print(args)
        generos=predice_GENEROS([args['Plot']])
        return {
        'p_Action': generos['p_Action'],
        'p_Adventure' : generos['p_Adventure'],
        'p_Animation' : generos['p_Animation'],
        'p_Biography' : generos['p_Biography'],
        'p_Comedy' : generos['p_Comedy'],
        'p_Crime' : generos['p_Crime'],
        'p_Documentary' : generos['p_Documentary'],
        'p_Drama' : generos['p_Drama'],
        'p_Family' : generos['p_Family'],
        'p_Fantasy' : generos['p_Fantasy'],       ''
        'p_Film-Noir' : generos['p_Film-Noir'],
        'p_History' : generos['p_History'],
        'p_Horror' : generos['p_Horror'],
        'p_Music' : generos['p_Music'],
        'p_Mystery' : generos['p_Mystery'],
        'p_News' : generos['p_News'],
        'p_Romance' : generos['p_Romance'],
        'p_Sci-Fi' : generos['p_Sci-Fi'],
        'p_Short' : generos['p_Short'],
        'p_Sport' : generos['p_Sport'],
        'p_Thriller' : generos['p_Thriller'],
        'p_War' : generos['p_War'],
        'p_Western' : generos['p_Western']
        }, 200
# Ejecución de la aplicación que disponibiliza el modelo de manera local en el puerto 8888
app.run(debug=True, use_reloader=False, host='0.0.0.0', port=8888)
