from app.login import login # 获取蓝图
import requests
from flask import request,session,render_template,flash,redirect,url_for
from app import create_app
prefix='/login'

app = create_app ()

@login.route('/', methods=['GET', 'POST'])  # 设置路由
def login():  # 执行的方法
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)



# @login.route(prefix+'/in', methods=['GET', 'POST'])
# def login_in():
#     error = None
#     if request.method == 'POST':
#         if request.form['username'] != app.config['USERNAME']:
#             error = 'Invalid username'
#         elif request.form['password'] != app.config['PASSWORD']:
#             error = 'Invalid password'
#         else:
#             session['logged_in'] = True
#             flash('You were logged in')
#             return redirect(url_for('show_entries'))
#     return render_template('login.html', error=error)