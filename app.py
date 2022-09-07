import os

from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


def do_query(params):
    with open(os.path.join(DATA_DIR, params["file_name"])) as f:
        file_data = f.readlines()

    if params['cmd1'] == 'filter':
        result = filter(lambda record: params["value1"] in record, file_data)

    return list(result)


@app.route("/perform_query", methods=["POST"])
def perform_query():
    # получить параметры query и file_name из request.args, при ошибке вернуть ошибку 400
    # проверить, что файла file_name существует в папке DATA_DIR, при ошибке вернуть ошибку 400
    # с помощью функционального программирования (функций filter, map), итераторов/генераторов сконструировать запрос
    # вернуть пользователю сформированный результат

    data = request.json
    file_name = data["file_name"]
    if not os.path.exists(os.path.join(DATA_DIR, file_name)):
        raise BadRequest

    return jsonify(do_query(data))


# app.response_class('Hello', content_type="text/plain")


if __name__ == "__main__":
    app.run()
