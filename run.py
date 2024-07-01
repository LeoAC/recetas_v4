from flask import Flask
from app.views import *
from app.database import init_app
from flask_cors import CORS

app = Flask(__name__) 
init_app(app)
CORS(app) 

app.route('/api/recetas/',methods=['GET'])(get_all_recetas) # Obtener todas las peliculas
app.route('/api/recetas/',methods=['POST'])(create_receta)    # Crear la pelicula
app.route('/api/recetas/<int:receta_id>',methods=['GET'])(get_receta)           # Obtener pelicula
app.route('/api/recetas/<int:receta_id>',methods=['PUT'])(update_receta)        # Actualizar la pelicula
app.route('/api/recetas/<int:receta_id>',methods=['DELETE'])(delete_receta)        # Eliminar la pelicula

if __name__ == '__main__': 
    app.run(debug=True) 
