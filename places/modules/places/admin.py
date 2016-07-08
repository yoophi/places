from flask.ext.admin.contrib import sqla

from places.database import db
from places.extensions import admin
from .models import Place

admin.add_view(sqla.ModelView(Place, db.session))
