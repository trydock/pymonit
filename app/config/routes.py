from flask import Blueprint, render_template

config = Blueprint('config', __name__, template_folder='templates', static_folder='static')

@config.route('/config')
def index():
    return "Config page"
