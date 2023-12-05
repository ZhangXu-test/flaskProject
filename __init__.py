# -- coding: utf-8 --
# date：2023/12/5 10:28
# author: ZhangXu

from flask import Flask


def create_app():
    app = Flask(__name__)
    app.secret_key = 'abc'
    
    @app.route('/index')
    def index():
        return "index"

    from views.pp1 import pp1
    from views.pp2 import pp2

    app.register_blueprint(pp1, url_prefix="/admin")
    app.register_blueprint(pp2, url_prefix="/client")

    return app
