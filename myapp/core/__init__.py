from flask import Blueprint
import barebones

bp = Blueprint('core', 'barebones', template_folder='core/templates')
import views.login_view

