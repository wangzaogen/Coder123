from flask import jsonify


class Response(object):
    def success(self, data=[]):
        return jsonify({'code': 200, 'msg': '成功！', 'data': data})

    def failed(self, msg='', code=500):
        return jsonify({'code': code, 'msg': '失败！错误信息：[' + str(msg) + ']'})

    def refuse(self, msg=''):
        return jsonify({'code': 403, 'msg': '失败！没有权限进行此操作。' + str(msg)})
