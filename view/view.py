import logging
from service.tools import json_data
from flask import Blueprint, render_template, request
from controller import control


logger = logging.getLogger('request_logger')


view_main = Blueprint('view_main', __name__, url_prefix='/confession')


@view_main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        data = request.get_json()
        email = data.get('email', '')
        name = data.get('name', '')
        sex = data.get('sex', '')
        o_email = data.get('o_email', '')
        o_name = data.get('o_name', '')
        code = data.get('code', '')
        try:
            control.email_send_confession(email, name, sex, o_email, o_name, code)
            return json_data({
                'success': True
            })
        except Exception as e:
            logger.error('args: %s, error info: %s', str({
                'email': email,
                'name': name,
                'sex': sex,
                'o_email': o_email,
                'o_name': o_name
            }), str(e))
            return json_data({
                'success': False,
                'message': str(e)
            })


@view_main.route('/get_code', methods=['POST'])
def get_code():
    data = request.get_json()
    email = data.get('email', '')
    try:
        control.email_send_code(email)
        return json_data({'success': True})
    except Exception as e:
        logger.error(
            'args: %s,  error: %s' % (
                str({
                    'email': email
                }),
                str(e)
            )
        )
        return json_data({'success': False})


@view_main.route('verify_code', methods=['POST'])
def verify_code():
    data = request.get_json()
    email = data.get('email', '')
    code = data.get('code', '')
    return json_data({
        'success': control.verify_code(email, code)
    })


@view_main.route('success', methods=['GET'])
def success():
    return render_template('success.html')