from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data structure to store users and products
data = {
    'users': [],
    'products': []
}

# CRUD operations for users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(data['users'])

@app.route('/users', methods=['POST'])
def add_user():
    new_user = request.json
    data['users'].append(new_user)
    return jsonify(new_user), 201

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in data['users'] if user['id'] == user_id), None)
    return jsonify(user) if user else ('', 404)

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((user for user in data['users'] if user['id'] == user_id), None)
    if user:
        updated_user = request.json
        user.update(updated_user)
        return jsonify(user)
    return ('', 404)

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global data
    data['users'] = [user for user in data['users'] if user['id'] != user_id]
    return ('', 204)

# CRUD operations for products
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(data['products'])

@app.route('/products', methods=['POST'])
def add_product():
    new_product = request.json
    data['products'].append(new_product)
    return jsonify(new_product), 201

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((product for product in data['products'] if product['id'] == product_id), None)
    return jsonify(product) if product else ('', 404)

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = next((product for product in data['products'] if product['id'] == product_id), None)
    if product:
        updated_product = request.json
        product.update(updated_product)
        return jsonify(product)
    return ('', 404)

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    global data
    data['products'] = [product for product in data['products'] if product['id'] != product_id]
    return ('', 204)

if __name__ == '__main__':
    app.run(debug=True)