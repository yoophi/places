from flask.ext.api_app.database import BaseMixin

from places.database import db


class Place(db.Model, BaseMixin):
    title = db.Column(db.Unicode(255))
