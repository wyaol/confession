import logging
from service.tools import json_data
from flask import Blueprint, render_template, request
from controller import control
from exceptions.custom_exception import BlockTimeException
from config import service_config


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
            control.email_send_info(email, name, sex, o_email, o_name, code)
            return json_data({
                'success': True,
                'code': service_config.CODE_SUCCESS
            })
        except BlockTimeException as e:
            return json_data({
                'success': False,
                'code': service_config.CODE_BLOCK,
                'block_time': e.rest_time
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
                'code': service_config.CODE_FAIL,
                'message': str(e)
            })


@view_main.route('/get_code', methods=['POST'])
def get_code():
    data = request.get_json()
    email = data.get('email', '')
    try:
        control.email_send_code(email)
        return json_data({'success': True, 'code': service_config.CODE_SUCCESS})
    except Exception as e:
        logger.error(
            'args: %s,  error: %s' % (
                str({
                    'email': email
                }),
                str(e)
            )
        )
        return json_data({'success': False, 'code': service_config.CODE_FAIL})


@view_main.route('verify_code', methods=['POST'])
def verify_code():
    data = request.get_json()
    email = data.get('email', '')
    code = data.get('code', '')
    res = control.verify_code(email, code)
    if res == True:
        return json_data({
            'success': True,
            'code': service_config.CODE_SUCCESS
        })
    else:
        return json_data({
            'success': False,
            'code': service_config.CODE_FAIL
        })


@view_main.route('success', methods=['GET'])
def success():
    return render_template('success.html')


@view_main.route('time', methods=['GET'])
def rest_block_time():
    return str(control.get_rest_block_time('1422850017@qq.com', 24 * 60 * 60))