from app.search import search # 获取蓝图
from flask import request,session,render_template,flash,redirect,url_for

search_en = {'baidu':'https://www.baidu.com/s?word={}'}
search_en['google'] = 'https://www.google.com/search?q={}&oq=1&sourceid=chrome&ie=UTF-8'
search_en['bing'] = 'https://cn.bing.com/search?q={}'

@search.route('/search_info', methods=['GET', 'POST'])  # 设置路由
def search_info():  # 执行的方法
    if request.method == 'POST':
        search_type = request.form['search_type']
        search_info = request.form['search_info']
        print("search_type:{}".format(search_type))
        print("search_info:{}".format(search_info))
        for key in search_en:
            if key == search_type:
                return redirect(str(search_en[key]).format(search_info))

    return render_template('search.html')

