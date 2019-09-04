from flask import Blueprint


view_main = Blueprint('view_main', __name__, url_prefix='/confession')


@view_main.route('/')
def index():
    return ''