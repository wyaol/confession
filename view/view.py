import logging
from flask import Blueprint, render_template, request
from controller import control


logger = logging.getLogger('request_logger')


view_main = Blueprint('view_main', __name__, url_prefix='/confession')


@view_main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        email = request.form.get('email', '')
        name = request.form.get('name', '')
        sex = request.form.get('sex', '')
        o_email = request.form.get('o_email', '')
        o_name = request.form.get('o_name', '')
        try:
            control.email_send_confession(email, name, sex, o_email, o_name)
            return render_template('success.html')
        except Exception as e:
            logger.error('args: %s, error info: %s', str({
                'email': email,
                'name': name,
                'sex': sex,
                'o_email': o_email,
                'o_name': o_name
            }), str(e))
            return render_template('error.html')
    return render_template('error.html')