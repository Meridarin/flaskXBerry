from flask import Flask, jsonify, request
import math

app = Flask(__name__)

@app.route("/getProducts")
def getProducts():

  product_list = {
    "products": [
      {
        "name": "Chleb",
        "price": 2,
        "weight": 0.5
      },
      {
        "name": "Woda",
        "price": 1,
        "weight": 2
      },
      {
        "name": "Cukier",
        "price": 5,
        "weight": 1
      },
      {
        "name": "Cola",
        "price": 7,
        "weight": 1.5
      },
      {
        "name": "Paluszki",
        "price": 4,
        "weight": 0.2
      }
    ]
  }

  return jsonify(product_list), 200

@app.route("/order", methods=['POST'])
def order():
  req_json = request.get_json()
  if not req_json['price']:
    return jsonify({'message': 'no price field!'}), 404
  price = math.ceil(req_json['price'] * 1.23)
  return jsonify({"price": price}), 200