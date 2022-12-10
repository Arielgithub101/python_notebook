from flask import Flask, request, jsonify, abort
import sqlite3
from typing import Dict

app = Flask(__name__)


def req_body_validation(data_obj: Dict):
    for key, value in data_obj.items():
        if key == 'friends' or len(value) == 0:
            return True
    return False
def db_connction():
    conn = None
    try:
        conn = sqlite3.connect("users.sqlite")
    except ConnectionError as e:
        print(e)
    return conn


books = [

    {'id': 0,
     'first_name': 'ariel',
     'last_name': 'cohen',
     'p_number': '123456789',
     'location': 'tlv',
     'gender': 'M',
     'rel_status': 'singel',
     'intersted_in': 'F',
     'hobbis': ["Ford", "BMW", "Fiat"],
     'friends': ["Ford", "BMW", "Fiat"]},
    {'id': 1,
     'first_name': 'yair',
     'last_name': 'cohen',
     'p_number': '123456789',
     'location': 'tlv',
     'gender': 'M',
     'rel_status': 'singel',
     'intersted_in': 'F',
     'hobbis': ["Ford", "BMW", "Fiat"],
     'friends': ["Ford", "BMW", "Fiat"]},
    {'id': 2,
     'first_name': 'shlomo',
     'last_name': 'cohen',
     'p_number': '123456789',
     'location': 'tlv',
     'gender': 'M',
     'rel_status': 'singel',
     'intersted_in': 'F',
     'hobbis': ["Ford", "BMW", "Fiat"],
     'friends': ["Ford", "BMW", "Fiat"]}
]


@app.route('/', methods=['GET'])
def home():
    return 'users list welcome: A prototype API for distant reading of science fiction novels.'


@app.route('/api/user/id', methods=['GET'])
def api_display_user():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if request.method == 'GET':
        if 'id' in request.args:
            id = int(request.args['id'])
        else:
            return abort(404)
        for book in books:
            if book['id'] == id:
                try:
                    book.pop('friends')
                    return jsonify(book), 200
                except Exception:
                    return jsonify(book), 200
        return f'User not found', 404


@app.route('/api/user', methods=['POST'])
def api_create_user():
    conn = db_connction()
    cursor = conn.cursor()
    if request.method == 'POST':
        # cursor = conn.execute("SELECT * FROM users")
        # users = [
        #     dict(id=row[0] for row in cursor.fetchall())
        #
        # ]
        if req_body_validation(request.json):
            return 'bad req', 400

        user_name = request.json['first_name']
        user_last = request.json['last_name']
        p_number = request.json['p_number']
        location = request.json['location']
        gender = request.json['gender']
        rel_status = request.json['rel_status']
        intersted_in = request.json['intersted_in']
        hobbis = request.json['hobbis']
        id = books[-1]['id'] + 1

        validation_user_exits = p_number
        for book in books:
            # שליפה יוזריפ\מספרי טלפון מהדיבי
            if book['p_number'] == validation_user_exits:
                return 'user alredy in system', 409

        new_obj = {'id': id,
                   'first_name': user_name,
                   'last_name': user_last,
                   'p_number': p_number,
                   'location': location,
                   'gender': gender,
                   'rel_status': rel_status,
                   'intersted_in': intersted_in,
                   'hobbis': hobbis}

        books.append(new_obj)
        return f'new user with id {new_obj["id"]} createdd!', 201


@app.route('/api/user/id', methods=['DELETE'])
def api_delete_user():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if request.method == 'DELETE':
        if 'id' in request.args:
            id = int(request.args['id'])
        else:
            return abort(404)
        for book in books:
            # חיבור לדיבי לבדיקה על יוזר למחיקה
            if book['id'] == id:
                books.pop(books.index(book))
                return f'User with id {id} deleted', 200
        return f'User not found', 404


@app.route('/api/users', methods=['DELETE'])
def api_delete_all_user():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if request.method == 'DELETE':
        # חיבור לדיבי לבדיקה על יוזר למחיקה של כולם
        books.clear()
        return f'all users dleted', 200


@app.route('/api/user/id', methods=['PATCH'])
def api_update_user():
    if request.method == 'PATCH':
        if 'id' in request.args:
            id_d = int(request.args['id'])
        else:
            return abort(404)

        if req_body_validation(request.json):
            return 'bad req', 400

        for book in books:
            if book['id'] == 1:
                # חיבור לדידי לשליפת תונים

                book['first_name'] = request.json['first_name']
                book['last_name'] = request.json['last_name']
                book['p_number'] = request.json['p_number']
                book['location'] = request.json['location']
                book['gender'] = request.json['gender']
                book['rel_status'] = request.json['rel_status']
                book['intersted_in'] = request.json['intersted_in']
                book['hobbis'] = request.json['hobbis']
                # book['friends'] = request.json['friends']

                update_obj = {
                    'id': id_d,
                    'first_name': book['first_name'],
                    'last_name': book['last_name'],
                    'p_number': book['p_number'],
                    'location': book['location'],
                    'gender': book['gender'],
                    'rel_status': book['rel_status'],
                    'intersted_in': book['intersted_in'],
                    'hobbis': book['hobbis'],
                    'friends': book['friends']}
                return jsonify(update_obj), 200
        return f'User not found', 404


# if request.method == 'DELETE':
#     for book in books:
#         if book['id'] == id:
#             books.pop(books.index(book))
#             return jsonify(books)

# @app.route('/api/create/user', methods=['GET', 'POST'])
# def api_create_user():
#     if request.method == 'GET':
#         return jsonify(books), 200
#     if request.method == 'POST':
#         user_name = request.json['first_name']
#         user_last = request.json['last_name']
#         p_number = request.json['p_number']
#         location = request.json['location']
#         gender = request.json['gender']
#         rel_status = request.json['rel_status']
#         intersted_in = request.json['intersted_in']
#         hobbis = request.json['hobbis']
#         friends = request.json['friends']
#         id = books[-1]['id'] + 1
#
#         new_obj = {'id': id,
#                    'first_name': user_name,
#                    'last_name': user_last,
#                    'p_number': p_number,
#                    'location': location,
#                    'gender': gender,
#                    'rel_status': rel_status,
#                    'intersted_in': intersted_in,
#                    'hobbis': hobbis,
#                    'friends': friends}
#         books.append(new_obj)
#         return  f'new user with id {new_obj["id"]} createdd!',200




@app.route('/api/try/id/friend', methods=['GET'])
def api_delete_id():
    if 'id' in request.args:
        id = int(request.args['id'])
        return f'this is work {id}'
    else:
        return 'not god',404



@app.route('/api/deleteAll/user', methods=['GET'])
def api_delete_all():
    pass


@app.route('/api/update/user/id', methods=['GET'])
def api_update_id():
    pass


if __name__ == '__main__':
    app.run(debug=True)
