from flask import jsonify, request
from marshmallow import ValidationError
from collections.abc import Iterable
from .constants import HOST, PORT, DEBUG
from .validations import ListItemsInput
from .config import app

@app.route('/', methods=['POST'])
def resolve_matrix():
    try:
        schema = ListItemsInput()
        request_data = schema.load(request.json)

        lists = list(__plain_list(request_data['items']))

        return { 'result': lists }, 200

    except ValidationError:
        return { 'result': 'Please provided correct request, for example: { items: [1, 2] }' }, 400

def __plain_list(multi_lists):
    for list in multi_lists:
        if isinstance(list, Iterable) and not isinstance(list, str):
            for nested_list in __plain_list(list):
                yield nested_list
        else:
            yield list

def run_server():
    app.run(host=HOST, port=PORT, debug=DEBUG)
