from app.index import index
from flask import Flask, request,g, session, redirect, url_for, abort, \
    render_template, flash


# @index.route('/')  # 设置路由
# def index():  # 执行的方法
#     return 'This Page Is Index'



@index.route('/')
def show_entries():
    cur = g.db.execute('select title, text from entries order by id desc')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)


@index.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into entries (title, text) values (?, ?)',
                 [request.form['title'], request.form['text']])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('index.show_entries'))