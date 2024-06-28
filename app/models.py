from app.database import get_db

class Receta:
    # Receta(None,data['name'],data['ingredientes'],data['descripcion'],data['cheff'],data['precio'])
    # Constructor
    def __init__(self, id_receta=None,name=None,ingredientes=None,
                 descripcion=None,cheff=None, precio=None):
        self.id_receta = id_receta
        self.name = name
        self.ingredientes = ingredientes
        self.descripcion = descripcion
        self.cheff = cheff
        self.precio = precio
    # Metodos de la clase movie
    def serialize(self): # Convierte un objeto de la clase movie en un diccionario como yo lo defina.
        return{
            'id_receta':self.id_receta,
            'name':self.name,
            'ingredientes':self.ingredientes,
            'descripcion':self.descripcion,
            'cheff':self.cheff,
            'precio':self.precio,
        }
     
    # llamado "decorador"    
    @staticmethod # Metodo estatico q me permite ejecutarlo sin instanciar...
    def get_all():
        # Logica de buscar en la db todas las peliculas.
        db = get_db()
        cursor = db.cursor()
        query = "Select * from db_cac_recetas_163.recetas"
        cursor.execute(query)
        # Obtengo resultados
        rows = cursor.fetchall() # la base devuelve tuplas
        # 3° ejemplo (movies serializado)
        movies = [Receta(id_receta=row[0], name=row[1], 
                        ingredientes=row[2], descripcion=row[3],
                        cheff=row[4],precio=row[5]) for row in rows]        
        # Cerramos el cursor
        cursor.close()
        # return rows       # 2° ejemplo
        return movies # 3° ejemplo

    # ESTE METODO NO ES ESTATICO como en get_all
    def save(self):
        db = get_db()
        cursor = db.cursor()
        if self.id_receta:
            # De esta forma es mas segura q con un f"string". ver clase 33
            cursor.execute("""
                UPDATE db_cac_recetas_163.recetas SET name = %s, ingredientes = %s, descripcion = %s, cheff = %s, precio = %s
                WHERE id_receta = %s
            """, (self.name, self.ingredientes, self.descripcion, self.cheff, self.precio, self.id_receta))
        else:
            cursor.execute("""
                INSERT INTO db_cac_recetas_163.recetas (name, ingredientes, descripcion, cheff, precio) VALUES (%s, %s, %s, %s, %s)
            """, (self.name, self.ingredientes, self.descripcion, self.cheff, self.precio))
            #voy a obtener el último id generado
            self.id_receta = cursor.lastrowid
        db.commit() #confirmar la accion
        cursor.close()
    
    @staticmethod
    def get_by_id(receta_id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM db_cac_recetas_163.recetas WHERE id_receta = %s", (receta_id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Receta(id_receta=row[0], name=row[1], ingredientes=row[2], descripcion=row[3], cheff=row[4], precio=row[5])
        return None

    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM db_cac_recetas_163.recetas WHERE id_receta = %s", (self.id_receta,))
        db.commit()
        cursor.close()