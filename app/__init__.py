from flask import Flask
from flask_cors import CORS

def create_app(config_name='development'):
    app = Flask(__name__)
    app.jinja_env.auto_reload = True
    CORS(app, resources=r'/*') #所有URL都允许跨域

    from app.siteAdmin import siteAdmin as siteAdmin
    app.register_blueprint(siteAdmin, url_prefix='/')

    from app.device_uploadinfo import device_uploadinfo as device_uploadinfo
    app.register_blueprint(device_uploadinfo, url_prefix='/device_uploadinfo')
    return app



