from flask import Flask, jsonify, request
import requests

app = Flask(__name__)
users = [{
    "id": 0,
    "name": "cerulean",
    "year": 2000,
    "color": "#98B2D1",
    "pantone_value": "15-4020"
}, {
    "id": 1,
    "name": "fuchsia rose",
    "year": 2001,
    "color": "#C74375",
    "pantone_value": "17-2031"
}, {
    "id": 2,
    "name": "true red",
    "year": 2002,
    "color": "#BF1932",
    "pantone_value": "19-1664"
}, {
    "id": 3,
    "name": "aqua sky",
    "year": 2003,
    "color": "#7BC4C4",
    "pantone_value": "14-4811"
}, {
    "id": 4,
    "name": "tigerlily",
    "year": 2004,
    "color": "#E2583E",
    "pantone_value": "17-1456"
}, {
    "id": 5,
    "name": "blue turquoise",
    "year": 2005,
    "color": "#53B0AE",
    "pantone_value": "15-5217"
}]


@app.route('/')
def index():
    return "Welcome to the API, This API is built for demo"


@app.route("/users", methods=['GET'])
def get():
    """this function is used to get the contents of the Users using the GET method"""
    return jsonify({'msg': 'users displayed successfully'}, {'users': users})


@app.route("/users/cookies", methods=['GET'])
def get_cookies():
    cookies = dict(cookies_are='working')
    return jsonify({'cookies':{'cookies_are':'working'}})

# @app.route("/users/<int:id>", methods=['GET'])
# def get_users(id):
#     """this function is returning the contents using IDs"""
#     return jsonify({'users': users[id]})


@app.route("/users/<int:id>", methods=['POST'])
def create_user(id):
    for user in users:
        if users[id] == id:
            req_data = request.get_json()
            new_item = {

                'name': req_data['name'],
                'year': req_data['year'],
                'color': req_data['color'],
                'pantone_value': req_data['pantone_value']
            }
            users[id].append(new_item)
        return jsonify("User added succesfully", users)

    # new_user = request.get_json()
    # users.append(new_user)
    # return jsonify("updated successfully", {'users': users})


@app.route("/users/<int:id>", methods=['PUT'])
def update_user(id):
    new_user = request.get_json()
    for i, q in enumerate(users):
        if q['id'] == id:
            users[i] = new_user
    us = request.get_json()
    return jsonify("Updated successfully", {'users': users})


# @app.route("/users/<int:id>", methods=['DELETE'])
# def delete_user(id):
#     for index, name in enumerate(users):
#         if users[id] == id:
#             users.pop(index)
#     return jsonify(users)
@app.route("/users/<int:id>", methods=['DELETE'])
def delete_user(id):
    new_id = [user for user in users if users[id] == id]
    if len(new_id) > 0:
        users.remove(new_id[0])
    return jsonify("Deleted Successfully", {'users': users})
    # id = users[-1]['id'] + 1
    # new_name = request.form['name']
    # new_year = request.form['year']
    # new_color = request.form['color']
    # new_pantone_value = request.ge
    # new_obj = {
    #     'id': id,
    #     'name': new_name,
    #     'year': new_year,
    #     'color': new_color,
    #     'pantone_value': new_pantone_value
    # }
    # users.append(new_obj)
    # return jsonify(users)


# @app.route("/users/<int:id>", methods=['PUT', 'GET', 'DELETE'])
# def book_put_get_del():
#     """this method is for HTTP methods GET,PUT and DELETE using ids"""
#     if request.method == "GET":
#         for user in users:
#             if user['id'] == id:
#                 return jsonify(user)
#     elif request.method == "PUT":
#         for user in users:
#             if user['id'] == id:
#
#     elif request.method == "DELETE":
#         for index,book in enumerate(users):
#             if users[id] == id:
#                 users.pop(index)
#                 return jsonify(users)


# @app.route("/users/<int:id>", methods=['PUT'])
# def user_update(id):
#     users[id]['name'] = "f"
#     return jsonify({'users': users[id]})
#
#
# @app.route("/users/<int:id>", methods=['DELETE'])
# def delete_user(id):
#     users.remove(users[id])
#     return jsonify({'result': True})


if __name__ == "__main__":
    print(get.__doc__)

    app.run(debug=True)
