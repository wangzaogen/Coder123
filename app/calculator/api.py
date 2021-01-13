from app.calculator import calc # 获取蓝图
from flask import request,session,render_template,flash,redirect,url_for



@calc.route('/calc_info', methods=['GET', 'POST'])  # 设置路由
def calc_info():  # 执行的方法
    result = None
    if request.method == 'POST':
        expression  = request.form['expression']
        print("result:{}".format(eval(expression)))
        result = eval(expression)

    return render_template('calc.html',result = result)


if __name__ == '__main__':

    print("result:{}".format(eval('1 + (5 - 2) * 3')))

