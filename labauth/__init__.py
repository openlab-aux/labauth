from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.restful import Resource, Api

app = Flask(__name__)

import appconfig
app.config.from_object(appconfig)

db = SQLAlchemy(app)
admin = Admin(app)

from labauth.models import Human, Machine

admin.add_view(ModelView(Human, db.session))
admin.add_view(ModelView(Machine, db.session))

from labauth.models import *

from labauth.api import *
