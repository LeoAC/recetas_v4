from flask import jsonify, request # me perfmite recuperar info...
from app.models import Receta

def get_all_recetas():     
    recetas = Receta.get_all()                                
    return jsonify([receta.serialize() for receta in recetas]) 

def get_receta(receta_id):
    receta =  Receta.get_by_id(receta_id)
    if not receta:
        return jsonify({'message': 'Receta not found'}), 404    
    return jsonify(receta.serialize())

def create_receta():
    data = request.json    
    new_receta = Receta(None,data['name'],data['ingredientes'],data['descripcion'],data['cheff'],data['precio'])
    new_receta.save()
    response = {'message':'Creanto pelicula'}  # Esto es un diccionario.
    return jsonify(response), 201 # puedo definir yo un codigo q comunica al fron el resultado si grabo bien o un err.  

def update_receta(receta_id): 
    receta = Receta.get_by_id(receta_id)
    if not receta:
        return jsonify({'message': 'Receta not found'}), 404
    data = request.json
    receta.name = data['name']
    receta.ingredientes = data['ingredientes']
    receta.descripcion = data['descripcion']
    receta.cheff = data['cheff']
    receta.precio = data['precio']
    receta.save()
    return jsonify({'message': 'Receta updated successfully'})

def delete_receta(receta_id):
    receta = Receta.get_by_id(receta_id)
    if not receta:
        return jsonify({'message': 'Receta not found'}), 404
    receta.delete()
    return jsonify({'message': 'Receta deleted successfully'})