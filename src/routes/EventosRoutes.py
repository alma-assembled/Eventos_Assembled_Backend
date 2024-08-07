from flask import Blueprint, request, jsonify

# Logger
from src.utils.Logger import Logger
# Services
from src.services.eventos import EventosService
from src.schemas.evento import eventos_schema
#from flask_cors import cross_origin

main = Blueprint('eventos_blueprint', __name__)

#@cross_origin(origins='*')
@main.route('/', methods=['GET'])
def get_eventos():
    try:
        eventos = EventosService.get_eventos()
        if (len(eventos) > 0):
            return jsonify({'Data': eventos, 'message': "SUCCESS", 'success': True})
        else:
            return jsonify({'message': "NOTFOUND", 'success': True})
    except Exception as ex:
        Logger.add_to_log("er:" , f"Error routes gets: {str(ex)}")
        print(ex)
        return jsonify({'message': "ERROR", 'success': False})

#@cross_origin(origins='http://192.168.1.200:3000')
@main.route('/', methods=['POST'])
def post_create_empleado():
    try:
        data = request.json
        print(data,"data")
        errors = eventos_schema.validate(data)
        
        if errors:
            return jsonify(errors), 400
        
        evento = EventosService.save_evento(data)
        if evento:
            return jsonify({'success': True})
        else:
            return jsonify({'message': "Error al guardar el evento", 'success': False}), 500
    except Exception as ex:
        Logger.add_to_log(f"Error routes POSTEmpleados: {str(ex)}")
        return jsonify({'message': "ERROR", 'success': False}), 500

#@cross_origin(origins='http://192.168.1.200:3000')
@main.route('/<int:id_evento>', methods=['PUT'])
def editar_evento(id_evento):    
    try:
        evento_data = request.json
        if EventosService.update_evento(id_evento, evento_data):
            return jsonify({"message": "Evento actualizado correctamente"}), 200
        else:
            return jsonify({"message": "Error al actualizar el evento"}), 500
    except Exception as ex:
        Logger.add_to_log(f"Error: {str(ex)}")
        return jsonify({'message': "ERROR", 'success': False}), 500

#@cross_origin(origins='http://192.168.1.200:3000')
@main.route('/baja-evento/<int:id_evento>', methods=['PUT'])
def put_baja_evento(id_evento):
        try:
            empleado = EventosService.baja_evento(id_evento)
            if empleado:
                return jsonify({'success': True})
            else:
                return jsonify({'message': "Error al dar de baja el evento", 'success': False}), 500
        except Exception as ex:
            Logger.add_to_log(f"Error routes baja: {str(ex)}")
            return jsonify({'message': "ERROR", 'success': False}), 500