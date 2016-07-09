# -*- coding: utf-8 -*-
from flask import jsonify

from places.blueprint import api
from .models import Place


@api.route('/place')
def place_list():
    """
    Sample
    ---
    tags:
      - Place
    security:
      - oauth:
        - email
    responses:
      200:
        description: OK
        schema:
          $ref: '#/definitions/CommonResult'
    """
    places = Place.query.all()
    return jsonify({'places': [{'id': p.id, 'title': p.title} for p in places]})
