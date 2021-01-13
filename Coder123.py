from app import create_app
from flask import g,render_template,session,flash,redirect,url_for
import db_option
from app.login import login
from app.index import index
from app.translator import fanyi
from app.search import search
from app.calculator import calc

app = create_app ()  # 创建app
app.register_blueprint (login, url_prefix='/login')  # 注册蓝图
app.register_blueprint (index, url_prefix='/index')  # 注册蓝图
app.register_blueprint (index, url_prefix='/show_entries')  # 注册蓝图
app.register_blueprint (fanyi, url_prefix='/fanyi')  # 注册蓝图
app.register_blueprint (search, url_prefix='/search')  # 注册蓝图
app.register_blueprint (calc, url_prefix='/calc')  # 注册蓝图

@app.before_request
def before_request():
    g.db = db_option.get_db()



if __name__ == '__main__':
    app.run()
