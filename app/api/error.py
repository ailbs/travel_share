from flask import jsonify

def _404(error):
    return jsonify({'message': '404~~~~~~~'}), 404


