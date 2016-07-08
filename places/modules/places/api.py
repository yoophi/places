from flask import jsonify

from places.blueprint import api
from .models import Place


@api.route('/place')
def place_list():
    places = Place.query.all()
    return jsonify({'places': [{'id': p.id, 'title': p.title} for p in places]})
