import os
import mysql.connector
from flask import g # Actua como un espacio de almacenador global de forma temporal.
from dotenv import load_dotenv # Carga las variables de entorno q estan en el archivo .env

# Cargar variables de entorno desde el archivo .env
load_dotenv()

DATABASE_CONFIG = {
    'user': os.getenv('DB_USERNAME'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_NAME'),
    'port': os.getenv('DB_PORT', 3306)  # puerto predeterminado es 3306 si no se especifica
}
# Funcion para obtener la conecxión a la base de datos.
# ...
def get_db(): 
    # si 'db' no esta en el contexto global de Flask 'g'
    if 'db' not in g:
        # Crear ....
        g.db = mysql.connector.connect(**DATABASE_CONFIG)
    # . . .
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()
# . . . 
def init_app(app):
    # . . .
    app.teardown_appcontext(close_db)