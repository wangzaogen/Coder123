from flask import Flask
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "coder123")


def create_app():
    """ 创建app的方法 """
    app = Flask(__name__,static_folder="../static",template_folder="../templates")  # 生成Flask对象
    app.config['DATABASE'] = db_path
    app.config['USERNAME'] = 'demo'
    app.config['PASSWORD'] = '1234'
    app.secret_key = 'wang'
    # 在这还可以设置好配置后， 初始化其他的模块

    return app  # 返回Flask对象app


