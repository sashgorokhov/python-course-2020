from werkzeug.exceptions import abort

from app import app
from flask import jsonify, request


@app.route('/')
def hello_world():
    return "Hello world!"


ORDERS = [
    {
        'id': 1,
        'item': 'Notebook',
        'price': 500000
    },
    {
        'id': 2,
        'item': 'Book, Fluent Python',
        'price': 10000
    },
]


@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(ORDERS)


@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    orders = [order for order in ORDERS if order['id'] == order_id]
    return jsonify(orders)


@app.route('/orders', methods=['POST'])
def create_order():
    if not request.json:
        abort(400)

    if 'item' not in request.json or 'price' not in request.json:
        abort(400)

    order = {
        'id': ORDERS[-1]['id'] + 1,
        'item': request.json['item'],
        'price': request.json['price']
    }
    ORDERS.append(order)

    return jsonify(order), 201


@app.route('/orders/<int:order_id>', methods=['PUT'])
def edit_order(order_id):
    if not request.json:
        abort(400)

    if 'item' not in request.json or 'price' not in request.json:
        abort(400)

    orders = [order for order in ORDERS if order['id'] == order_id]
    if not orders:
        return jsonify({'error': "Resource not found"}), 404

    orders[0]['item'] = request.json['item']
    orders[0]['price'] = request.json['price']
    return jsonify(orders[0])


@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    orders = [order for order in ORDERS if order['id'] == order_id]
    if not orders:
        return jsonify({'error': "Resource not found"}), 404

    ORDERS.remove(orders[0])
    return jsonify({'result': True})
