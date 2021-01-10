from app import create_app
from flask import g,render_template
import db_option
from app.login import login
from app.index import index

app = create_app ()  # 创建app
app.register_blueprint (login, url_prefix='/login')  # 注册蓝图
app.register_blueprint (index, url_prefix='/index')  # 注册蓝图
app.register_blueprint (index, url_prefix='/show_entries')  # 注册蓝图

@app.before_request
def before_request():
    g.db = db_option.get_db()

@app.route('/')
def show_entries():
    cur = g.db.execute('select title, text from entries order by id desc')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)

if __name__ == '__main__':
    app.run()
