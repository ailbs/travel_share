from flask import jsonify


class Response:
    # 标准成功代码
    ok_code = 0
    # 标准错误代码
    err_code = 1000000

    def __init__(self, code=ok_code, message='', data=None):
        self._code = code
        self._message = message
        self._data = data

    @staticmethod
    def Ok():
        return Response()

    @staticmethod
    def Err(code=err_code):
        return Response(code)

    # 设置数据
    def data(self, data):
        self._data = data
        return self

    # 设置代码
    def code(self, code):
        self._code = code
        return self

    # 设置返回信息
    def message(self, message):
        self._message = message
        return self

    # 构建返回
    def build(self):
        return jsonify(self.__str__())

    def __json__(self):
        return str(self)

    def __str__(self):
        return self.__dict__()

    def __dict__(self):
        return {
            'code': self._code,
            'message': self._message,
            'data': self._data
        }
