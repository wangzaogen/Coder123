from flask import Blueprint

from config import TEMPLATES_DIR, STATICFILES_DIR

calc = Blueprint('calc', __name__,
                   template_folder=TEMPLATES_DIR,
                   static_folder=STATICFILES_DIR)  # 创建一个蓝图对象，设置别名，模板文件地址，静态文件地址

from app.calculator import api  #