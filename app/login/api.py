from app.login import login # 获取蓝图
from flask import request,session,render_template,flash,redirect,url_for
from app import create_app


app = create_app ()

@login.route('/login_in', methods=['GET', 'POST'])  # 设置路由
def login_in():  # 执行的方法
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('index.show_entries'))
    return render_template('login.html', error=error)

@login.route('/login_out', methods=['GET'])
def login_out():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('index.show_entries'))
