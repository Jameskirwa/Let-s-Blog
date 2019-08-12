from flask import Blueprints

auth = Blueprint('auth',__name__)

from . import views,forms