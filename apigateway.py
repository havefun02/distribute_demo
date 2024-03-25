from flask import Flask, request, jsonify
import requests
import json
app = Flask(__name__)

# Service URLs
ORDER_SERVICE_URL = 'http://127.0.0.1:5000'
PAYMENT_SERVICE_URL = 'http://127.0.0.1:5001'



@app.route('/')
def index():
    return "API Gateway is running!"

@app.route('/order', methods=['POST'])
def prepare_order():
    try:
        request_data = request.data
        # Forward request to message broker
        # forward_request_to_message_broker(request_data)
        # Forward request to order service
        response = requests.post(ORDER_SERVICE_URL + '/order', data=request_data)
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return str(e), 500


@app.route('/payment', methods=['POST'])
def process_payment():
    try:
        # Forward request to message broker
        # forward_request_to_message_broker(request.data)
        # Forward request to payment service
        response = requests.post(PAYMENT_SERVICE_URL + '/payment', data=request.data)
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000)
