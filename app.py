from flask import Flask, jsonify, request

app = Flask(__name__)

products = [
    {
        "id": 1,
        "name": "tomatoe",
        "quantity": 3},
    {
        "id": 2,
        "name": "onion",
        "quantity": 10
    }
]


def uuid():
    max_id = 0

    for product in products:
        if product["id"] > max_id:
            max_id = product["id"]

    max_id += 1

    return max_id


@app.route('/products', methods=["GET"])
def get_products():
    return jsonify(products), 200


@app.route('/products/<int:idx>', methods=["GET"])
def get_product(idx):
    for product in products:
        if product["id"] == idx:
            return jsonify(product), 200
    return f"No data with id:{idx}", 404


@app.route('/products/<int:idx>', methods=["DELETE"])
def delete_product(idx):
    for product in products:
        if product["id"] == idx:
            products.remove(product)
            return jsonify({}), 200
    return f"No data with id:{idx}", 404


@app.route('/products', methods=["POST"])
def create_products():
    data = request.json
    data["id"] = uuid()
    products.append(data)

    return jsonify(data), 201


if __name__ == '__main__':
    app.run(debug=True)
