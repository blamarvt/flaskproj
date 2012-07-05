from flask import Blueprint
import medphoto

bp = Blueprint('core', 'medphoto', template_folder='core/templates')
import views.login_view

