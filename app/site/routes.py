from flask import Blueprint, render_template

site = Blueprint('site', __name__, template_folder='templates', static_folder='static')

@site.route('/')
def index():
    return "Hello Guys"
