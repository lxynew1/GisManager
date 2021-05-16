# 注册管理路由:主要包括首页、链接库、
from flask import Blueprint
device_uploadinfo = Blueprint('device_uploadinfo', __name__)
from . import view
