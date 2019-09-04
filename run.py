import os
from flask import Flask
from log import log_init
from view.view import view_main


APP_ROOT_PATH = os.getcwd()


app = Flask(__name__)
app.register_blueprint(view_main)


log_init.init(APP_ROOT_PATH)


@app.route('/')
def hello_world():
    return 'hello world'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)