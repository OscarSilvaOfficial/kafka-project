from flask import jsonify 
import jsonpickle

def set_to_json(str):
    return jsonify(jsonpickle.encode(str))