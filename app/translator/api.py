from app.translator import fanyi # 获取蓝图
from flask import request,session,render_template,flash,redirect,url_for
import translators as ts


@fanyi.route('/translator_en', methods=['GET', 'POST'])
def translator_en():
    result = None
    if request.method == 'POST':
        if request.form['translator_info'] != '':
            error = 'null'
        translator_info = request.form['translator_info']
        if is_contains_chinese(translator_info):
            result = ts.alibaba(translator_info, to_language='en', professional_field='general')
        else:
            result = ts.alibaba(translator_info, to_language='zh', professional_field='general')

    return render_template('fanyi.html', error=result)


def is_contains_chinese(strs):
    for _char in strs:
        if '\u4e00' <= _char <= '\u9fa5':
            return True
    return False